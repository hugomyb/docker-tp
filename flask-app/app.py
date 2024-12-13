import os
import psycopg2
from flask import Flask

app = Flask(__name__)

def read_secret(secret_path, default_value):
    try:
        with open(secret_path, "r") as file:
            return file.read().strip()
    except FileNotFoundError:
        return default_value


DB_USER = read_secret("/run/secrets/pg_user", "user")
DB_PASSWORD = read_secret("/run/secrets/pg_password", "password")
DB_NAME = read_secret("/run/secrets/pg_db", "mydatabase")
DB_HOST = os.getenv("POSTGRES_HOST", "postgres")
DB_PORT = os.getenv("POSTGRES_PORT", "5432")


def test_db_connection():
    try:
        connection = psycopg2.connect(
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
            port=DB_PORT,
        )
        connection.close()
        print("Connexion à la base de données réussie.")
    except Exception as e:
        print(f"Erreur de connexion à la base de données : {e}")
        exit(1)


@app.route("/")
def hello():
    return "Hello from Flask!"


if __name__ == "__main__":
    print("Démarrage de l'application Flask...")
    test_db_connection()
    app.run(host="0.0.0.0", port=5000)
else:
    print("Démarrage avec Gunicorn...")
    test_db_connection()
