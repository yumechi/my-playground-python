# ベースイメージは常に最新の 3.14 系を取得する（同梱 Python のパッチは固定しない）
# プロジェクトで使う Python は mise.toml / .python-version で固定
FROM mcr.microsoft.com/devcontainers/python:3.14

# Upgrade pip to the latest version
RUN python -m pip install --no-cache-dir --upgrade pip==26.2.2

# Install mise system-wide (バージョン固定)
RUN curl https://mise.run | MISE_VERSION=v2026.10.19 sh && \
    cp /root/.local/bin/mise /usr/local/bin/ && \
    chmod +x /usr/local/bin/mise
