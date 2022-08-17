FROM python:3-alpine

RUN apk add curl
RUN pip install -U flask

RUN mkdir /detecter
RUN mkdir /detecter/.kube

RUN adduser -D detecter

COPY detecter.py /detecter
WORKDIR /detecter

RUN chown -R detecter:detecter /detecter
WORKDIR /detecter
USER detecter

CMD python3 detecter.py
