# Use mcr.microsoft.com/devcontainers/python:3.14 as the base image
FROM mcr.microsoft.com/devcontainers/python:3.14

# Upgrade pip to the latest version
RUN python -m pip install --no-cache-dir --upgrade pip==26.2.2

# Install mise system-wide
RUN curl https://mise.run | sh && \
    cp /root/.local/bin/mise /usr/local/bin/ && \
    chmod +x /usr/local/bin/mise
