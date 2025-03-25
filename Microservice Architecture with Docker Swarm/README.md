# Shared Notes Microservices Application

A microservices-based web application that demonstrates Docker Swarm's service resilience through replicas. The application allows users to write and view shared notes across three different pages, each running as a separate service.

<p align="center">
  <img src="https://github.com/git-raghav/My-Docker-Dockyard/blob/edit/Microservice%20Architecture%20with%20Docker%20Swarm/assets/docker-to-swarm-1.png?raw=true" alt="Docker to Swarm" width="300" />
</p>


## Project Structure

```
project/
├── frontend/
│   ├── page1.html
│   ├── page2.html
│   ├── page3.html
│   ├── styles.css
│   ├── script.js
│   └── Dockerfile
├── backend/
│   ├── server.js         # Node.js API server
│   ├── package.json
│   └── Dockerfile
├── docker-compose.yml    # Docker Swarm configuration
└── README.md
```

## Architecture

### Frontend Services

-   Three separate web pages (page1, page2, page3)
-   Each page runs as an independent service with 2 replicas
-   Served by Nginx
-   Ports: 8081, 8082, 8083
-   Share the same frontend code but run independently

### Backend Service

-   Node.js Express server
-   Handles note storage and retrieval
-   Runs with 3 replicas for high availability
-   Port: 3000
-   Uses in-memory storage (for demonstration)

### Docker Swarm Features

-   Service resilience through replicas
-   Automatic load balancing
-   Service discovery
-   Overlay network for inter-service communication
-   Dynamic scaling capabilities

## How It Works

1. **Frontend-Backend Communication**

    - Frontend services communicate with the backend via REST API
    - Notes are saved and retrieved through HTTP requests
    - Frontend polls the backend every 2 seconds for updates

2. **Service Resilience**

    - Each frontend service has 2 replicas
    - Backend service has 3 replicas
    - If a replica fails, Docker Swarm automatically routes traffic to available replicas
    - Services remain available even if some replicas fail

3. **Data Flow**
    ```
    User Input → Frontend Service → Backend Service → All Frontend Services
    ```
    - User enters a note on any page
    - Frontend sends note to backend via POST request
    - Backend stores the note
    - All frontend services poll backend and display updated note

## Prerequisites

-   Docker
-   Docker Swarm enabled
-   Docker Compose

## Setup Instructions

1. Initialize Docker Swarm (if not already initialized):

```bash
docker swarm init
```
![Screenshot](/Microservice%20Architecture%20with%20Docker%20Swarm/assets/Screenshot%202025-03-25%20231817.png)

2. Build and deploy the services:

```bash
docker stack deploy -c docker-compose.yml shared-notes
```
![Screenshot](/Microservice%20Architecture%20with%20Docker%20Swarm/assets/Screenshot%202025-03-26%20000159.png)

3. Access the application:

-   Page 1: http://localhost:8081/page1.html
-   Page 2: http://localhost:8082/page2.html
-   Page 3: http://localhost:8083/page3.html

![Screenshot](/Microservice%20Architecture%20with%20Docker%20Swarm/assets/Screenshot%202025-03-26%20001218.png)
![Screenshot](/Microservice%20Architecture%20with%20Docker%20Swarm/assets/Screenshot%202025-03-26%20001235.png)

## Service Scaling

### View Current Service Status

```bash
# List all services and their replicas
docker service ls

# View detailed status of a specific service
docker service ps shared-notes_backend
```
![Screenshot](/Microservice%20Architecture%20with%20Docker%20Swarm/assets/Screenshot%202025-03-26%20000609.png)

### Scale Services Up/Down

1. **Using docker service scale**

```bash
# Scale backend to 4 replicas
docker service scale shared-notes_backend=4

# Scale frontend service to 3 replicas
docker service scale shared-notes_page1=3
```

2. **Using docker service update**

```bash
# Scale backend to 4 replicas
docker service update --replicas 4 shared-notes_backend

# Scale frontend service to 3 replicas
docker service update --replicas 3 shared-notes_page1
```
![Screenshot](/Microservice%20Architecture%20with%20Docker%20Swarm/assets/Screenshot%202025-03-26%20003607.png)

### Scaling Guidelines

-   Backend service can be scaled to handle increased API load
-   Frontend services can be scaled to handle more concurrent users
-   Docker Swarm automatically handles load balancing across replicas
-   Services remain available during scaling operations
-   You can scale up or down as needed based on demand

## Testing Service Resilience

1. View running services:

```bash
docker service ls
```
![Screenshot](/Microservice%20Architecture%20with%20Docker%20Swarm/assets/Screenshot%202025-03-26%20000609.png)

2. Test backend resilience:

```bash
# Stop one backend replica
docker service update --replicas 2 shared-notes_backend
# The application continues working with remaining replicas
```
![Screenshot](/Microservice%20Architecture%20with%20Docker%20Swarm/assets/Screenshot%202025-03-26%20002139.png)
![Screenshot](/Microservice%20Architecture%20with%20Docker%20Swarm/assets/Screenshot%202025-03-26%20002321.png)

3. Test frontend resilience:

```bash
# Stop one frontend replica
docker service update --replicas 1 shared-notes_page1
# The page remains accessible through the other replica
```
![Screenshot](/Microservice%20Architecture%20with%20Docker%20Swarm/assets/Screenshot%202025-03-26%20002525.png)
![Screenshot](/Microservice%20Architecture%20with%20Docker%20Swarm/assets/Screenshot%202025-03-26%20002634.png)

## API Endpoints

### Backend Service

-   `GET /api/note` - Retrieve current note
-   `POST /api/note` - Save new note

## Cleanup

To remove the application:

```bash
docker stack rm shared-notes
```
![Screenshot](/Microservice%20Architecture%20with%20Docker%20Swarm/assets/Screenshot%202025-03-26%20003934.png)

## Key Features

-   Microservices architecture
-   Service resilience through replicas
-   Real-time note sharing across pages
-   Automatic failover
-   Load balancing
-   Service discovery
-   Container orchestration with Docker Swarm
-   Dynamic service scaling
