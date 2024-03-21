# Mutual TLS Migration

## Create two sample namespaces & deploy http & sleep app respectivly 

```
kubectl create ns ns1
kubectl apply -f <(istioctl kube-inject -f http.yaml) -n ns1
kubectl apply -f <(istioctl kube-inject -f sleep.yaml) -n ns1
kubectl create ns ns2
kubectl apply -f <(istioctl kube-inject -f http.yaml) -n ns2
kubectl apply -f <(istioctl kube-inject -f sleep.yaml) -n ns2
```

## Create another namespace, legacy, and deploy sleep without a sidecar:
```
kubectl create ns legacy
kubectl apply -f sleep.yaml -n legacy
```

## Verify the setup by sending http requests (using curl) from the sleep pods, in namespaces: 
```
for from in "ns1" "ns2" "legacy"; do for to in "ns1" "ns2"; do kubectl exec "$(kubectl get pod -l app=sleep -n ${from} -o jsonpath={.items..metadata.name})" -c sleep -n ${from} -- curl http://httpbin.${to}:8000/ip -s -o /dev/null -w "sleep.${from} to httpbin.${to}: %{http_code}\n"; done; done
```

## Enable mutual TLS by namespace
```
kubectl apply -n ns1 -f - <<EOF
apiVersion: security.istio.io/v1beta1
kind: PeerAuthentication
metadata:
  name: "default"
spec:
  mtls:
    mode: STRICT
EOF
```

## Now, you should see the request from sleep.legacy to httpbin.ns1 failing.
```
for from in "ns1" "ns2" "legacy"; do for to in "ns1" "ns2"; do kubectl exec "$(kubectl get pod -l app=sleep -n ${from} -o jsonpath={.items..metadata.name})" -c sleep -n ${from} -- curl http://httpbin.${to}:8000/ip -s -o /dev/null -w "sleep.${from} to httpbin.${to}: %{http_code}\n"; done; done
```

## Now, enable mutual TLS for the entire mesh:
```
kubectl apply -n istio-system -f - <<EOF
apiVersion: security.istio.io/v1beta1
kind: PeerAuthentication
metadata:
  name: "default"
spec:
  mtls:
    mode: STRICT
EOF
```

## Now, both the ns1 and ns2 namespaces enforce mutual TLS only traffic, so you should see requests from sleep.legacy failing for both.
```
for from in "ns1" "ns2" "legacy"; do for to in "ns1" "ns2"; do kubectl exec "$(kubectl get pod -l app=sleep -n ${from} -o jsonpath={.items..metadata.name})" -c sleep -n ${from} -- curl http://httpbin.${to}:8000/ip -s -o /dev/null -w "sleep.${from} to httpbin.${to}: %{http_code}\n"; done; done
```


## Clean up
```
 kubectl delete peerauthentication -n istio-system default
```

## Enable mutual TLS per workload
```
cat <<EOF | kubectl apply -n ns1 -f -
apiVersion: security.istio.io/v1beta1
kind: PeerAuthentication
metadata:
  name: "httpbin"
  namespace: "ns1"
spec:
  selector:
    matchLabels:
      app: httpbin
  mtls:
    mode: STRICT
EOF
```

## Now, peer authentication policy enables strict mutual TLS for the httpbin.ns1 workload:, so you should see requests from sleep.legacy failing for both.
```
for from in "ns1" "ns2" "legacy"; do for to in "ns1" "ns2"; do kubectl exec "$(kubectl get pod -l app=sleep -n ${from} -o jsonpath={.items..metadata.name})" -c sleep -n ${from} -- curl http://httpbin.${to}:8000/ip -s -o /dev/null -w "sleep.${from} to httpbin.${to}: %{http_code}\n"; done; done
```

## Clean up
```
 kubectl delete peerauthentication -n istio-system default
```


## Remove the test Namespaces
```
kubectl delete ns ns1 ns2 legacy
```

