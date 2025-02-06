FROM python:3.10-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    net-tools \
    curl \
    wget \
    git \
    procps\
    && rm -rf /var/lib/apt/lists/*

# Copy the requirements file first to leverage Docker cache
COPY requirements.txt .

# Install Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Install dev tools
RUN pip install --no-cache-dir pytest-cov debugpy

# Copy the application code
COPY . .

# Expose the application port
EXPOSE 8000

