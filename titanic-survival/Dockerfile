# Use Python 3.12.3 as the base image
FROM python:3.12.3-slim

# Set the working directory inside the container
WORKDIR /app

# Upgrade pip
RUN pip install --upgrade pip setuptools wheel

# Install build dependencies (for compiling packages like pickle5)
RUN apt-get update && apt-get install -y build-essential

# Copy the requirements file first to leverage Docker caching
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Create the Streamlit configuration directory
RUN mkdir -p ~/.streamlit

# Copy the custom Streamlit configuration file
COPY config.toml ~/.streamlit/config.toml

# Copy the entire app codebase (including images, model, and script)
COPY . .

# Expose the port Streamlit will run on
EXPOSE 8502

# Command to run Streamlit app (change `app.py` → `main.py`)
CMD ["streamlit", "run", "main.py", "--server.port=8502", "--server.runOnSave=true"]
