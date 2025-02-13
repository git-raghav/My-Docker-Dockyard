# 🚀 Setting Up MySQL in Docker with Raghav's Database 🐳

## 📌 Introduction

This guide walks through setting up a MySQL database inside a Docker container using an initialization script. We will:

-   Create a custom MySQL database (`RaghavDB`).
-   Use an SQL script (`raghav_demo.sql`) to initialize the database.
-   Run the MySQL container with persistent data.
-   Access and verify the database.

## 📂 Project Structure

Ensure the following files are present in your working directory:

```
📁 mysql-docker-setup
 ├── 📄 Dockerfile
 ├── 📄 raghav_demo.sql
```

## 📝 SQL Initialization Script: `raghav_demo.sql`

This script creates a database and a `students` table with sample data.

```sql
CREATE DATABASE IF NOT EXISTS RaghavDB;
USE RaghavDB;

CREATE TABLE students (
    StudentID INT NOT NULL AUTO_INCREMENT,
    FirstName VARCHAR(100) NOT NULL,
    Surname VARCHAR(100) NOT NULL,
    PRIMARY KEY (StudentID)
);

INSERT INTO students (FirstName, Surname)
VALUES ('Raghav', 'Agarwal'), ('Aryan', 'Soni');
```

## 🐳 Dockerfile for MySQL Container

This `Dockerfile` sets up the MySQL environment and loads the SQL script.

```dockerfile
FROM mysql:latest

# Set root password environment variable
ENV MYSQL_ROOT_PASSWORD=root

# Copy the SQL initialization script into the correct directory
COPY raghav_demo.sql /docker-entrypoint-initdb.d/
```

## 🛠 Steps to Run the MySQL Docker Container

### 1️⃣ **Build the Docker Image**

Run the following command in the directory containing the `Dockerfile` and `raghav_demo.sql`:

```sh
docker build -t raghav-mysql .
```

### 2️⃣ **Run the MySQL Container**

Start a MySQL container with a custom database:

```sh
docker run -d --name raghav-mysql-container -p 3306:3306 raghav-mysql
```

-   `-d` → Runs the container in detached mode.
-   `--name raghav-mysql-container` → Assigns a name to the container.
-   `-p 3306:3306` → Maps port 3306 on the host to 3306 in the container.

### 3️⃣ **Access the MySQL Database**

To connect to MySQL inside the container:

```sh
docker exec -it raghav-mysql-container mysql -uroot -p
```

(Enter password `root` when prompted.)

### 4️⃣ **Verify the Database and Table**

After logging into MySQL, run:

```sql
SHOW DATABASES;
USE RaghavDB;
SHOW TABLES;
SELECT * FROM students;
```

✅ Expected Output:

```
+--------------------+
| Database          |
+--------------------+
| RaghavDB          |
| information_schema |
| mysql             |
| performance_schema |
| sys               |
+--------------------+

+-------------------+
| Tables_in_RaghavDB |
+-------------------+
| students         |
+-------------------+

+-----------+----------+---------+
| StudentID | FirstName | Surname |
+-----------+----------+---------+
|         1 | Raghav   | Agarwal |
|         2 | Aryan    | Soni    |
+-----------+----------+---------+
```

## 🎯 Conclusion

✅ We successfully set up MySQL inside a Docker container.
✅ Our initialization script created a database and populated it with sample data.
✅ The database remains available as long as the container is running.
✅ This setup can be used in real-world projects for database persistence.

## 🚀 Next Steps

🔹 Experiment with **volume mounts** to persist MySQL data even if the container is removed.
🔹 Use **Docker Compose** to manage multi-container applications.
🔹 Connect this database to a **Node.js** or **Python** application for further development.

🎯 Keep exploring and happy coding! 🚀
