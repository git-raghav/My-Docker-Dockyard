# 🚀 Running a Streamlit App in Docker on AWS EC2

## 📜 Table of Contents

1. 🛠 Setting Up a VPC, Subnet, Route Table, and Internet Gateway
2. 🖥️ Launching and Configuring an EC2 Instance
3. 🔗 Connecting to EC2 Instance via EC2 Instance Connect
4. 🔑 Setting Permissions for the PEM Key
5. 🐳 Installing and Configuring Docker on EC2
6. 📂 Copying Project Files to EC2
7. 🏗️ Building and Running the Docker Container
8. 🌐 Accessing the Streamlit App
9. 🔄 Managing the Docker Container

---

## 1️⃣ Setting Up a VPC, Subnet, Route Table, and Internet Gateway

To ensure a well-structured networking setup, follow these steps in the AWS Management Console.

### 1.1 Create a New VPC
1. Navigate to **AWS Console → VPC Dashboard**.
2. Click **Create VPC**.
3. Enter:
   - **Name:** MyCustomVPC
   - **IPv4 CIDR block:** 10.0.0.0/16
4. Click **Create VPC**.

### 1.2 Create a Subnet
1. Go to **VPC Dashboard → Subnets → Create Subnet**.
2. Select **MyCustomVPC**.
3. Enter:
   - **Subnet name:** MyPublicSubnet
   - **CIDR block:** 10.0.1.0/24
   - **Availability Zone:** Select any zone.
4. Click **Create Subnet**.

### 1.3 Enable Auto-Assign Public IPv4
1. Go to **Subnets**.
2. Select **MyPublicSubnet**.
3. Click **Actions → Edit Subnet Settings**.
4. Enable **Auto-assign public IPv4 address**.
5. Click **Save changes**.

### 1.4 Create an Internet Gateway
1. Go to **VPC Dashboard → Internet Gateways**.
2. Click **Create Internet Gateway**.
3. Name it **MyIGW** and click **Create**.
4. Attach it to **MyCustomVPC**:
   - Select **MyIGW**.
   - Click **Actions → Attach to VPC → Select MyCustomVPC**.
   - Click **Attach**.

### 1.5 Create a Route Table
1. Go to **VPC Dashboard → Route Tables**.
2. Click **Create Route Table**.
3. Name it **MyPublicRouteTable**, select **MyCustomVPC**, and click **Create**.
4. Select **MyPublicRouteTable**, go to the **Routes** tab.
5. Click **Edit routes → Add route**:
   - **Destination:** 0.0.0.0/0
   - **Target:** Select **MyIGW**.
6. Click **Save changes**.

### 1.6 Associate the Subnet with the Route Table
1. Go to **Route Tables**.
2. Select **MyPublicRouteTable**.
3. Click **Subnet Associations → Edit Subnet Associations**.
4. Select **MyPublicSubnet** and click **Save**.

---

## 2️⃣ Launching and Configuring an EC2 Instance

### 2.1 Create an EC2 Instance
1. Go to **EC2 Dashboard → Instances → Launch Instance**.
2. Configure:
   - **Name:** Streamlit-EC2
   - **AMI:** Select **Amazon Linux 2023**
   - **Instance Type:** t2.micro (Free Tier)
   - **Key Pair:** Create or use an existing key pair.
   - **Network Settings:**
     - **VPC:** Select **MyCustomVPC**.
     - **Subnet:** Select **MyPublicSubnet**.
     - **Auto-assign public IP:** Enabled.
   - **Security Group:**
     - Allow **SSH (port 22)**.
     - Allow **HTTP (port 80, optional)**.
     - Allow **Streamlit (port 8501)**.
3. Click **Launch Instance**.

---

## 3️⃣ Connecting to EC2 Using EC2 Instance Connect

1. Go to **EC2 Dashboard → Instances**.
2. Select **Streamlit-EC2**.
3. Click **Connect**.
4. Choose **EC2 Instance Connect**.
5. Click **Connect** (Opens a browser-based terminal).

---

## 4️⃣ Setting Permissions for the PEM Key

Move your `.pem` key to your work directory:
```sh
mv /path/to/your-key.pem ~/your-work-directory/
```
Or copy-paste it into your work directory.

Set the correct permissions:
```sh
chmod 600 your-key.pem
```
![Screenshot](/Running%20a%20Streamlit%20App%20in%20Docker%20on%20AWS%20EC2/images/1.jpg)

## 5️⃣ Installing and Configuring Docker on EC2

Update packages:
```sh
sudo yum update -y
```
Install Docker:
```sh
sudo yum install -y docker
```
![Screenshot](/Running%20a%20Streamlit%20App%20in%20Docker%20on%20AWS%20EC2/images/2.jpg)

Enable and start Docker:
```sh
sudo systemctl enable docker
```

```sh
sudo systemctl start docker
```
![Screenshot](/Running%20a%20Streamlit%20App%20in%20Docker%20on%20AWS%20EC2/images/3.jpg)

## 6️⃣ Copying Project Files to EC2

Transfer files using SCP:
```sh
scp -i your-key.pem app.py Dockerfile requirements.txt mushroom.cv ec2-user@your-ec2-public-ip:/home/ec2-user/
```
![Screenshot](/Running%20a%20Streamlit%20App%20in%20Docker%20on%20AWS%20EC2/images/4.jpg)

## 7️⃣ Building and Running the Docker Container

Navigate to the directory:
```sh
cd /home/ec2-user/
```
Build the Docker image:
```sh
sudo docker build -t streamlit-app .
```
Run the container:
```sh
sudo docker run -d -p 8501:8501 --name streamlit_container streamlit-app
```
![Screenshot](/Running%20a%20Streamlit%20App%20in%20Docker%20on%20AWS%20EC2/images/5.jpg)

## 8️⃣ Accessing the Streamlit App

Open your browser and go to:
```sh
http://your-ec2-public-ip:8501
```
The Streamlit app should now be accessible.

![Screenshot](/Running%20a%20Streamlit%20App%20in%20Docker%20on%20AWS%20EC2/images/6.jpg)

## 9️⃣ Managing the Docker Container

Check running containers:
```sh
sudo docker ps
```
Stop the container:
```sh
sudo docker stop streamlit_container
```
Remove the container:
```sh
sudo docker rm streamlit_container
```
Restart the container:
```sh
sudo docker start streamlit_container
```

---

## 🎯 Conclusion

This documentation provides a step-by-step guide to:

✅ Set up a **custom VPC, subnet, and Internet Gateway**

✅ Launch an **EC2 instance** and enable **IPv4 assignment**

✅ Install **Docker** and deploy the **Streamlit app** in a Docker container

✅ Access the app via a **public IP**

This setup ensures **scalability, security, and reliability** for your project. 🚀
