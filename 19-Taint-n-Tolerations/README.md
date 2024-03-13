 14  mkdir 19-Taint-n-Tolerations
   15  ls
   16  kubectl get nodes
   17  ls
   18  cd 19-Taint-n-Tolerations/
   19  ls
   20  vim 01-Helloworld-deploy.yaml
   21  ls
   22  kubectl get nodes
   23  ls
   24  kubectl apply -f 01-Helloworld-deploy.yaml
   25  kubectl get nodes
   26  kubectl get pods
   27  kubectl get pods -o wide
   28  kubectl describe pod helloworld-deployment-95f9c9df-lq76g
   29  kubectl get pods -o wide
   30  kubectl get pods -A
   31  kubectl get pods -o wide
   32  kubectl get nodes
   33  kubectl delete -f 01-Helloworld-deploy.yaml
   34  kubectl get nodes
   35  kubectl apply -f 01-Helloworld-deploy.yaml
   36  kubectl scale --replicas=5 apply -f 01-Helloworld-deploy.yaml
   37  kubectl scale --replicas 5 apply -f 01-Helloworld-deploy.yaml
   38  ls
   39  kubectl scale --replicas 5  -f 01-Helloworld-deploy.yaml
   40  kubectl scale --replicas 0  -f 01-Helloworld-deploy.yaml
   41  kubectl scale --replicas 1  -f 01-Helloworld-deploy.yaml
   42  kubectl scale --replicas 5  -f 01-Helloworld-deploy.yaml
   43  kubectl scale --replicas 10  -f 01-Helloworld-deploy.yaml
   44  kubectl delete -f 01-Helloworld-deploy.yaml
   45  ls
   46  vim 02-hello-deploy-with-toleration.yaml
   47  ls
   48  kubectl apply -f 02
   49  kubectl apply -f 02-hello-deploy-with-toleration.yaml
   50  kubectl get nodes
   51  kubectl describe node ip-10-0-11-175.ap-south-1.compute.internal | grep -i taint
   52  vim 02-hello-deploy-with-toleration.yaml
   53  kubectl scale --replicas 5  -f 02-hello-deploy-with-toleration.yaml
   54  kubectl delete -f 02-hello-deploy-with-toleration.yaml
   55  kubectl get nodes
   56  kubectl taint node ip-10-0-15-218.ap-south-1.compute.internal example=AmitVashist:NoSchedule
   57  kubectl describe nodes | grep -i taint
   58  ls
   59  kubectl apply -f 01-Helloworld-deploy.yaml
   60  kubectl apply -f 02-hello-deploy-with-toleration.yaml
   61  vim 03-hello-deploy-with-multi-toleration.yaml
   62  ls
   63  kubectl apply -f 03-hello-deploy-with-multi-toleration.yaml
   64  kubectl replicas 5  -f 03-hello-deploy-with-multi-toleration.yaml
   65  kubectl scale --replicas 5  -f 03-hello-deploy-with-multi-toleration.yaml
   66  kubectl get nodes
   67  kubectl taint node ip-10-0-11-154.ap-south-1.compute.internal example2=example2-key:NoSchedule
   68  kubectl taint node ip-10-0-11-154.ap-south-1.compute.internal example2-
   69  kubectl taint node ip-10-0-11-154.ap-south-1.compute.internal example2=example2-key:NoExecute
   70  kubectl delete -f 01-Helloworld-deploy.yaml
   71  kubectl get nodes
   72  cd ..
   73  ls
   74  kubectl delete -f 19-Taint-n-Tolerations/
   75  ls
   76  cd 18-Node-Labels/
   77  cd ..
   78  l
   79  ls
   80  cd 19-Taint-n-Tolerations/
   81  ls
   82  vim 04-hello-deploy-with-multi-toleration.yaml
   83  kubectl applu -f 04-hello-deploy-with-multi-toleration.yaml
   84  kubectl apply -f 04-hello-deploy-with-multi-toleration.yaml
   85  kubectl delete -f  04-hello-deploy-with-multi-toleration.yaml
   86  kubectl describe nodes | grep -i taint
   87  kubectl get nodes
   88  kubectl taint node ip-10-0-11-154.ap-south-1.compute.internal example1=example1-key:NoExecute
   89  kubectl describe nodes ip-10-0-11-154.ap-south-1.compute.internal | grep -A5 taint
   90  kubectl describe node ip-10-0-11-154.ap-south-1.compute.internal | grep -A5 taint
   91  kubectl describe node ip-10-0-11-154.ap-south-1.compute.internal
   92  kubectl describe node ip-10-0-11-154.ap-south-1.compute.internal | grep -i taint
   93  kubectl describe node ip-10-0-11-154.ap-south-1.compute.internal | grep -iA5 taint
   94  kubectl taint node ip-10-0-11-154.ap-south-1.compute.internal example1-
   95  kubectl get nodes
   96  ls
   97  vim 05-hello-daemonset
   98  vim 05-hello-daemonset.yaml
   99  ls
  100  kubectl apply -f 05-hello-daemonset.yaml
  101  kubectl get nodes
  102  kubectl get pods
  103  ls
  104  vim 06-hello-daemonset-with-toleration.yaml
  105  ls
  106  kubectl apply -f 06-hello-daemonset-with-toleration.yaml
  107  kubectl delete -f 06-hello-daemonset-with-toleration.yaml
  108  kubectl delete -f 05-hello-daemonset.yaml
