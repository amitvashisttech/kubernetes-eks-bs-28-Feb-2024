* Install Helm:

  ```bash
  curl https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3 | bash
  ```

* Install Argo CD on the cluster using Helm as follows:

  ```bash
  helm repo add argo https://argoproj.github.io/argo-helm
  kubectl create namespace argocd
  helm install argocd -n argocd argo/argo-cd
  ```

* Get the administrator password (or just copy the command from the Helm output):

  ```bash
  kubectl -n argocd get secret argocd-initial-admin-secret -o jsonpath="{.data.password}" | base64 -d
  ```

* Copy the password that was brought.

* Create a port-forward to access the UI of the server by running:

  ```bash
  kubectl port-forward service/argocd-server -n argocd 8080:443 --address="0.0.0.0"
  ```

* Open the browser and navigate to 172.31.0.100:8080. Accept the security risk. Enter the username: admin and paste the password from the above output.

* If you are using your local machine, navigate to localhost and accept the security warning. Login again with the same password.

### Argo CD CLI Installation

* Navigate to https://github.com/argoproj/argo-cd/releases/latest to get the Argo CD CLI.

* Scroll down till the downloadable files.

* Copy the link to the Linux amd64 file.

* Install Argo CD CLI by running the following command:

  ```bash
  wget https://github.com/argoproj/argo-cd/releases/download/v2.6.7/argocd-linux-amd64
  sudo mv argocd /usr/local/bin/argocd
  chmod +x /usr/local/bin/argocd
  ```

* Login to Argo CD using the following command (username is `admin` and the password can be pasted from the previous output):

  ```bash
  argocd login localhost --insecure
  ```

* Verify that you are logged in by running:

  ```bash
  argocd repo list
  ```

* Change the password using the following command:

  ```bash
  argocd account update-password \
  --current-password # current password \
  --new-password # new password
  ```

  
