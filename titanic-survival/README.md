# 🚢 Titanic Survival Prediction - Streamlit + Docker

## 📌 Quick Start

Run in 3 simple commands:

```bash
docker build -t titanic-prediction .  # Build the container
docker run -p 8502:8502 titanic-prediction  # Launch the app
# Open http://localhost:8502 in your browser 🌐
```

---

## 🧰 Tech Stack

| Component            | Technology                  |
| -------------------- | --------------------------- |
| **Frontend**         | Streamlit                   |
| **Backend**          | Scikit-learn, Pandas, NumPy |
| **Containerization** | Docker                      |
| **Visualization**    | Seaborn                     |

---

## 🗂 Project Structure

```
Titanic-Prediction-Model/
│── Dockerfile               # Docker setup for deployment
│── requirements.txt         # Dependency manifest
│── main.py                  # Streamlit app script
│── config.toml              # Streamlit server configuration
│── model.pkl                # Pre-trained Titanic model
│── images/                  # Images for UI enhancement
```

---

## 🔍 Key Files Explained

### 🐋 Dockerfile - Container Setup

```dockerfile
FROM python:3.12.3-slim  # Optimized base image
WORKDIR /app             # Organized workspace
RUN pip install --upgrade pip setuptools wheel  # Dependency handling
COPY requirements.txt .  # Leverage Docker caching
RUN pip install --no-cache-dir -r requirements.txt  # Install dependencies
COPY . .                 # Include app files, model, and images
EXPOSE 8502              # Port for Streamlit app
CMD ["streamlit", "run", "main.py", "--server.port=8502", "--server.runOnSave=true"]  # Run app
```

### ⚙️ config.toml - Streamlit Configuration

```toml
[server]
headless = true
runOnSave = true
fileWatcherType = "poll"
```

### 🎯 main.py - Titanic Survival Predictor (Features Overview)

-   Accepts user inputs like **Passenger Class, Age, Gender, Fare, Family Size, and Embarkation Port**.
-   Loads a **pre-trained model (model.pkl)** to predict survival chances.
-   **Interactive UI** using Streamlit widgets (dropdowns, number inputs, buttons).
-   **Displays survival prediction** in a formatted message.
-   **Includes visual feedback** with images based on prediction results.

---

## 🛠 Development Workflow

### 🚀 Build & Run the App

```bash
docker build -t titanic-prediction:v1.0 .  # Build with version tag
docker run -p 8502:8502 --name titanic-app titanic-prediction  # Run container
```

### 🛠 Troubleshooting

#### ❌ Port Conflict?

```bash
docker run -p 8503:8502 titanic-prediction  # Change port if needed
```

#### 🛑 Remove Stuck Containers

```bash
docker ps -a  # Find container ID
docker rm -f <container_id>  # Force remove
```

#### 🔍 Need Shell Access?

```bash
docker exec -it titanic-app /bin/bash
```

---

## 🌟 Next Steps

-   Enhance UI with **more visualizations**.
-   Improve model accuracy with **better feature engineering**.
-   Deploy on **Cloud Services (AWS, GCP, etc.)**.

📜 **License:** MIT - Free to use, modify, and share!

Made by Raghav Agarwal 🚀
