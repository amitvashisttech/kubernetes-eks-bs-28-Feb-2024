# JWT Token

## Create two sample namespaces & deploy http & sleep app respectivly 

```
kubectl create ns ns1
kubectl apply -f <(istioctl kube-inject -f http.yaml) -n ns1
kubectl apply -f <(istioctl kube-inject -f sleep.yaml) -n ns1
```

## Verify that sleep successfully communicates with httpbin using this command: 
```
kubectl exec "$(kubectl get pod -l app=sleep -n ns1 -o jsonpath={.items..metadata.name})" -c sleep -n ns1 -- curl http://httpbin.ns1:8000/ip -sS -o /dev/null -w "%{http_code}\n"

```

## Allow requests with valid JWT and list-typed claims:

### The following command creates the jwt-example request authentication policy for the httpbin workload in the ns1 namespace. This policy for httpbin workload accepts a JWT issued by testing@secure.istio.io: 
```
kubectl apply -f - <<EOF
apiVersion: security.istio.io/v1beta1
kind: RequestAuthentication
metadata:
  name: "jwt-example"
  namespace: ns1
spec:
  selector:
    matchLabels:
      app: httpbin
  jwtRules:
  - issuer: "testing@secure.istio.io"
    jwksUri: "https://raw.githubusercontent.com/istio/istio/release-1.21/security/tools/jwt/samples/jwks.json"
EOF

```

### Verify that a request with an invalid JWT is denied:
```
kubectl exec "$(kubectl get pod -l app=sleep -n ns1 -o jsonpath={.items..metadata.name})" -c sleep -n ns1 -- curl "http://httpbin.ns1:8000/headers" -sS -o /dev/null -H "Authorization: Bearer invalidToken" -w "%{http_code}\n"

```

### Verify that a request without a JWT is allowed because there is no authorization policy:
```
kubectl exec "$(kubectl get pod -l app=sleep -n ns1 -o jsonpath={.items..metadata.name})" -c sleep -n ns1 -- curl "http://httpbin.ns1:8000/headers" -sS -o /dev/null -w "%{http_code}\n"

```

## Now, creates the require-jwt authorization policy for the httpbin workload in the ns1 namespace:
```
kubectl apply -f - <<EOF
apiVersion: security.istio.io/v1beta1
kind: AuthorizationPolicy
metadata:
  name: require-jwt
  namespace: ns1
spec:
  selector:
    matchLabels:
      app: httpbin
  action: ALLOW
  rules:
  - from:
    - source:
       requestPrincipals: ["testing@secure.istio.io/testing@secure.istio.io"]
EOF

```

### Now, Get the JWT that sets the iss and sub keys to the same value, testing@secure.istio.io. This causes Istio to generate the attribute requestPrincipal with the value testing@secure.istio.io/testing@secure.istio.io:
```
TOKEN=$(curl https://raw.githubusercontent.com/istio/istio/release-1.21/security/tools/jwt/samples/demo.jwt -s) && echo "$TOKEN" | cut -d '.' -f2 - | base64 --decode -

```


### Verify that a request with a valid JWT is allowed:
```
kubectl exec "$(kubectl get pod -l app=sleep -n ns1 -o jsonpath={.items..metadata.name})" -c sleep -n ns1 -- curl "http://httpbin.ns1:8000/headers" -sS -o /dev/null -H "Authorization: Bearer $TOKEN" -w "%{http_code}\n"
```

### Verify that a request without a JWT is denied:
```
kubectl exec "$(kubectl get pod -l app=sleep -n ns1 -o jsonpath={.items..metadata.name})" -c sleep -n ns1 -- curl "http://httpbin.ns1:8000/headers" -sS -o /dev/null -w "%{http_code}\n"
```



### Now, updates the require-jwt authorization policy to also require the JWT to have a claim named groups containing the value group1:
```
kubectl apply -f - <<EOF
apiVersion: security.istio.io/v1beta1
kind: AuthorizationPolicy
metadata:
  name: require-jwt
  namespace: ns1
spec:
  selector:
    matchLabels:
      app: httpbin
  action: ALLOW
  rules:
  - from:
    - source:
       requestPrincipals: ["testing@secure.istio.io/testing@secure.istio.io"]
    when:
    - key: request.auth.claims[groups]
      values: ["group1"]
EOF
```

### Get the JWT that sets the groups claim to a list of strings: group1 and group2:
```
TOKEN_GROUP=$(curl https://raw.githubusercontent.com/istio/istio/release-1.21/security/tools/jwt/samples/groups-scope.jwt -s) && echo "$TOKEN_GROUP" | cut -d '.' -f2 - | base64 --decode -
```

### Verify that a request with the JWT that includes group1 in the groups claim is allowed:
```
kubectl exec "$(kubectl get pod -l app=sleep -n ns1 -o jsonpath={.items..metadata.name})" -c sleep -n ns1 -- curl "http://httpbin.ns1:8000/headers" -sS -o /dev/null -H "Authorization: Bearer $TOKEN_GROUP" -w "%{http_code}\n"
```

### Verify that a request with a JWT, which doesn’t have the groups claim is rejected:
```
kubectl exec "$(kubectl get pod -l app=sleep -n ns1 -o jsonpath={.items..metadata.name})" -c sleep -n ns1 -- curl "http://httpbin.ns1:8000/headers" -sS -o /dev/null -H "Authorization: Bearer $TOKEN" -w "%{http_code}\n"
```


## Clean up
```
 kubectl delete ns ns1
```

