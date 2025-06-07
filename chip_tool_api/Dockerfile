FROM ghcr.io/home-assistant/amd64-base:latest

ENV DEBIAN_FRONTEND=noninteractive
ENV PYTHONUNBUFFERED=1

# Install dependencies
RUN apt-get update && apt-get install -y \
    python3 python3-pip curl \
    libssl-dev libavahi-compat-libdnssd-dev \
    build-essential jq unzip iproute2 avahi-daemon \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Set work directory
WORKDIR /app

# Copy app and chip-tool (chip-tool must already be present in this image)
COPY python_server/ /app/
COPY run.sh /run.sh
RUN chmod +x /run.sh

# Set chip-tool path env
ENV CHIP_TOOL_PATH=/usr/bin/chip-tool
ENV CHIPTOOL_PORT=6000

# Install Python dependencies
RUN pip3 install --no-cache-dir -r /app/requirements.txt

EXPOSE 6000

HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:6000/ || exit 1

CMD ["/run.sh"]
