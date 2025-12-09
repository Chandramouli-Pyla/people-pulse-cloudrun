# backend/Dockerfile

FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

# Upgrade pip
RUN pip install --no-cache-dir --upgrade pip

# Install backend dependencies
COPY backend/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy backend source code
COPY backend ./backend

# Expose port for documentation purposes (Cloud Run uses $PORT)
EXPOSE 8080

# Start FastAPI with uvicorn
# Cloud Run injects $PORT (default 8080); we fall back to 8080 if not set
CMD ["sh", "-c", "uvicorn backend.main:app --host 0.0.0.0 --port ${PORT:-8080}"]