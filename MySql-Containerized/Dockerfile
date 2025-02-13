FROM mysql:latest

# Set the root password environment variable
ENV MYSQL_ROOT_PASSWORD=root

# Copy your SQL initialization script into the proper directory
COPY raghav_demo.sql /docker-entrypoint-initdb.d/
