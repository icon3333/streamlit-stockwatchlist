# Use a Debian-based Python image
FROM python:3.9-slim

# Set environment variables to minimize prompts and logs
ENV DEBIAN_FRONTEND=noninteractive \
    PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

# Install system dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    git \
    build-essential \
    cmake \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . .

# Expose the necessary port
EXPOSE 8501

# Set the entrypoint and command
ENTRYPOINT ["streamlit", "run"]
CMD ["app.py"]
