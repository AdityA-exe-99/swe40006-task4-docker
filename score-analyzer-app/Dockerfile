# --- Optimized Dockerfile for Task 4.4 ---
# Small base image, no unnecessary packages
FROM python:3.12-slim

WORKDIR /app

# Only standard library is used, so no requirements.txt/pip install needed
COPY analyzer.py .

# Create a non-root user and switch to it, same best practice as 4.3
RUN useradd --create-home appuser
USER appuser

# /data is where the host's scores.txt / report.txt get mounted at runtime
# with "docker run -v", this is not baked into the image on purpose
CMD ["python", "analyzer.py"]
