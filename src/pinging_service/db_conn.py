import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()


def insert_stat(data: dict):

    conn = psycopg2.connect(
        f"dbname={os.getenv('POSTGRES_DB')} user={os.getenv('POSTGRES_USER')} password={os.getenv('POSTGRES_PASSWORD')} host={os.getenv('POSTGRES_HOST')}"
    )
    cur = conn.cursor()

    insert_query = "INSERT INTO addresses_pingstat (timestamp, avarage_response, is_alive, address_id, packet_loss) VALUES (%s, %s, %s, %s, %s)"
    data_to_insert = (
        data["timestamp"],
        data["avarage_response"],
        data["is_alive"],
        data["address_id"],
        data["packet_loss"],
    )

    cur.execute(insert_query, data_to_insert)

    conn.commit()

    cur.close()
    conn.close()
