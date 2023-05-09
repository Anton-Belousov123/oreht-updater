import time

import psycopg2
from misc import sc

def update_price_values(data):
    try:
        conn = psycopg2.connect(
            host=sc.secret.DATABASE_HOST,
            database=sc.secret.DATABASE_NAME,
            user=sc.secret.DATABASE_LOGIN,
            password=sc.secret.DATABASE_PASSWORD
        )
        cur = conn.cursor()
        sql_query = "UPDATE kamran SET price = (CASE article "
        for article, price, count in data:
            sql_query += f"WHEN {article} THEN {price} "
        sql_query += "ELSE price END), count = (CASE article "
        for article, price, count in data:
            sql_query += f'WHEN {article} THEN {count} '
        sql_query += "ELSE count END), source_update_date = (CASE article "
        t = int(time.time())
        for _ in data:
            sql_query += f'WHEN {article} THEN {t} '
        sql_query += "ELSE source_update_date END)"
        cur.execute(sql_query)
        conn.commit()
        cur.close()
        conn.close()
        print("Данные успешно обновлены")
    except (Exception, psycopg2.Error) as error:
        print("Ошибка при работе с PostgreSQL", error)


def get_item_list():
    conn = psycopg2.connect(
        host=sc.secret.DATABASE_HOST,
        database=sc.secret.DATABASE_NAME,
        user=sc.secret.DATABASE_LOGIN,
        password=sc.secret.DATABASE_PASSWORD
    )
    cur = conn.cursor()
    cur.execute(f"SELECT * FROM kamran WHERE stage=%s", ("Suggested",))
    records = cur.fetchall()
    return records
