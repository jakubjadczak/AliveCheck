import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()


def fetch() -> list:

    conn = psycopg2.connect(
        f"dbname={os.getenv('POSTGRES_DB')} user={os.getenv('POSTGRES_USER')} password={os.getenv('POSTGRES_PASSWORD')} host={os.getenv('POSTGRES_HOST')}"
    )
    cur = conn.cursor()

    array = cur.execute("SELECT * FROM addresses_ipaddress")
    array = cur.fetchall()

    cur.close()
    conn.close()

    return array
