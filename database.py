import os
import psycopg

from dotenv import load_dotenv

load_dotenv()

def connect_db():
    conn_string = (
        f"host={os.getenv('DB_HOST')} "
        f"port={os.getenv('DB_PORT')} "
        f"user={os.getenv('DB_USER')} "
        f"password={os.getenv('DB_PASSWORD')} "
        f"dbname={os.getenv('DB_NAME')}"
    )
    try:
        conn = psycopg.connect(conn_string)
        print("Database connection successful")
        return conn
    except Exception as err:
        print("Database connection error: ", err)
        return None

