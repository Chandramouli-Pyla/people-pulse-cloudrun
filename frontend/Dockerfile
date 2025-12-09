# frontend/Dockerfile

FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

RUN pip install --no-cache-dir --upgrade pip

# Install frontend dependencies
COPY frontend/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy frontend source code
COPY frontend ./frontend

EXPOSE 8080

# Start Streamlit
CMD ["sh", "-c", "streamlit run frontend/streamlit_app.py \
    --server.port ${PORT:-8080} \
    --server.address 0.0.0.0 \
    --server.enableCORS=false \
    --server.enableXsrfProtection=false"]
