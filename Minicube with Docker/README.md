# Minikube with Docker (Kubernetes Demonstration)

<div align="center">
    <img src="/Minicube with Docker/assets/Kubernetes.png" alt="kubernetes Logo" style="width: 200px; height: auto;">
</div>

This project demonstrates a simple web application deployed on Kubernetes with autoscaling capabilities. The application is a Node.js web server that displays a welcome message.

## Features

-   Simple Node.js web application
-   Docker containerization
-   Kubernetes deployment
-   Load balancing service
-   Horizontal Pod Autoscaler (HPA)
-   Stress testing capabilities

## Prerequisites

-   Docker Desktop
-   Minikube (Install using: `choco install minikube`)
-   kubectl
-   Node.js and npm
-   hey (HTTP load generator)

## Project Structure

```
.
├── app.js              # Node.js web application
├── package.json        # Node.js dependencies
├── Dockerfile          # Docker image configuration
├── deployment.yaml     # Kubernetes deployment
├── service.yaml        # Kubernetes service
└── hpa.yaml           # Horizontal Pod Autoscaler configuration
```

## YAML File Explanations

### 1. deployment.yaml

This file defines how your application should be deployed in Kubernetes:

-   `replicas: 2`: Starts with 2 identical copies (pods) of your application
-   `selector`: Identifies which pods belong to this deployment using labels
-   `template`: Defines the pod template
    -   `containers`: Specifies the container configuration
        -   `image`: The Docker image to use
        -   `ports`: Exposes port 3000 from the container
        -   `resources`: Sets CPU and memory limits/requests

### 2. service.yaml

This file creates a network service that makes your application accessible:

-   `type: LoadBalancer`: Makes the service accessible from outside the cluster
-   `selector`: Routes traffic to pods with matching labels
-   `ports`: Maps external port 80 to internal port 3000

### 3. hpa.yaml

This file automatically scales your application based on CPU usage:

-   `minReplicas: 2`: Minimum number of pods
-   `maxReplicas: 10`: Maximum number of pods
-   `metrics`: Defines scaling based on CPU utilization (50%)

## Setup Instructions

1. **Install Minikube**

    ```bash
    choco install minikube
    ```

2. **Start Minikube**

    ```bash
    minikube start
    ```
    ![image](/Minicube with Docker/assets/Screenshot%202025-04-18%20195620.png)

3. **Enable Metrics Server**

    ```bash
    minikube addons enable metrics-server
    ```
    ![image](/Minicube with Docker/assets/Screenshot%202025-04-18%20205511.png)

4. **Build and Push Docker Image**

    ```bash
    docker build -t raghavcodes/raghav-web-app:latest .
    docker push raghavcodes/raghav-web-app:latest
    ```
    ![image](/Minicube with Docker/assets/Screenshot%202025-04-18%20200035.png)
    ![image](/Minicube with Docker/assets/Screenshot%202025-04-18%20200230.png)
    ![image](/Minicube with Docker/assets/Screenshot%202025-04-18%20200401.png)

5. **Deploy to Kubernetes**
    ```bash
    kubectl apply -f deployment.yaml
    kubectl apply -f service.yaml
    kubectl apply -f hpa.yaml
    ```
    ![image](/Minicube with Docker/assets/Screenshot%202025-04-18%20200754.png)

## Testing and Monitoring

For proper testing and monitoring, you'll need to run multiple commands in separate terminals simultaneously:

### Terminal 1: Access the Application

```bash
minikube service raghav-web-app-service --url
```

![image](/Minicube with Docker/assets/Screenshot%202025-04-18%20201431.png)
![image](/Minicube with Docker/assets/Screenshot%202025-04-18%20201507.png)

Keep this terminal open as it maintains the connection to your application.

### Terminal 2: Run Stress Test

```bash
hey -z 5m -c 50 http://127.0.0.1:51200
```

![image](/Minicube with Docker/assets/Screenshot%202025-04-18%20210516.png)

### Terminal 3: Monitor HPA

```bash
kubectl get hpa -w
```

![image](/Minicube with Docker/assets/Screenshot%202025-04-18%20210851.png)

What to observe:

-   CPU utilization percentage
-   Current number of replicas
-   Target number of replicas

### Terminal 4: Monitor Pods

```bash
kubectl get pods -w
```

![image](/Minicube with Docker/assets/Screenshot%202025-04-18%20210929.png)

What to observe:

-   Number of pods increasing/decreasing
-   Pod status changes
-   Pod creation and termination

### Terminal 5: Monitor Service

```bash
kubectl get service -w
```

What to observe:

-   Service status
-   External IP assignment
-   Port mappings

## Expected Observations During Stress Testing

1. **Initial State**

    - 2 pods running (minReplicas)
    - CPU utilization below 50%

2. **During Stress Test**

    - CPU utilization increasing
    - HPA detecting increased load
    - New pods being created
    - Number of pods increasing up to maxReplicas (10)

3. **After Stress Test**
    - CPU utilization decreasing
    - HPA scaling down pods
    - Number of pods returning to minReplicas (2)

## Cleanup

To remove all resources:

```bash
kubectl delete -f deployment.yaml
kubectl delete -f service.yaml
kubectl delete -f hpa.yaml
minikube stop
```

![image](/Minicube with Docker/assets/Screenshot%202025-04-18%20211806.png)
![image](/Minicube with Docker/assets/Screenshot%202025-04-18%20211941.png)

## Troubleshooting

1. **Metrics Server Not Working**

    ```bash
    minikube addons enable metrics-server
    kubectl top pods
    ```

2. **Service Not Accessible**

    ```bash
    kubectl get services
    minikube service list
    ```

3. **Pods Not Starting**
    ```bash
    kubectl describe pod <pod-name>
    kubectl get events
    ```

## Author

Raghav Agarwal
