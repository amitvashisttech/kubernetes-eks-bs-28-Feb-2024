## Install Sample App of Your Choice from the SampleApp Dir. 

### 1. HelloWorld ( kubectl apply -f HelloWorld/ )  
### 2. Eks-WorkShop

# Create workshop namespace 
```
kubectl create namespace workshop
kubectl label namespace workshop istio-injection=enabled
```
# Install all the microservices in one go
```
cd Eks-WorkShop
helm install sample-eks-app . -n workshop 
```
