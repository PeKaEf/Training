import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
    
    return conn

def execute_sql(conn, sql):
    try:
        c = conn.cursor()
        c.execute(sql)
    except Error as e:
        print(e)

if __name__ == "__main__":
    create_items_sql = """
    -- items table
    CREATE TABLE IF NOT EXISTS items (
        id integer PRIMARY KEY,
        nazwa text NOT NULL,
        cena float NOT NULL,
        stan_w_magazynie integer NOT NULL
    );
    """

    create_orders_sql = """
    -- orders table
    CREATE TABLE IF NOT EXISTS orders (
        id integer PRIMARY KEY,
        item_id integer NOT NULL,
        klient_id integer NOT NULL,
        data text NOT NULL,
        liczba_sztuk integer NOT NULL,
        suma float NOT NULL,
        FOREIGN KEY (item_id) REFERENCES items (id)
    );
    """

def add_item(conn, item):
    sql = '''INSERT INTO items(nazwa, cena, stan_w_magazynie)
            VALUES(?,?,?)'''
    cur = conn.cursor()
    cur.execute(sql,item)
    conn.commit()
    return cur.lastrowid

def add_order(conn, order):
    sql = '''INSERT INTO orders(item_id, klient_id, data, liczba_sztuk, suma)
            VALUES(?,?,?,?,?)'''
    cur = conn.cursor()
    cur.execute(sql,order)
    conn.commit()
    return cur.lastrowid

db_file = "test_database.db"


def select_all(conn, table):
   cur = conn.cursor()
   cur.execute(f"SELECT * FROM {table}")
   rows = cur.fetchall()

   return rows

def select_where(conn, table, **query):
   cur = conn.cursor()
   qs = []
   values = ()
   for k, v in query.items():
       qs.append(f"{k}=?")
       values += (v,)
   q = " AND ".join(qs)
   cur.execute(f"SELECT * FROM {table} WHERE {q}", values)
   rows = cur.fetchall()
   return rows

def update(conn, table, id, **kwargs):
   parameters = [f"{k} = ?" for k in kwargs]
   parameters = ", ".join(parameters)
   values = tuple(v for v in kwargs.values())
   values += (id, )

   sql = f''' UPDATE {table}
             SET {parameters}
             WHERE id = ?'''
   try:
       cur = conn.cursor()
       cur.execute(sql, values)
       conn.commit()
       print("OK")
   except sqlite3.OperationalError as e:
       print(e)

def delete_where(conn, table, **kwargs):
   qs = []
   values = tuple()
   for k, v in kwargs.items():
       qs.append(f"{k}=?")
       values += (v,)
   q = " AND ".join(qs)

   sql = f'DELETE FROM {table} WHERE {q}'
   cur = conn.cursor()
   cur.execute(sql, values)
   conn.commit()
   print("Deleted")

if __name__ == "__main__":
    item = ("długopis niebieski","2.09","10000")

    conn = create_connection("test_database.db")
    it_id = add_item(conn, item)

    order = (it_id, "1036", "2023-01-20","20","41.80")

    order_id = add_order(conn, order)

    print(it_id,order_id)
    conn.commit()
    update(conn, "orders", 1, suma="100")
    update(conn, "items", 1, cena="2.15")
    delete_where(conn, "orders", id=2)
   
select_all(conn, "orders")
select_where(conn, "items", cena="2.09")