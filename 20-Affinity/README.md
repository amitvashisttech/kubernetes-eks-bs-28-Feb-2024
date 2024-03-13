 119  mkdir 20-Affinity
  120  ls
  121  cd 20-Affinity/
  122  ls
  123  vim 01-helloworld.yaml
  124  ls
  125  kubectl apply -f 01-helloworld.yaml
  126  kubectl get nodes
  127  kubectl label node ip-10-0-11-175.ap-south-1.compute.internal env=prod
  128  kubectl label node ip-10-0-14-95.ap-south-1.compute.internal env=dev
  129  kubectl delete -f 01-helloworld.yaml
  130  kubectl apply -f 01-helloworld.yaml
  131  kubectl delete -f 01-helloworld.yaml
  132  ls
  133  cp -rf 01-helloworld.yaml 02-helloworld-multi.yaml
  134  vim 02-helloworld-multi.yaml
  135  kubectl apply -f 02-helloworld-multi.yaml
  136  ping -c2 google.com
  137  kubectl apply -f 02-helloworld-multi.yaml
  138  kubectl delete -f 02-helloworld-multi.yaml
  139  ks
  140  ls
  141  cp -rf 02-helloworld-multi.yaml 02-helloworld-dev.yaml
  142  ks
  143  ls
  144  mv 02-helloworld-dev.yaml 03-helloworld-dev.yaml
  145  ls
  146  vim 02-helloworld-multi.yaml
  147  vim 03-helloworld-dev.yaml
  148  ls
  149  vim 03-helloworld-dev.yaml
  150  kubectl apply -f 03-helloworld-dev.yaml
  151*
  152  kubectl label node ip-10-0-15-218.ap-south-1.compute.internal env=dev
  153  kubectl label node ip-10-0-11-175.ap-south-1.compute.internal env-
  154  kubectl label node ip-10-0-11-175.ap-south-1.compute.internal env=dev
  155  kubectl delete -f 03-helloworld-dev.yaml
  156  kubectl apply -f 03-helloworld-dev.yaml
  157  kubectl delete -f 03-helloworld-dev.yaml
  158  vim 04-hello-devops-preff.yaml
  159  ls
  160  kubectl apply -f 04-hello-devops-preff.yaml
  161  kubectl delete -f 04-hello-devops-preff.yaml
  162  kubectl get nodes
  163  kubectl label node ip-10-0-11-217.ap-south-1.compute.internal env=dev
  164  kubectl get nodes
  165  kubectl apply -f 04-hello-devops-preff.yaml
  166  kubectl delete -f 04-hello-devops-preff.yaml
  167  kubectl label node ip-10-0-11-217.ap-south-1.compute.internal team=devops
  168  kubectl apply -f 04-hello-devops-preff.yaml
  169  kubectl delete -f 04-hello-devops-preff.yaml
  170  kubectl apply -f 04-hello-devops-preff.yaml
  171  ls
  172  kubectl delete -f 04-hello-devops-preff.yaml
