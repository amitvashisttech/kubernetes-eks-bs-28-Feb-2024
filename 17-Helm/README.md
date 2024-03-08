# Install Helm

## Download the latest version of helm : as of today: 3.4.2
```
wget https://get.helm.sh/helm-v3.4.2-linux-amd64.tar.gz
tar -zxvf helm-v3.4.2-linux-amd64.tar.gz
sudo mv linux-amd64/helm /usr/local/bin/helm
```

## Initialize Helm
```
kubectl create -f helm-rbac.yaml
```

## Install Nginx Web App.
```
helm repo add azure-marketplace https://marketplace.azurecr.io/helm/v1/repo
helm search repo nginx
helm install first-nginx azure-marketplace/nginx-test
helm list
helm history first-nginx
helm delete first-nginx

```

Have Fun.!!

