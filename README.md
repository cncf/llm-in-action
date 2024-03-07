# LLMs in Action: A Cloud Native Story

## Prerequisites

- [Docker](https://docs.docker.com/install/)
  - Docker is a platform for developers and sysadmins to develop, ship, and run applications. Docker enables you to separate your applications from your infrastructure so you can deliver software quickly.
- [Ollama](https://ollama.com/)
  - Ollama is a Language Model as a Service (LMaaS) that provides a RESTful API for interacting with large language models. It's a great way to get started with LLMs without having to worry about the infrastructure.
- [kind](https://kind.sigs.k8s.io/)
  - kind is "Kubernetes in Docker," used by the Kubernetes project to help test features and run integration tests. It turns out it's a handy way for anyone to spin up a cluster quickly. Big thank you to @bentheelder for developing it 👏🏼 👏🏼
- [kubectl](https://kubernetes.io/docs/tasks/tools/install-kubectl/)
  - kubectl is how you interact with k8s using the command line. This allows you to become a k8s whisperer :-)

With Ollama installed on your machine, you will need to pull the LLaVa model by running

```sh
ollama pull llava
```

You can verify that the model is installed by running

```sh
ollama list

NAME            ID           SIZE   MODIFIED
llava:latest    8dd30f6b0cb1 4.7 GB 17 seconds ago 
```

## Startup

We have crafted a few scripts to make this demo run as quickly as possible on your machine once you've installed the prerequisites.

This script will:

- Create a kind cluster
- Apply the Kubernetes manifests we need for our demo
- Use port-forwarding to help us access our service in the browser so we can take photos and describe them with LLaVa (Large Language and Vision Assistant)

```sh
./startup.sh
```

To access the service, open your browser and navigate to [http://localhost:8501](http://localhost:8501)

## Shutdown

To shut down the demo, run the following command, which will:

- Remove the Kubernetes manifests
- Remove the port-forwarding
- Delete the kind cluster

```sh
./shutdown.sh
```

## Operating System Information

This demo has been tested on the following operating systems and will work if you have the prerequisites installed.

- macOS
- Linux
- Windows
