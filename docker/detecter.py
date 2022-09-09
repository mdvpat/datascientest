# /status
# /verify

import os, sys
import traceback
from flask import Flask, jsonify, request
import numpy as np
import pandas as pd
import json
from sklearn.ensemble import RandomForestClassifier
from joblib import dump, load
import joblib

API_HOST = os.environ["API_HOST"]
API_PORT = os.environ["API_PORT"]

app = Flask(__name__)

@app.route("/health")
def health():
    return jsonify({"status": "ok"})

@app.route("/status")
def status():
    pass

@app.route("/verify", methods=["POST"])
def verify():
    try:
        input = request.get_json()
        print(f"verifying: {data}")
        ## Model Params
        model=joblib.load('model.joblib')
        print(model.estimators_)
        ## Input Json // csv input will be implemented later
        df = pd.read_json(input)
        ### Check structure

        df.head()
        ## Transform input : to be pipelined
        df["signup_time"] = pd.to_datetime(df["signup_time"])
        df["purchase_time"] = pd.to_datetime(df["purchase_time"])
        df["delta"]=(df["purchase_time"]-df["signup_time"])

        ## Encodage variables sex,browser et source en numériques
        df.source = pd.Categorical(df.source)
        df.sex = pd.Categorical(df.sex)
        df.browser = pd.Categorical(df.browser)
        df["source"] = df["source"].cat.codes
        df["sex"] = df["sex"].cat.codes
        df["browser"] = df["browser"].cat.codes

        ## Variables à supprimer
        df=df.drop("user_id",1)
        df=df.drop("signup_time",1)
        df=df.drop("purchase_time",1)
        df=df.drop("device_id",1)
        df=df.drop("ip_address",1)
        df=df.drop("is_fraud",1)
        ### Delta en heures
        df["delta"]=df["delta"].dt.total_seconds()
        df["delta"]=pd.to_numeric( df["delta"])/3600

        ## Feed input to Model
        df["is_fraud"]=model.predict(df)
        #print("\nRandom Forrest report \n",classification_report(df["is_fraud"], model))


        ## Send Answer
        #ans=df.to_json(orient="index")
        ans={'is_fraud' : df["is_fraud"]}
        
        return jsonify(ans)
    except Exception as e:
        exc_info = sys.exc_info()
        return ''.join(traceback.format_exception(*exc_info))

if __name__ == '__main__':
    app.run(host=API_HOST, port=API_PORT)
