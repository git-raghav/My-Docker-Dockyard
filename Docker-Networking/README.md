# 🚀 Docker Networking Experiment - Custom & Default Networks

## 📌 Objective

The goal of this experiment is to understand Docker networking by creating three containers:

1. **Two containers connected via a custom network.**
2. **One container connected to Docker's default bridge network.**

We will test network connectivity between these containers to understand the differences between Docker's custom networks and the default bridge network.

---

## 🌐 Introduction to Docker Networking

Docker provides various networking options for containerized applications:

-   **Bridge Network (Default)** - Allows containers to communicate using internal IPs unless restricted.
-   **Custom Bridge Network** - Provides better control with name-based resolution.
-   **Host Network** - Directly attaches containers to the host’s network stack.
-   **Overlay Network** - Enables communication across multiple hosts in Docker Swarm.
-   **Macvlan Network** - Assigns a MAC address to each container, making them appear as separate devices.
-   **None Network** - Completely disables networking.

For this demonstration, we focus on the **custom bridge network** for improved control and security.

---

## 🔧 Step 1: Creating a Custom Docker Network

A custom bridge network ensures that containers can communicate with each other while being isolated from others.

```bash
docker network create --driver bridge --subnet 192.168.1.0/24 raghav_network
```

### 🔍 Explanation:

-   `--driver bridge` → Uses Docker's bridge network mode.
-   `--subnet 192.168.1.0/24` → Defines the custom network’s IP range.

Verify the creation of the network:

```bash
docker network ls
```

---

## 🚀 Step 2: Running Three Containers

We will create three containers using different networks.

### ✅ Containers on the Custom Network

```bash
docker run -dit --name raghav_nginx1 --network raghav_network nginx

docker run -dit --name raghav_nginx2 --network raghav_network nginx
```

### ❌ Container on the Default Bridge Network

```bash
docker run -dit --name raghav_busybox busybox sh
```

Check running containers:

```bash
docker ps
```

---

## 🔄 Step 3: Verify Connectivity Between Containers

### ✅ Ping Between Containers on the Custom Network

```bash
docker exec -it raghav_nginx1 ping -c 4 raghav_nginx2
```

Expected output:

```
PING raghav_nginx2 (192.168.1.x): 56 data bytes
64 bytes from 192.168.1.x: icmp_seq=1 ttl=64 time=0.05 ms
```

### ❌ Ping Between Containers on Different Networks

```bash
docker exec -it raghav_nginx1 ping -c 4 raghav_busybox
```

Expected output:

```
ping: raghav_busybox: Name or service not known
```

This demonstrates that containers on different networks **cannot** communicate unless explicitly connected.

---

## 📂 Step 4: Inspect Networks

### 🔍 View Custom Network Details

```bash
docker network inspect raghav_network
```

This will list all containers in `raghav_network`, including `raghav_nginx1` and `raghav_nginx2`.

### 🔍 View Default Bridge Network

```bash
docker network inspect bridge
```

This will list `raghav_busybox`, confirming it is isolated.

---

## 🚧 Step 5: Cleanup After Experiment

To remove the containers and the network:

```bash
docker rm -f raghav_nginx1 raghav_nginx2 raghav_busybox

docker network rm raghav_network
```

---

## 📌 Key Takeaways

✅ Containers on the **same custom network** can communicate.
✅ Containers on **different networks are isolated** by default.
✅ **Custom networks offer better control** over container communication.
✅ To allow inter-network communication, **explicit connections must be configured**.

---

## 🌟 Next Steps

-   **Experiment with multiple networks & inter-network communication.**
-   **Use network aliases for easier container discovery.**
-   **Explore Docker Compose for multi-container networking setups.**

🚀 **Mastering Docker networking is crucial for scalable and secure deployments!** 🎯
