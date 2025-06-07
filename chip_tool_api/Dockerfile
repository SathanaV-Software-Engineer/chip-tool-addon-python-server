# Use a lightweight Python base image
FROM python:3.11-slim

# Install chip-tool dependencies (adjust as needed for your system)
RUN apt-get update && apt-get install -y \
    git \
    unzip \
    libavahi-compat-libdnssd-dev \
    libssl-dev \
    libstdc++6 \
    avahi-daemon \
    dbus \
    curl \
    && apt-get clean

# Set working directory
WORKDIR /app

# Copy app files
COPY chip_tool_server.py /app/chip_tool_server.py
COPY run.sh /app/run.sh
COPY requirements.txt /app/requirements.txt

# Install Python requirements
RUN pip install --no-cache-dir -r requirements.txt

# Make run.sh executable
RUN chmod +x /app/run.sh

# Expose API port
EXPOSE 6000

# Entry point
ENTRYPOINT ["/app/run.sh"]
