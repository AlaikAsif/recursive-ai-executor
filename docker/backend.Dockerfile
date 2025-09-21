# Backend Dockerfile
# Uses official Python image, creates a non-root user, installs dependencies and runs uvicorn
FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

# Add a non-root user
RUN addgroup --system appgroup && adduser --system --ingroup appgroup appuser

# Install system deps for uvicorn extras and docker (if needed)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    gcc \
    libffi-dev \
    libssl-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install
COPY backend/requirements.txt /app/backend_requirements.txt
RUN python -m pip install --upgrade pip \
    && pip install --no-cache-dir -r /app/backend_requirements.txt

# Copy application
COPY backend /app/backend

# Expose port
EXPOSE 8000

# Switch to non-root
USER appuser

# Default command
CMD ["python", "-m", "uvicorn", "backend.app.main:app", "--host", "0.0.0.0", "--port", "8000"]
