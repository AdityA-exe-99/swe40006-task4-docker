# Small base image with Python already installed
FROM python:3.12-slim

# Folder inside the container where our app will live
WORKDIR /app

# Copy requirements first so Docker can cache this layer
# (only re-installs packages if requirements.txt actually changes)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Now copy the rest of the app code
COPY app.py .

# Document which port the app listens on (informational, doesn't publish it)
EXPOSE 5000

# Start the Flask app when the container runs
CMD ["python", "app.py"]
