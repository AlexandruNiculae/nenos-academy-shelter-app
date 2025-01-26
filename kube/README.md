
This tutorial focuses on `minikube`!

# Minikube
Minikube is a containerized kubernetes environment that allows developers to test their apps in kubernetes-like environments.

## Basic commands
`minikube start` - pulls and starts the minikube container  

`minikube stop` - stops the current active minikube container  

`minikube delete` - removes container and image along with other minikube related files (use this instead of deleting things manually)  

`minikube dashboard` - will open a browser window where you can visualize things deployed in minikube  
*Requires an active minikube session  
*Blocks the console tab in which executed

`minikube image load image:tag` - transfer a docker image into minikube's docker image repository
*Required when running deployments using custom images

## Deploying things in minikube
Once minikube is running, in order to deploy things into minikube you will need the `kubectl` command.
If minikube was installed correctly, the command `kubectl version` should display the current version of the tool.

In order to deploy something in minikube you have to execute the following command:
`kubectl apply -f component.yaml`

This will parse the given yaml file and create the component or components from that file.

You can visualize that the component deployed correctly by looking into minikube dashboard and seeing the status of that component as green. Though components can deploy successfuly this doesn't mean that they are also working. Please check the logs (especially for pods) to ensure they are working properly.

# Deploying your app
The following will guide you with deploying all the required components for your app.

## Deploying the database
This will guide you on how to deploy either of the databases in minikube.

### Service
The `service.yaml` file describes a `Service` component. Services allow for communication inside the cluster between the components of the namespace. They dictate the how the information goes in and out of the deployment.

### Persistent Volume Claim
The `pvc.yaml` file describes a `Persistent Volume Clain` component. Persistent volumes are similar to hard drives, as in they allow for the storage of data and for it to persist across deploments.  
When a pod dies, the entire data that was stored on that pod is deleted. In order to prevent such things from happening, a volume is created and linked to the deployment through such a claim.

### Deployment
The `deployment.yaml` describes a `Deployment`. This component contains all the required info for a container to run. Some of these are:
- the container image
- number of active pods
- required resources
- environment variables
- volumes

This file is the backbone of your component and responsible for the pods that will run your application.

Be sure to check that the image you are using is available in minikube. If not you will have to transfer it using `minikube image load`.

### How to deploy the database
In order to deploy the components you will need to execute the following:  
`kubectl apply -f pvc.yaml`  
`kubectl apply -f service.yaml`  
`kubectl apply -f deployment.yaml`

The order of these is not important. Once you run all the commands you can check the status of your components in the minikube dashboard. **Please adapt the file names according to your files.**

## Deploying your app
This part will guide you on how to deploy your application in minikube.

### Deployment
The `deployment.yaml` file functions just as before but since our container needs to run 2 apps, there are 2 deployement files. One for the `API` and one for the `Web` component.

### Service
Similar to the `deployment.yaml`, you will have 2 files for the service.

### Ingress
The `ingress.yaml` links outside connections to your service. This means that in order to access the web application from outside the minikube cluster we will need an ingress. 

> At the moment, this doesn't work so do `kubectl port-forward service/shelter-web 8050:8050` in order to access the web interface.

### How to deploy the API and Web
In order to make sure that our application deploys correctly we will do the following. First, we will deploy the api by executing the commands:

`kubectl apply -f service-api.yaml`  
`kubectl apply -f deployment-api.yaml`

After this, we will check in the minikube dashboard that the API pod is running normally. You can view the logs of the pod to make sure that start-up and database initialization worked.

If all worked fine, then we deploy the web application:

`kubectl apply -f service-web.yaml`  
`kubectl apply -f deployment-web.yaml`
`kubectl apply -f ingress-web.yaml`

After that, opening the ingress link in the browser should yield the web page.