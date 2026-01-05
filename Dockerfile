FROM python:3.13-slim

ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN apt-get update -qq && \
    apt-get install -y -qq build-essential curl && \
    rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt gunicorn

COPY . .

RUN chmod +x entrypoint.sh

EXPOSE 5556

ENTRYPOINT ["./entrypoint.sh"]
