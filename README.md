# GKE-Flask-HELM
A simple project to automate the build and deployment for a Flask Application in GKE.

## Mission Statement:
This project is composed of three parts:

- Backend Application
- Container Creation
- Helm Chart Templating

This guide will go over the process of creating the backend application which is a simple REST API with two routes /will which returns "Hello World" in JSON format and /ready route which returns "It works!" in JSON format. We will walk through the process of containerzing this application in a light weight and secure manner. And finaly, we'll cover templating the deployment phase of our application using Helm. Our templating will cover deploying TCP liveness and readiness probes on each routes to allow for durability and availability of our application.

## Prerequisites:
The following is a list of dependencies to follow along:

- Deploy a kubernetes cluster on GCP using GKE. (This can be done with the below mentioned commands)
- Navigate to Cloud Shell on GCP console and start a terminal. Run the following commands:

        >  gcloud config set project <project-id>
        >  gcloud config set compute/zone <compute-zone>
        >  gcloud container clusters create <cluster-name> --num-nodes=1
        >  gcloud container clusters get-credentials <cluster-name>

The above steps will configure your project, compute/zone, create a one-node cluster for this simple application and configure authentication credentials to interact with the cluster.

- Download Helm 3 from https://helm.sh/docs/intro/install/ by using wget. This will download the tar. Untar helm binary and place it in /usr/local/bin
- Cloud Shell comes with Docker, which we will use to build our docker image. 
- We will also make use of Google Container Registry to host our image and pull during deployment phase.

## Design:

### Backend Application:

Our backend application is a simple Flask application under the path app/app.py. The app listens on port 5000 for the routes /will and /ready and returns 'Hello World' and 'It works!' respectively. The responses are in JSON format using JSONIFY.

### Containerization:

In order to keep our docker image light-weight and secure we're using an apline image which on its own is 97.8MB, and with our application on top amounts to 108MB. This removes the unnecessary overhead of tools that are not relevant to our application or our needs and provides a hardening approach to our application. Our containerization approach further comes in handy when we deploy to GKE and are able to call our image during deployment phase and allows for future revisions to be rolled out at faster rate as opposed to a bare metal deployment of our application.

### Helm Chart:






![alt text](service.png)


![alt text](deployment.png)
