FROM python:3.11-slim

ARG VERSION=dev
ARG VCS_REF=local
ARG BUILD_DATE=unknown
ARG SOURCE=https://github.com/example/student-ml-api

LABEL org.opencontainers.image.title="student-ml-api" \
      org.opencontainers.image.description="Flask prediction API for the MLOps assignment" \
      org.opencontainers.image.version="$VERSION" \
      org.opencontainers.image.revision="$VCS_REF" \
      org.opencontainers.image.created="$BUILD_DATE" \
      org.opencontainers.image.source="$SOURCE" \
      org.opencontainers.image.url="$SOURCE" \
      org.opencontainers.image.licenses="Academic"

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PORT=5000

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py VERSION ./

EXPOSE 5000

CMD ["python", "app.py"]
