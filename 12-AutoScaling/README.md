## Create a Load Gen Busybox Pod: 

```
kubectl.exe run -it load-gen --image=busybox:1.28 -- sh
```

## Check the resolve.conf file 
```
cat /etc/resolve.conf
```

## Check the DNS Lookup 
```
nslookup hpa-example
```
```
Name:      hpa-example
Address 1: 172.20.48.145 hpa-example.default.svc.cluster.local
```

## Check the Service is reachable or not
```
wget hpa-example.default.svc.cluster.local
```
## Check the current pods,top,hpa status 
```
kubectl get pods,hpa
```

```
kubectl top pods 
```


## Now Genrate the load 
```
while true; do wget -q -O- http://hpa-example.default.svc.cluster.local:31001; done
```


## Now you can see HPA in Action to Check, check the current pods,top,hpa status 
```
kubectl get pods,hpa
```

```
kubectl top pods 
```
