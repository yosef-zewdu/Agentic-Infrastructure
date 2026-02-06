FROM python:3.11-slim

WORKDIR /app

# Install system deps (if needed) and python deps
COPY requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir -r /app/requirements.txt

# Copy project
COPY tests/ /app/tests/
COPY specs/ /app/specs/
COPY scripts/ /app/scripts/




# Default command runs tests
CMD ["pytest", "-q"]
