import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()


def fetch() -> list:

    conn = psycopg2.connect(
        "dbname=postgres user=postgres password=postgres host=postgres"
    )
    cur = conn.cursor()

    array = cur.execute("SELECT * FROM addresses_ipaddress")
    array = cur.fetchall()

    cur.close()
    conn.close()

    return array
