# ─── Stage 1: build ───────────────────────────────────────────────────────────
FROM python:3.13-slim AS builder

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=1

WORKDIR /app

RUN apt-get update -qq && \
    apt-get install -y -qq build-essential && \
    rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt gunicorn

# ─── Stage 2: runtime ─────────────────────────────────────────────────────────
FROM python:3.13-slim

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    DJANGO_SETTINGS_MODULE=sumconnect.settings

WORKDIR /app

# Copy installed packages from builder
COPY --from=builder /usr/local/lib/python3.13/site-packages /usr/local/lib/python3.13/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin

# Copy source code
COPY . .

# Collect static files at build time (SECRET_KEY placeholder is fine for collectstatic)
RUN SECRET_KEY=collectstatic-placeholder \
    python manage.py collectstatic --noinput --clear

EXPOSE 8000

# Entrypoint: migrate then serve
CMD ["sh", "-c", "python manage.py migrate --noinput && \
    gunicorn sumconnect.wsgi:application \
    --bind 0.0.0.0:8000 \
    --workers 2 \
    --threads 2 \
    --timeout 120 \
    --access-logfile - \
    --error-logfile -"]
