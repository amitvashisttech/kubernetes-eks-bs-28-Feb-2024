```
  652  curl  http://40.83.130.216/hello -H 'Host: hello.example.com'
  653  for ((i=1;i<=10;i++)); do curl  http://40.83.130.216/hello -H 'Host: hello.example.com'; done 
  654  ls
  655  kubectl delete -f 03-helloworld-AB-routing.yaml 
  656  kubectl  apply -f 04-helloworld-Canary-routing.yaml 
  657  for ((i=1;i<=10;i++)); do curl  http://40.83.130.216/hello -H 'Host: hello.example.com'; done 

```
