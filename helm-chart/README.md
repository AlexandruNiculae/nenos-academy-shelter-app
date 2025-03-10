# Helm

## Basic Commands
Helm is a package manager for Kubernetes that simplifies application deployment. Here are some essential commands:

- Install Helm: https://helm.sh/docs/intro/install/

- Create a new chart:
  ```sh
  helm create mychart
  ```
- Install a chart:
  ```sh
  helm install myrelease ./mychart
  ```
- Upgrade a release:
  ```sh
  helm upgrade myrelease ./mychart
  ```
- Uninstall a release:
  ```sh
  helm uninstall myrelease
  ```
- List installed releases:
  ```sh
  helm list
  ```

## Generating a Chart
To create a Helm chart, run:
```sh
helm create mychart
```
This generates a directory structure with necessary files such as `Chart.yaml`, `values.yaml`, and Kubernetes manifests under `templates/`.

## What Are Charts?
Helm charts are packaged Kubernetes applications. Each chart contains:

- `Chart.yaml`: Metadata about the chart.
- `values.yaml`: Default configuration values.
- `templates/`: Kubernetes YAML templates for resources like Deployments and Services.

## Modifying a Chart
To customize a Helm chart:

1. Edit `values.yaml` to update configurations.
2. Modify templates in `templates/` to change Kubernetes resources.
3. Install or upgrade your deployment:
   ```sh
   helm upgrade --install myrelease ./mychart -f custom-values.yaml
   ```

### Adding new templates

To add a new component, create a new file inside the templates/ folder. For example, if you want to add a new deployment, create templates/new-deployment.yaml with content like:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: {{ .Release.Name }}-new
spec:
  replicas: 1
  selector:
    matchLabels:
      app: {{ .Release.Name }}-new
  template:
    metadata:
      labels:
        app: {{ .Release.Name }}-new
    spec:
      containers:
        - name: new-container
          image: my-new-image:latest
```

This will deploy a new application component when you apply your chart.

### Altering an existing template

To modify an existing deployment.yaml, you can add environment variables or commands. Example:

Modify templates/deployment.yaml to include:
```yaml
spec:
  containers:
    - name: my-container
      image: my-image:latest
      command: ["/bin/sh", "-c", "echo Hello World && sleep 3600"]
      env:
        - name: ENV_VAR_1
          value: "some-value"
```
This ensures that the container prints "Hello World" before sleeping and uses the new environment variable.

### Deleting components

If certain components are not needed, you can safely delete their corresponding YAML files in `templates/`.

- Service Account: The serviceaccount.yaml file was removed as it was unnecessary.

- Test Connection YAML: This was also deleted because the test was no longer needed.

Removing these files ensures that Helm does not try to create these resources when deploying the chart.


## Notes
While this guide uses a **single chart** for all components (databases, API, web app), in a real-world scenario, **subcharts** should be used to modularize the deployment. Subcharts help in:
- Reusing common components like databases.
- Managing configurations separately for each service.
- Making deployments more scalable and maintainable.

For more details, check out:
- [Helm Official Docs](https://helm.sh/docs/)
- [Creating Helm Subcharts](https://helm.sh/docs/chart_template_guide/subcharts_and_globals/)


## Deploying our apps
In order to release our app using helm we run the following command in the folder of our helm chart:  
`helm install sheter-app .\shelter-app\ --namespace shelter-app --create-namespace`  

If everything is correct, the output should be:
```
NAME: sheter-app
LAST DEPLOYED: Mon Mar 10 13:55:45 2025
NAMESPACE: shelter-app
STATUS: deployed
REVISION: 1
TEST SUITE: None
```
Once deployed, we check inside the minikube dashboard to ensure that all of our components are running. Further we port-forward our web service and open `http://localhost:8050` in our browser. You can port forward using the command `kubectl port-forward service/shelter-app-web 8050:8050 -n shelter-app`.