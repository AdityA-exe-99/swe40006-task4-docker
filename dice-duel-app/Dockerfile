# --- Optimized Dockerfile for Task 4.3 ---
# Small base image, not the full python image
FROM python:3.12-slim

WORKDIR /app

# Copy requirements first so this layer is cached and only re-runs
# pip install when requirements.txt actually changes (faster rebuilds)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Now copy the actual app code
COPY app.py .

# Default values for the environment variables the app reads.
# These can be overridden at "docker run" time with -e
ENV APP_NAME="Dice Duel"
ENV DICE_SIDES=6

# Create a non-root user and switch to it, best practice so the app
# isn't running as root inside the container
RUN useradd --create-home appuser
USER appuser

# Document which port the app listens on
EXPOSE 8000

CMD ["python", "app.py"]
