# Build des dépendances
FROM python:3.11-alpine AS builder
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Création de l'image
FROM python:3.11-alpine
LABEL maintainer="Hugo Mayonobe <hugomayonobe@gmail.com>"
WORKDIR /app
COPY --from=builder /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
COPY app.py .
ENV FLASK_APP=app.py
EXPOSE 5000
CMD ["python", "-m", "flask", "run", "--host=0.0.0.0"]
