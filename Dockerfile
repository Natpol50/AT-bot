# Use official Python slim image
FROM python:3.12-slim

ARG BUILD_VERSION=dev

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    ATBOT_DOCKER=1 \
    ATBOT_VERSION=${BUILD_VERSION}

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Create app directory
WORKDIR /app

# Copy requirements first for better caching
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY Files/ ./Files/
COPY README.md LICENSE.md ./

# Create non-root user
RUN useradd -m -u 1000 atbot && chown -R atbot:atbot /app
USER atbot

# Set working directory back to Files for config access
WORKDIR /app/Files

# Run the bot in Docker mode
# Expects DISCORD_TOKEN and DEEPL_API_KEY env vars
ENTRYPOINT ["python", "-u", "AT_bot.py", "--docker"]
CMD []
