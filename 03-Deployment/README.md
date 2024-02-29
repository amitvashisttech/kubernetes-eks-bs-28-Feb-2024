 ```
   35  kubectl apply -f helloworld.yaml 
   36  kubectl  get deploy,rs,pod
   37  kubectl get pods 
   38  kubectl  get svc 
   39  kubectl  get deploy
       kubectl expose deploy helloworld-deployment --type=NodePort 
   40  cat README.md 
   41  kubectl set image deployment helloworld-deployment k8s-demo=amitvashist7/k8s-tiny-web:2
   42  kubectl  get deploy 
   43  kubectl  get deploy,rs,pod
   44  kubectl set image deployment helloworld-deployment k8s-demo=amitvashist7/k8s-tiny-web:3
   45  kubectl set image deployment helloworld-deployment k8s-demo=amitvashist7/k8s-tiny-web:4
   46  cat helloworld.yaml 
   47  cat README.md 
   48  kubectl rollout history deploy helloworld-deployment
   49  kubectl rollout history deploy helloworld-deployment --revision=1
   50  kubectl rollout history deploy helloworld-deployment --revision=2
   51  kubectl rollout history deploy helloworld-deployment
   52  kubectl rollout undo deploy helloworld-deployment
   53  kubectl rollout history deploy helloworld-deployment
   54  kubectl rollout undo deploy helloworld-deployment
   55  kubectl rollout history deploy helloworld-deployment
   56  kubectl rollout undo deploy helloworld-deployment --to-revision=2
   57  kubectl rollout history deploy helloworld-deployment
   58  kubectl rollout undo deploy helloworld-deployment --to-revision=1
   59  kubectl rollout history deploy helloworld-deployment
   60  kubectl set image deployment helloworld-deployment k8s-demo=amitvashist7/k8s-tiny-web:4 --record 
   61  kubectl rollout history deploy helloworld-deployment
   62  kubectl set image deployment helloworld-deployment k8s-demo=amitvashist7/k8s-tiny-web:3 --record 
   63  kubectl set image deployment helloworld-deployment k8s-demo=amitvashist7/k8s-tiny-web:2 --record 
   64  kubectl set image deployment helloworld-deployment k8s-demo=amitvashist7/k8s-tiny-web --record 
   65  kubectl rollout history deploy helloworld-deployment
       kubectl edit deploy helloworld-deployment
       kubectl get deploy helloworld-deployment -o yaml > abc.yaml    
```

```
  347  kubectl run hello-k8s --image=nginx --port=80 --dry-run
  348  kubectl run hello-k8s --image=nginx --port=80 --dry-run -o yaml
  349  kubectl run hello-k8s --image=nginx --port=80 --dry-run -o yaml  > abc.yaml
  350  ls
  351  kubectl apply -f abc.yaml
```

```
   66  ls
   67  kubectl get deployment 
   68  kubectl get deploy helloworld-deployment
   69  kubectl describe deploy helloworld-deployment
   70  kubectl get deploy 
   71  vim helloworld.yaml 
   72  kubectl apply -f helloworld.yaml 
   73  kubectl scale --replicas=7 deploy helloworld-deployment
   74  kubectl  edit deploy helloworld-deployment
   75  kubectl  get deploy 
   76  kubectl set image deployment helloworld-deployment k8s-demo=amitvashist7/k8s-tiny-web:2 --record 
   77  kubectl delete -f helloworld.yaml 
   78  ls
   79  vim helloworld-v2.yaml 
   80  kubectl  apply -f helloworld-v2.yaml 
   81  kubectl set image deployment helloworld-deployment k8s-demo=amitvashist7/k8s-tiny-web:2 --record 
   82  kubectl  get deploy 
   83  kubectl set image deployment helloworld-2-deployment k8s-demo=amitvashist7/k8s-tiny-web:2 --record 
   84  cat helloworld-v2.yaml 
   85  kubectl  get deploy 
   86  kubectl  describe deploy helloworld-2-deployment 
   87  kubectl  delete -f helloworld-v2.yaml 
   88  vim helloworld-v3.yaml 
   89  kubectl apply -f helloworld-v3.yaml 
   90  kubectl set image deployment helloworld-3-deployment k8s-demo=amitvashist7/k8s-tiny-web:2 --record 
   91  kubectl delete -f helloworld-v3.yaml 
```


