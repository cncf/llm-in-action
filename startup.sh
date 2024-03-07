#!/bin/bash

echo "Create the kind cluster..."
kind create cluster --config cluster.yaml

kind -n llm load docker-image onlydole/llm-in-action:latest

echo "Applying the Kubernets manifests..."
kubectl apply -f kubernetes/deployment.yaml
kubectl apply -f kubernetes/service.yaml

# Wait for the pod starting with "keynote" to be running
while [[ $(kubectl get pods --no-headers | grep 'keynote' | awk '{print $3}') != "Running" ]]; do
  echo "Keynote demo is starting, make some noise..."
  sleep 10
done

echo "Forwarding the Keynote pod..."
kubectl port-forward svc/keynote 8501:8501 &

echo "Keynote demo is running, it's time to present! Open your browser to http://localhost:8501"