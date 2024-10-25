FROM python:3.9-slim

# Install git and clean up cache in the same layer to keep image size down
RUN apt-get update && \
    apt-get install -y git && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Set the working directory
WORKDIR /app

# Clone the repository (will be overwritten by volume mount in dev)
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Create data directory
RUN mkdir -p data

# Expose Streamlit port
EXPOSE 8501

# Command to run the application
CMD ["streamlit", "run", "app.py"]