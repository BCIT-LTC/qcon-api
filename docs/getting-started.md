# Getting Started

!!! warning "This dev environment makes some very opinionated assumptions..."
    * You have push registry authorization to `registry.dev.ltc.bcit.ca`
    * You have login credentials for the development cluster, [rancher2.dev.ltc.bcit.ca](https://rancher2.dev.ltc.bcit.ca)

## 1. Install dependencies
* [git](https://git-scm.com/downloads)
* [Docker](https://www.docker.com/products/docker-desktop)
* [Kubernetes-cli](https://kubectl.docs.kubernetes.io/)
    * Install both:
        * kubectl
        * kustomize
* [Skaffold](https://skaffold.dev/)

!!! tip "Windows git shim"
    * If you're using Windows, make sure you're line endings are sane
    ```shell
    git config --system --edit` && set `autocrlf = false
    ```


## 2. Clone the project

```shell
git clone https://issues.ltc.bcit.ca/web-apps/qcon/qcon-api.git
```

## 3. Login to the container registry

```shell
docker login registry.dev.ltc.bcit.ca
```

## 4. Configure Skaffold

```shell
skaffold config set default-repo registry.dev.ltc.bcit.ca/web-apps/qcon
```

## 5. Configure the Kubernetes context

```shell
kubectl config set-context {cluster}
```

??? hint "Config file merge script"
    Where new config is in `~/.kube/config.new`:
    
    ```shell
    cd ~/.kube/ && cp config config.bak \
    && KUBECONFIG=config.new:config kubectl config view \
    --merge --flatten > config
    ```

## 6. Run Skaffold (using your profile)
```
skaffold dev -p {profile}
```

## 7. Access the app via NodePort
1. login to `rancher2.dev.ltc.bcit.ca`
2. click on the `development` > `default` namespace
3. click on the *NodePort link* under your namespaces' workload