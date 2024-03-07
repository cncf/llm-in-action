#!/bin/bash

echo "Deleting the Kubernetes manifest for this demo..."
kubectl delete -f kubernetes/

# Use pgrep to find the PIDs of the processes with 'kubectl port-forward' command
pids=$(pgrep -f "kubectl port-forward")

if [ -z "$pids" ]; then
    echo "No kubectl port-forward processes found."
else
    # Display the PIDs and kill them
    for pid in $pids; do
        echo "Terminating process with PID: $pid"
        kill $pid
        if [ $? -eq 0 ]; then
            echo "Successfully terminated process with PID: $pid"
        else
            echo "Failed to terminate process with PID: $pid. You may need to run the script as root or use 'sudo'."
        fi
    done
fi

echo "Delete the kind cluster to clean up our machine..."
kind delete cluster -n llm