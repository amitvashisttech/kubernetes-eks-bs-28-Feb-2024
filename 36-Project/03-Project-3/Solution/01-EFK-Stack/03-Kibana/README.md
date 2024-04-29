## Deploy Kibana Deployment & Service
#### Kibana can be created as a simple Kubernetes deployment. If you check the following Kibana deployment manifest file, we have an env var ELASTICSEARCH_URL defined to configure the Elasticsearch cluster endpoint. Kibana uses the endpoint URL to connect to elasticsearch.


#### Let's deploy kibana deployment
```
kubectl create -f kibana-deployment.yaml
```



#### Let's deploy kibana Service
```
kubectl create -f kibana-svc.yaml
```

## Verify Kibana Deployment

#### After the pods come into the running state, let us try and verify Kibana deployment. The easiest method to do this is through the UI access of the cluster.

#### To check the status, port-forward the Kibana pod’s 5601 port. If you have created the nodePort service, you can also use that.
```
kubectl port-forward <kibana-pod-name> 5601:5601
```

#### Access the UI through the web browser or make a request using curl
```
curl http://localhost:5601/app/kibana
```
