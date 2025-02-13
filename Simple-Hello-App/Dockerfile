# Use Python 3.12.3 as the base image
FROM python:3.12.3-slim

# Set the working directory
WORKDIR /app

# Copy requirements file
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Create the Streamlit configuration directory
RUN mkdir -p ~/.streamlit

# Copy the custom Streamlit configuration file
COPY config.toml ~/.streamlit/config.toml

# Copy the rest of the app code
COPY . .

# Expose the port Streamlit will run on
EXPOSE 8501

# Command to run Streamlit app
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.runOnSave=true"]
