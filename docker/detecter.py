import os
from flask import Flask, jsonify, request

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
    data = request.json
    
    pass

if __name__ == '__main__':
    app.run(host="localhost", port=API_PORT)
