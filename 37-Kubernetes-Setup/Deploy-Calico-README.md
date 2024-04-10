# Deploy Calico 

## Configure Docker Image Pull Secrets
```
docker login 
```
```
kubectl create secret generic regcred --from-file=.dockerconfigjson=/root/.docker/config.json --type=kubernetes.io/dockerconfigjson -n kube-system
```

OR 

```
kubectl create secret docker-registry NAME --docker-username=user --docker-password=password --docker-email=email -n kube-system
```

## Deploy Calico
```
kubectl apply -f calico.yaml
```

## Now wait for all the calico pods to come up. 
```
kubectl get pods -n kube-system -o wide 
```

## Let's delete old proxy, coredns, calico-kube-cantroller & other pods.

## Now check all the pod IP Address should be fall in 192.168.0.0/16 range. 
```
root@master:~ # kubectl  get pods -n kube-system -o wide
NAME                                       READY   STATUS    RESTARTS      AGE   IP                NODE      NOMINATED NODE   READINESS GATES
calico-kube-controllers-6c99c8747f-nn76w   1/1     Running   0             13m   192.168.219.65    master    <none>           <none>
calico-node-9785n                          1/1     Running   0             17m   172.31.0.100      master    <none>           <none>
calico-node-l9wdd                          1/1     Running   0             17m   172.31.0.101      worker1   <none>           <none>
calico-node-msx7l                          1/1     Running   0             17m   172.31.0.102      worker2   <none>           <none>
coredns-5d78c9869d-9r4hd                   1/1     Running   0             13m   192.168.235.129   worker1   <none>           <none>
coredns-5d78c9869d-rxtwt                   1/1     Running   0             13m   192.168.189.65    worker2   <none>           <none>
etcd-master                                1/1     Running   0             27h   172.31.0.100      master    <none>           <none>
kube-apiserver-master                      1/1     Running   0             27h   172.31.0.100      master    <none>           <none>
kube-controller-manager-master             1/1     Running   1 (23h ago)   27h   172.31.0.100      master    <none>           <none>
kube-proxy-9n6gf                           1/1     Running   0             13m   172.31.0.100      master    <none>           <none>
kube-proxy-bc7v8                           1/1     Running   0             13m   172.31.0.101      worker1   <none>           <none>
kube-proxy-x4lxk                           1/1     Running   0             13m   172.31.0.102      worker2   <none>           <none>
kube-scheduler-master                      1/1     Running   1 (23h ago)   27h   172.31.0.100      master    <none>           <none>
```
```
root@master:~# kubectl  get pods -o wide
NAME                                        READY   STATUS    RESTARTS   AGE   IP                NODE      NOMINATED NODE   READINESS GATES
python-webapp-deployment-5799f678dd-42mm9   1/1     Running   0          11m   192.168.189.66    worker2   <none>           <none>
python-webapp-deployment-5799f678dd-5bwds   1/1     Running   0          11m   192.168.235.130   worker1   <none>           <none>
python-webapp-deployment-5799f678dd-plwtz   1/1     Running   0          11m   192.168.235.131   worker1   <none>           <none>
root@master:~#
```
