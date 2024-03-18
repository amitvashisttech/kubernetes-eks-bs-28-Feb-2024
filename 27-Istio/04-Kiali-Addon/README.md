### Deploy Promentheus & Kiali
```
  kubectl apply -f 01-Kiali.yaml
  kubectl apply -f 02-Prometheus.yaml
```

### Gernrate Traffic for the Kiali Graphs  
```
  for i in $(seq 1 20); do  curl -s -o /dev/null "http://ab895612f41824c0b9abbe756c553f0d-1045744848.ap-south-1.elb.amazonaws.com/productpage"; done
  for i in $(seq 1 20); do  curl -s -o /dev/null "http://ab895612f41824c0b9abbe756c553f0d-1045744848.ap-south-1.elb.amazonaws.com/hello"; done
```
  
### Expose Kiali on LoadBalancer Type: 
```
kubectl edit svc kiali -n istio-system
```
