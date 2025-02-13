# 🚀 Docker Volume Persistence: Bind Mounts on Linux Container 🐳

## 📌 Introduction

This experiment demonstrates how to use **Docker bind mounts** to persist data beyond a container’s lifecycle. By mounting a local directory into a container, data remains accessible even after the container is removed. This ensures **data persistence** across different container instances.

---

## 🔧 Steps & Observations

### 🏗 Step 1: Running a Container with a Bind Mount

Run the following command to start a container with a bind mount:

```sh
docker run -dit --name raghav_alpine_bind -v /home/raghav/docker_data:/data alpine:latest sh
```

### 🔍 What Happened?

-   **If the `alpine:latest` image is not available locally, Docker will pull it from the official repository.**
-   **A new container named `raghav_alpine_bind` is created.**
-   **The `-v` flag mounts the local directory `/home/raghav/docker_data` to `/data` inside the container.**
-   **The container starts a shell (`sh`) in detached mode.**

---

### 📄 Step 2: Creating a File Inside the Bind Mount

Inside the container, create a test file:

```sh
docker exec -it raghav_alpine_bind sh -c "echo 'Hello, Raghav!' > /data/testfile.txt"
```

### 🔍 What Happened?

-   **The command executes a shell inside the running container.**
-   **It creates a file `testfile.txt` inside `/data` and writes `Hello, Raghav!` into it.**
-   **Since `/data` is a bind-mounted directory, the file is actually stored on the host at `/home/raghav/docker_data`.**

---

### ✅ Step 3: Verifying the File Exists

To check the contents of the file inside the container:

```sh
docker exec -it raghav_alpine_bind sh -c "cat /data/testfile.txt"
```

📌 **Expected Output:**

```sh
Hello, Raghav!
```

This confirms that the file was successfully created and is accessible inside the container. 🎉

---

### 🗑 Step 4: Removing the First Container

Remove the container:

```sh
docker rm -f raghav_alpine_bind
```

### 🔍 What Happened?

-   **The container is forcefully stopped and removed.**
-   **However, since `testfile.txt` was inside the bind-mounted directory, it remains on the host system.** 🏠

---

### 🔄 Step 5: Creating a New Container with the Same Bind Mount

Start a new container using the same bind mount:

```sh
docker run -dit --name raghav_new_alpine -v /home/raghav/docker_data:/data alpine sh
```

### 🔍 What Happened?

-   **A new container named `raghav_new_alpine` is created.**
-   **The same bind-mounted directory (`/home/raghav/docker_data`) is mounted to `/data`.**

---

### 🔎 Step 6: Verifying File Persistence

Check if `testfile.txt` still exists inside the new container:

```sh
docker exec -it raghav_new_alpine sh -c "cat /data/testfile.txt"
```

📌 **Expected Output:**

```sh
Hello, Raghav!
```

This confirms that **bind mounts persist data even after a container is removed.** 🔥

---

## 🎯 Conclusion

✅ Bind mounts allow **data persistence** across multiple container instances.
✅ Deleting a container **does not remove** data stored in the bind-mounted directory.
✅ Any **new container with the same mount** can access previous container data.
✅ Bind mounts are useful for **sharing files** between containers and persisting important data beyond a container’s lifecycle.

---

## 🚀 Next Steps

🛠 **Experiment with named volumes** (`docker volume create`) for better data management.
🐳 **Try bind mounts with different container images** like `nginx` or `busybox`.
🔐 **Explore permission settings** for secure file access between host and container.

### 🎯 This experiment showcases the power of bind mounts in Docker. Keep exploring, and happy coding! 🚀
