# 🚀 Streamlit & PostgreSQL in Docker 🐳

## 📌 Introduction

This guide walks through setting up a Streamlit app connected to PostgreSQL, both running in Docker containers. We will:

-   Run PostgreSQL in a Docker container.
-   Initialize a database with a `passengers` table.
-   Deploy a Streamlit app to interact with the database.
-   Use Docker Compose for easy setup and management.

## 📂 Project Structure

Ensure your working directory contains the following files:

```
📁 streamlit-postgres-docker
 ├── 📄 Dockerfile                # Defines Streamlit container
 ├── 📄 docker-compose.yml         # Manages services using Docker Compose
 ├── 📄 requirements.txt          # Python dependencies
 ├── 📄 main.py                   # Streamlit app (overview below)
 ├── 📄 init.sql                  # PostgreSQL initialization script
```

## 📝 SQL Initialization Script (init.sql)

This script ensures the database and table exist and inserts sample data.

```sql
-- Create `passengers` table if it doesn't exist
CREATE TABLE IF NOT EXISTS passengers (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    location VARCHAR(100) NOT NULL
);

-- Insert sample data (only if table is empty)
INSERT INTO passengers (name, location)
SELECT 'Raghav Agarwal', 'Dehradun'
WHERE NOT EXISTS (SELECT 1 FROM passengers WHERE name = 'Raghav Agarwal');

INSERT INTO passengers (name, location)
SELECT 'Aryan Soni', 'Delhi'
WHERE NOT EXISTS (SELECT 1 FROM passengers WHERE name = 'Aryan Soni');
```

## 🐳 Docker Compose Configuration (docker-compose.yml)

This file defines the PostgreSQL and Streamlit services.

```yaml
version: "3.8"

services:
    postgres:
        image: postgres:latest
        container_name: my_postgres_container
        restart: always
        environment:
            POSTGRES_DB: testdb
            POSTGRES_USER: raghav
            POSTGRES_PASSWORD: secret
        ports:
            - "5432:5432"
        volumes:
            - postgres_data:/var/lib/postgresql/data
            - ./init.sql:/docker-entrypoint-initdb.d/init.sql

    streamlit:
        build: .
        container_name: my_streamlit_app
        restart: always
        ports:
            - "8501:8501"
        depends_on:
            - postgres

volumes:
    postgres_data:
```

## 🐍 Python Dependencies (requirements.txt)

```txt
streamlit
psycopg2
```

## 📜 Streamlit Application (main.py - Overview)

The Streamlit app:

-   Connects to PostgreSQL using `psycopg2`
-   Fetches passengers' data and displays it in a styled format
-   Allows adding new passengers dynamically
-   Refreshes automatically when changes are made

### UI Features:

-   Custom CSS styling for a clean and modern look
-   Live updates without manual refresh
-   Error handling for database connectivity

For full details, refer to `main.py` in the project.

## 📦 Dockerfile for Streamlit (Dockerfile)

```dockerfile
FROM python:3.9

# Set the working directory
WORKDIR /app

# Copy necessary files
COPY requirements.txt .
COPY main.py .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the Streamlit port
EXPOSE 8501

# Run the Streamlit app
CMD ["streamlit", "run", "main.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

## 🛠 Steps to Run the Application

### 1️⃣ Clone the Repository & Navigate to the Project

```sh
git clone <repo-link>
cd streamlit-postgres-docker
```

### 2️⃣ Build & Run Containers

```sh
docker-compose up --build -d
```
![Screenshot](/Streamlit%20&%20PostgreSQL,%20docked/assets/image1.png)
![Screenshot](/Streamlit%20&%20PostgreSQL,%20docked/assets/image2.png)

-   `--build` → Ensures fresh build.
-   `-d` → Runs in detached mode.

### 3️⃣ Access the Streamlit App

Open [http://localhost:8501](http://localhost:8501) in your browser.
![Screenshot](/Streamlit%20&%20PostgreSQL,%20docked/assets/image.png)

### 4️⃣ Check PostgreSQL Database

Enter the PostgreSQL container:

```sh
docker exec -it my_postgres_container psql -U raghav -d testdb
```

Then, run:

```sql
SELECT * FROM passengers;
```

### 5️⃣ Stopping & Removing Containers

```sh
docker-compose down
```

This will stop and remove the containers, but data remains in `postgres_data` volume.

## 🎯 Conclusion

✅ We successfully set up PostgreSQL and Streamlit inside Docker containers.
✅ The database initializes automatically with sample data.
✅ The Streamlit app fetches and displays live data from PostgreSQL.
✅ We used Docker Compose to manage both services efficiently.

## 🚀 Next Steps

🔹 Add a form in Streamlit to insert new passengers.
🔹 Use volumes to persist PostgreSQL data even after `docker-compose down`.
🔹 Connect this setup to a React frontend for a full-stack experience.

🎯 Keep exploring and happy coding! 🚀
