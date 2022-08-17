#!/bin/bash

# build image
docker build -t muraduiurie/fraud-det ./docker

# push image
docker pull muraduiurie/fraud-det

# deploy image
kubectl delete -f kubernetes
kubectl apply -f kubernetes
