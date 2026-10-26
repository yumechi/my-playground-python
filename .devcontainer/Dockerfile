# ベースイメージはダイジェストで固定（タグ 3.14 / 3.2.6-3.14-trixie と同一、同梱 Python は 3.14.8）
# プロジェクトで使う Python は mise.toml / .python-version の 3.14.10
FROM mcr.microsoft.com/devcontainers/python:3.2.6-3.14-trixie@sha256:28835c112fd097cb6d2fe1e195b660d66ae051859070a9b871fa2308f35897d3

# Upgrade pip to the latest version
RUN python -m pip install --no-cache-dir --upgrade pip==26.2.2

# Install mise system-wide (バージョン固定)
RUN curl https://mise.run | MISE_VERSION=v2026.10.19 sh && \
    cp /root/.local/bin/mise /usr/local/bin/ && \
    chmod +x /usr/local/bin/mise
