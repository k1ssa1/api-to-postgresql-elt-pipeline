from extract.extract_products import extract_product_data

from psycopg.types.json import Jsonb

from database import connect_db

conn = connect_db()

def main():
    product_data = extract_product_data()
    products = product_data["products"]
    curr = conn.cursor()
    try:
        curr.execute("CREATE TABLE IF NOT EXISTS raw_products_data(id INT PRIMARY KEY, raw_data JSONB)")
        conn.commit()
        for d in products:
            curr.execute("INSERT INTO raw_products_data (id, raw_data) VALUES (%s, %s)", (d["id"], Jsonb(d)))
        conn.commit()
    finally:
        curr.close()
        conn.close()
main()