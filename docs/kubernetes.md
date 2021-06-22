---
title: Running Qcon-api in Kubernetes
---
# Running Qcon-api in a Kubernetes cluster

Qcon-api deployments are configured to be independent, ephemeral containers that scale horizontally.

To evaluate a Qcon-api Kubernetes deployment, spin up a [Kind](https://kind.sigs.k8s.io/docs/user/quick-start/) or [Minikube](https://minikube.sigs.k8s.io/docs/start/) cluster with an Ingress addon and run the following:

```
kubectl apply -k overlays/prod
```

Qcon-api deploys into the `web-apps` namespace. Get the deployment's external IP:

```
kubectl get ing qcon-api -g web-apps
```

Send a formatted Word file to the Qcon-api service with [cURL](https://curl.se/):

```
curl -X {ExternalIP} -f `formatted-document.docx`
```

The service returns a ...