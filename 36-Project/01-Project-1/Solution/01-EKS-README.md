## Setup Eks Cluster: 

### Using AWS Management Console:

    #### 1. Sign in to the AWS Management Console: Go to the AWS Management Console and sign in to your AWS account.

    #### 2. Navigate to Amazon EKS: From the services menu, select "Amazon EKS" under the "Compute" section.

    #### 3. Create Cluster: Click on the "Create cluster" button.
    ```
    Cluster Configuration:
        Choose the "Standard" cluster configuration.
        Enter a name for your cluster.
        Choose the Kubernetes version.
        Configure the networking settings (VPC, subnets, etc.).
    ```
    ```
    Node Group Configuration:
        Configure the node group settings (instance types, number of instances, etc.).
    ```
    #### 4. Cluster Add-ons: Optionally, you can enable add-ons like Kubernetes dashboard, Amazon EBS CSI driver, etc.

    #### 5. Review and Create: Review your configurations and click on "Create".

    #### 6. Wait for Cluster Creation: It may take a few minutes for the cluster to be created. Once done, you can access your cluster from the Amazon EKS dashboard.


### Using AWS CLI:

    #### 1. Install and Configure AWS CLI: Make sure you have the AWS CLI installed and configured with appropriate credentials.

    #### 2. Create a Cluster Configuration File: Create a YAML file (cluster.yaml for example) with your cluster configuration
    ```
    apiVersion: eksctl.io/v1alpha5
    kind: ClusterConfig

    metadata:
      name: my-cluster
      region: us-west-2

    nodeGroups:
      - name: ng-1
        instanceType: m5.large
        desiredCapacity: 2
        ssh:
          allow: true
     ``` 
    #### 3. Create Cluster: Use the eksctl command-line tool to create the cluster:
    ```
    eksctl create cluster -f cluster.yaml
    ```

    #### 4. Wait for Cluster Creation: It may take a few minutes for the cluster to be created. Once done, you can access your cluster using kubectl.

