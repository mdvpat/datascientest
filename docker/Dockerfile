FROM python

RUN apt update && apt install curl build-essential -y
RUN pip install -U flask numpy pandas sklearn joblib

RUN mkdir /detecter
RUN mkdir /detecter/.kube

RUN useradd detecter

COPY detecter.py /detecter
COPY model.joblib /detecter
WORKDIR /detecter

RUN chown -R detecter:detecter /detecter
WORKDIR /detecter
USER detecter

CMD python3 detecter.py
