FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Work inside /app/backend
WORKDIR /app/backend

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy backend code (everything from build context)
COPY . .

# Add /app to python path so "backend" imports work
ENV PYTHONPATH="/app"

EXPOSE 8080

# MUST reference correct module path
CMD ["uvicorn", "backend.main:app", "--host", "0.0.0.0", "--port", "8080"]