# Build des dépendances
FROM python:3.11-alpine AS builder
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Création de l'image
FROM python:3.11-alpine
LABEL maintainer="Hugo Mayonobe <hugomayonobe@gmail.com>"
WORKDIR /app
RUN apk add --no-cache curl
COPY --from=builder /usr/local /usr/local
COPY app.py .
ENV FLASK_APP=app.py
EXPOSE 5000
CMD ["sh", "-c", "if [ \"$FLASK_ENV\" = development ]; then flask run --host=0.0.0.0; else gunicorn -b 0.0.0.0:5000 app:app; fi"]
