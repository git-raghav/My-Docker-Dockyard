# Microservices Orchestration with Minikube & Kubernetes

This project demonstrates a basic microservices architecture using Minikube and Kubernetes. It includes an API Gateway and a Backend Service, showcasing how to containerize applications and deploy them in a Kubernetes cluster.

## Prerequisites

Before you begin, ensure you have the following installed:
- [Minikube](https://minikube.sigs.k8s.io/docs/start/) - For running a local Kubernetes cluster
- [kubectl](https://kubernetes.io/docs/tasks/tools/install-kubectl/) - For interacting with the Kubernetes cluster
- [Docker](https://docs.docker.com/get-docker/) - For building container images

## Project Structure

```
.
├── README.md
├── backend/
│   ├── Dockerfile
│   ├── backend.py
│   └── requirements.txt
├── api-gateway/
│   ├── Dockerfile
│   ├── api_gateway.py
│   └── requirements.txt
└── kubernetes/
    ├── backend-service.yaml
    └── api-gateway.yaml
```

## Step-by-Step Guide (Use all the commands in bash terminal)

### 1. Start Minikube

First, start your Minikube cluster:

```bash
minikube start
```
![Screenshot](/Microservice%20with%20Minicube%20and%20Kubectl/images/Screenshot%202025-03-21%20014343.png)

### 2. Set Up Docker Environment

Configure Docker to use Minikube's Docker daemon:

```bash
eval $(minikube -p minikube docker-env)
```

### 3. Build and Deploy Services

#### 3.1 Backend Service

1. Navigate to the backend directory:
```bash
cd backend
```

2. Build the Docker image:
```bash
docker build -t backend-service .
```

3. Deploy to Kubernetes:
```bash
kubectl apply -f ../kubernetes/backend-service.yaml
```
![Screenshot](/Microservice%20with%20Minicube%20and%20Kubectl/images/Screenshot%202025-03-21%20014834.png)

#### 3.2 API Gateway

1. Navigate to the api-gateway directory:
```bash
cd ../api-gateway
```

2. Build the Docker image:
```bash
docker build -t api-gateway .
```

3. Deploy to Kubernetes:
```bash
kubectl apply -f ../kubernetes/api-gateway.yaml
```
![Screenshot](/Microservice%20with%20Minicube%20and%20Kubectl/images/Screenshot%202025-03-21%20015036.png)

### 4. Verify Deployment

Check the status of your deployments:

```bash
kubectl get deployments
kubectl get services
```
![Screenshot](/Microservice%20with%20Minicube%20and%20Kubectl/images/Screenshot%202025-03-21%20020054.png)

### 5. Access the Application

To access the API Gateway service:

```bash
minikube service api-gateway
```
This will open your browser to the API Gateway endpoint, which will display a message from the backend service.

![Screenshot](/Microservice%20with%20Minicube%20and%20Kubectl/images/Screenshot%202025-03-21%20015902.png)
![Screenshot](/Microservice%20with%20Minicube%20and%20Kubectl/images/Screenshot%202025-03-21%20020139.png)
### 6. Monitoring and Debugging

Useful commands for monitoring and debugging:

```bash
# View logs of the API Gateway
kubectl logs deployment/api-gateway

# View logs of the Backend Service
kubectl logs deployment/backend-service

# Get detailed information about pods
kubectl describe pods
```

### 7. Clean Up

When you're done, clean up the resources:

```bash
# Delete deployments and services
kubectl delete -f kubernetes/api-gateway.yaml
kubectl delete -f kubernetes/backend-service.yaml

# Stop Minikube
minikube stop
```
![Screenshot](/Microservice%20with%20Minicube%20and%20Kubectl/images/Screenshot%202025-03-21%20020704.png)

## Architecture Overview

### Components

1. **API Gateway**
   - Acts as the entry point for all client requests
   - Routes requests to appropriate backend services
   - Port: 8080

2. **Backend Service**
   - Handles business logic
   - Returns simple responses
   - Port: 5000

### Communication Flow

1. Client → API Gateway (8080)
2. API Gateway → Backend Service (5000)
3. Backend Service → API Gateway
4. API Gateway → Client

## Troubleshooting

Common issues and solutions:

1. **Images not found**
   - Ensure you're using Minikube's Docker daemon
   - Verify image names in Kubernetes manifests

2. **Services not accessible**
   - Check if pods are running: `kubectl get pods`
   - Verify service types and ports
   - Check logs for errors

3. **Minikube issues**
   - Restart Minikube: `minikube stop && minikube start`
   - Reset cluster: `minikube delete && minikube start`

## Additional Resources

- [Minikube Documentation](https://minikube.sigs.k8s.io/docs/)
- [Kubernetes Documentation](https://kubernetes.io/docs/)
- [Docker Documentation](https://docs.docker.com/)
