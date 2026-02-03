FROM python:3.12.4-slim


# Install system dependencies
RUN apt-get update && apt-get install -y \
    ffmpeg \
    && rm -rf /var/lib/apt/lists/*


WORKDIR /app


# Copy and install Python dependencies
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt


ENV API_SECRET_KEY=TOP_SECRET


# Copy the rest of the application
COPY . .

# Use shell form for CMD to allow environment variable substitution for $PORT
CMD uvicorn app.main:app --host 0.0.0.0 --port=7860