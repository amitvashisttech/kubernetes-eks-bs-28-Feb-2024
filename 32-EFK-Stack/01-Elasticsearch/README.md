## Deploy Elasticsearch Statefulset
#### Elasticsearch is deployed as a Statefulset and the multiple replicas connect with each other using a headless service. The headless svc helps in the DNS domain of the pods.

```
kubectl apply -f es-svc.yaml
```

#### Before we begin creating the statefulset for elastic search, let’s recall that a statefulset requires a storage class defined beforehand using which it can create volumes whenever required.

#### Note: In a production environment, we need to use 400-500Gbs of volume for elastic search, here we are deploying with 3Gb PVC’s for demonstrations.
#### The statefulset creates the PVC with the default available storage class. If you have a custom storage class for PVC, you can add it in the volumeClaimTemplates by uncommenting the storageClassName parameter.

#### Let's deploy the statefulset
```
kubectl create -f es-sts.yaml
```

### Verify Elasticsearch Deployment

#### After the Elastisearch pods come into the running state, let us try and verify the Elasticsearch statefulset. The easiest method to do this is to check the status of the cluster. In order to check the status, port-forward the Elasticsearch pod’s 9200 port.
```
kubectl port-forward es-cluster-0 9200:9200
```


#### To check the health of the Elasticsearch cluster, run the following command in the terminal.
```
curl http://localhost:9200/_cluster/health/?pretty
```

#### The output will display the status of the Elasticsearch cluster. If all the steps were followed correctly, the status should come up as ‘green’.
```
{
  "cluster_name" : "k8s-logs",
  "status" : "green",
  "timed_out" : false,
  "number_of_nodes" : 3,
  "number_of_data_nodes" : 3,
  "active_primary_shards" : 8,
  "active_shards" : 16,
  "relocating_shards" : 0,
  "initializing_shards" : 0,
  "unassigned_shards" : 0,
  "delayed_unassigned_shards" : 0,
  "number_of_pending_tasks" : 0,
  "number_of_in_flight_fetch" : 0,
  "task_max_waiting_in_queue_millis" : 0,
  "active_shards_percent_as_number" : 100.0
}
```

### Elasticsearch Headless Service

#### As you know, headless svc does not work as a load balancer and is used to address a group of pods together. There is another use case for headless services.

```
kubectl run -it hello-network --image=busybox:1.28 -- sh
```
```
/ # nslookup es-cluster-0.elasticsearch.efk.svc.cluster.local
Server:    172.20.0.10
Address 1: 172.20.0.10 kube-dns.kube-system.svc.cluster.local

Name:      es-cluster-0.elasticsearch.efk.svc.cluster.local
Address 1: 10.0.9.221 es-cluster-0.elasticsearch.efk.svc.cluster.local
```
```
/ # nslookup es-cluster-1.elasticsearch.efk.svc.cluster.local
Server:    172.20.0.10
Address 1: 172.20.0.10 kube-dns.kube-system.svc.cluster.local

Name:      es-cluster-1.elasticsearch.efk.svc.cluster.local
Address 1: 10.0.8.113 es-cluster-1.elasticsearch.efk.svc.cluster.local
```
```
/ # nslookup es-cluster-2.elasticsearch.efk.svc.cluster.local
Server:    172.20.0.10
Address 1: 172.20.0.10 kube-dns.kube-system.svc.cluster.local

Name:      es-cluster-2.elasticsearch.efk.svc.cluster.local
Address 1: 10.0.10.108 es-cluster-2.elasticsearch.efk.svc.cluster.local
```

#### The above concept is used very commonly in Kubernetes, so should be understood clearly. In fact, the statefulset env vars – “discovery.seed_hosts” and “cluster.initial_master_nodes” are using this concept.
