# Install ISTIO 

## Download Istio Utils 
```
 cd /root
 curl -L https://istio.io/downloadIstio | sh -
```

## Export the Path in bashrc 
```
export PATH="$PATH:/root/istio-1.15.1/bin/"
```

## Install Istio with demo profile 
```
istioctl install --set profile=demo -y
```

## Enable Default Namespace for Istio Injection 
```
kubectl label namespace default istio-injection=enabled
```

## Deploy the Sample BookInfo Application from Istio Downloads: 
```
cd istio<tab>
kubectl apply -f samples/bookinfo/platform/kube/bookinfo.yaml
```

## Check the status of BookInfo App & Ingress svc: 
```
kubectl get svc 
kubectl get svc -n istio-system 
```

## As of now app is only accessable with in the cluster, let's open it to outsider world. 

## Deploy Gateway & Virtual Service
```
kubectl apply -f samples/bookinfo/networking/bookinfo-gateway.yaml
```

## Now we can access bookinfo app on Ingress LB URL with productpage context path. 

```
curl http://<IngressLB_IP>/productpage
```
