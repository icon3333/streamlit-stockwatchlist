FROM python:3.9-alpine

# Install git and clean up cache in the same layer to keep image size down
RUN apk update && \
    apk add --no-cache git && \
    rm -rf /var/cache/apk/*

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