FROM python:3.11-slim

WORKDIR /app

# Install system deps (if needed) and python deps
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

# Copy project
COPY . /app

# Default command runs tests
CMD ["pytest", "-q"]
