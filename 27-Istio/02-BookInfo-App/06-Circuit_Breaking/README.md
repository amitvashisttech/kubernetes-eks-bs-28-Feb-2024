## Genrate Traffic 

### Log in to the client pod and use the fortio tool to call httpbin. Pass in curl to indicate that you just want to make one call:
```
export FORTIO_POD=$(kubectl get pods -l app=fortio -n bookinfo-istio -o 'jsonpath={.items[0].metadata.name}')
```
```
kubectl -n bookinfo-istio exec "$FORTIO_POD" -c fortio -- /usr/bin/fortio curl -quiet http://httpbin:8000/get
```


## Tripping the circuit breaker

### In the DestinationRule settings, you specified maxConnections: 1 and http1MaxPendingRequests: 1. These rules indicate that if you exceed more than one connection and request concurrently, you should see some failures when the istio-proxy opens the circuit for further requests and connections.

### 1. Call the service with two concurrent connections (-c 2) and send 20 requests (-n 20):
```
kubectl -n bookinfo-istio exec "$FORTIO_POD" -c fortio -- /usr/bin/fortio load -c 2 -qps 0 -n 20 -loglevel Warning http://httpbin:8000/get
``` 

### It’s interesting to see that almost all requests made it through! The istio-proxy does allow for some leeway.
```
Code 200 : 17 (85.0 %)
Code 503 : 3 (15.0 %)
```


### 2. Bring the number of concurrent connections up to 3:
```
kubectl -n bookinfo-istio exec "$FORTIO_POD" -c fortio -- /usr/bin/fortio load -c 3 -qps 0 -n 30 -loglevel Warning http://httpbin:8000/get
```

### Now you start to see the expected circuit breaking behavior. Only 36.7% of the requests succeeded and the rest were trapped by circuit breaking:
```
Code 200 : 11 (36.7 %)
Code 503 : 19 (63.3 %)
```

### Query the istio-proxy stats to see more:
```
kubectl -n bookinfo-istion exec "$FORTIO_POD" -c istio-proxy -- pilot-agent request GET stats | grep httpbin | grep pending
```
```
cluster.outbound|8000||httpbin.default.svc.cluster.local.circuit_breakers.default.remaining_pending: 1
cluster.outbound|8000||httpbin.default.svc.cluster.local.circuit_breakers.default.rq_pending_open: 0
cluster.outbound|8000||httpbin.default.svc.cluster.local.circuit_breakers.high.rq_pending_open: 0
cluster.outbound|8000||httpbin.default.svc.cluster.local.upstream_rq_pending_active: 0
cluster.outbound|8000||httpbin.default.svc.cluster.local.upstream_rq_pending_failure_eject: 0
cluster.outbound|8000||httpbin.default.svc.cluster.local.upstream_rq_pending_overflow: 21
cluster.outbound|8000||httpbin.default.svc.cluster.local.upstream_rq_pending_total: 29
```

### You can see 21 for the upstream_rq_pending_overflow value which means 21 calls so far have been flagged for circuit breaking.



### Clean Up 
```
kubectl delete -f 03-httpbin.yaml -n bookinfo-istio
kubectl delete -f 04-Circuit_breaking_ds_rules.yaml -n bookinfo-istio
kubectl delete -f 05-Forty-Traffic_gen.yaml -n bookinfo-istio
```
