 1758  mkdir.exe 14-StatefulSet
 1771  ./../../kubectl.exe apply -f 01-StatefulSet.yaml --dry-run
 1772  ./../../kubectl.exe apply -f 01-StatefulSet.yaml
 1773  ./../../kubectl.exe get statefulset
 1778  ./../../kubectl.exe get pods
 1779  ./../../kubectl.exe describe statefulset helloworld-statefull
 1781  ./../../kubectl.exe rollout status statefulset helloworld-statefull
 1782  ./../../kubectl.exe rollout history statefulset helloworld-statefull
 1783  ./../../kubectl.exe get pods
 1784  ./../../kubectl.exe scale --replicas=10 statefulset helloworld-statefull
 1794  ./../../kubectl.exe get pods
 1795  ./../../kubectl.exe scale --replicas=8 statefulset helloworld-statefull
 1796  ./../../kubectl.exe get pods
 1797  ./../../kubectl.exe scale --replicas=5 statefulset helloworld-statefull
 1798  ./../../kubectl.exe get pods
 1801  cat 01-StatefulSet.yaml
 1802  ./../../kubectl.exe set image statefulset helloworld-statefull k8s-demo=amitvashist7/k8s-tiny-web:2 --record
 1803  ./../../kubectl.exe rollout history statefulset helloworld-statefull
 1805  ./../../kubectl.exe get pods
 1806  ./../../kubectl.exe describe pod helloworld-statefull-4
 1807  ./../../kubectl.exe get pods
 1810  ./../../kubectl.exe rollout status  statefulset helloworld-statefull
 1811  ./../../kubectl.exe get pods
 1815  ./../../kubectl.exe get pods
 1816  ./../../kubectl.exe scale --replicas=3 statefulset helloworld-statefull 
 1817  ./../../kubectl.exe get pods
 1818  ./../../kubectl.exe get pods
 1819  ./../../kubectl.exe rollout undo  statefulset helloworld-statefull
 1820  ./../../kubectl.exe get pods
 1821  ./../../kubectl.exe describe pod helloworld-statefull-2
 1822  ./../../kubectl.exe describe pod helloworld-statefull-0
