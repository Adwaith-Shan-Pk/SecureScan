FROM python:3.12-slim

WORKDIR /app

# Install ClamAV and dependencies
RUN apt-get update && apt-get install -y clamav clamav-daemon && \
    freshclam && \
    mkdir -p /var/run/clamav && chown -R root:root /var/run/clamav && \
    echo "TCPSocket 3310" >> /etc/clamav/clamd.conf && \
    echo "Foreground true" >> /etc/clamav/clamd.conf

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .
EXPOSE 5000

# Start clamd and Flask
CMD ["sh", "-c", "clamd & sleep 5 && python -m flask run --host=0.0.0.0"]