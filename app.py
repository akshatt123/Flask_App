from flask import Flask
import psycopg2
import os

app = Flask(__name__)

# Database connection details
DB_HOST = os.getenv("DB_HOST", "db")
DB_NAME = os.getenv("DB_NAME", "mydb")
DB_USER = os.getenv("DB_USER", "user")
DB_PASS = os.getenv("DB_PASS", "password")

def connect_db():
    try:
        conn = psycopg2.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASS
        )
        return conn
    except Exception as e:
        return str(e)

@app.route('/')
def hello():
    conn = connect_db()
    if isinstance(conn, str):  # If there's an error, return it
        return f"Database Connection Error: {conn}"
    
    return "Hello, Akshat Sahuji & 2022BCD0033"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
