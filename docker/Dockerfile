FROM python:3-alpine

RUN apk add curl gcc alpine-sdk
RUN pip install -U flask numpy pandas sklearn joblib

RUN mkdir /detecter
RUN mkdir /detecter/.kube

RUN adduser -D detecter

COPY detecter.py /detecter
COPY model.joblib /detecter
WORKDIR /detecter

RUN chown -R detecter:detecter /detecter
WORKDIR /detecter
USER detecter

CMD python3 detecter.py
