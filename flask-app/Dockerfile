# Build des dépendances
FROM python:3.11-alpine AS builder
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Création de l'image
FROM python:3.11-alpine
LABEL maintainer="Hugo Mayonobe <hugomayonobe@gmail.com>"
WORKDIR /app
COPY --from=builder /usr/local /usr/local
COPY app.py .
ENV FLASK_APP=app.py
EXPOSE 5000
CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app"]
