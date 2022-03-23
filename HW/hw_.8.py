
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


def create_table(conn, sql):
    try:
        c = conn.cursor()
        c.execute(sql)
        c.close()
    except Error as e:
        print(e)


def insert_product(conn, product):
    try:
        sql = '''INSERT INTO products (product_title, price, quantity) 
        VALUES (?, ?, ?);'''
        c = conn.cursor()
        c.execute(sql, product)
        conn.commit()
        c.close()
    except Error as e:
        print(e)

def update_product_quantity(conn, quantity, id):
    try:
        sql = '''update products set quantity = ? where id = ?;'''
        c = conn.cursor()
        c.execute(sql, (quantity, id))
        conn.commit()
        c.close()
    except Error as e:
        print(e)


def update_product_price(conn, quantity, id):
    try:
        sql = '''update products set price = ? where id = ?;'''
        c = conn.cursor()
        c.execute(sql, (quantity, id))
        conn.commit()
        c.close()
    except Error as e:
        print(e)


def delete_product(conn, id):
    try:
        sql = '''delete from products where id = ?;'''
        c = conn.cursor()
        c.execute(sql, (id,))
        conn.commit()
        c.close()
    except Error as e:
        print(e)


def select_all_products(conn):
    try:
        sql = '''select * from products;'''
        c = conn.cursor()
        c.execute(sql)
        rows = c.fetchall()

        for row in rows:
            print(row)

        c.close()
    except Error as e:
        print(e)


def select_all_products_whose_price_and_quantity_bigger_than(conn, price, quantity):
    try:
        sql = '''select product_title, price, quantity from products where price <= ?;'''
        c = conn.cursor()
        c.execute(sql, (price,))
        c.execute(sql, (quantity,))
        rows = c.fetchall()

        for row in rows:
            print(row)

        c.close()
    except Error as e:
        print(e)


def search_by_name(conn):
    try:
        sql = '''select * from products  where product_title LIKE 'Onion';'''
        c = conn.cursor()
        c.execute(sql)
        rows = c.fetchall()

        for row in rows:
            print(row)

        c.close()
    except Error as e:
        print(e)


database = r'hw.db'
conn = create_connection(database)
sql_create_products_table = '''
CREATE TABLE products (
id INTEGER PRIMARY KEY AUTOINCREMENT,
product_title VARCHAR(200) NOT NULL,
price DOUBLE(10, 2) NOT NULL DEFAULT 0.0,
quantity INTEGER(5) NOT NULL DEFAULT 0
);
'''

if conn is not None:
    print('Successfully connected')

    create_table(conn, sql_create_products_table)
    # insert_product(conn, ('Onion', 100, 5))
    # insert_product(conn, ("Potato", 12, 10))
    # insert_product(conn, ("Tomato", 120, 7))
    # insert_product(conn, ("Sugar", 70, 10))
    # insert_product(conn, ("Flour", 100, 1))
    # insert_product(conn, ("Shampoo", 170, 2))
    # insert_product(conn, ("Pasta", 80, 3))
    # insert_product(conn, ("Oil", 85, 3))
    # insert_product(conn, ("Salt", 98, 3))

    update_product_quantity(conn, 10, 1)
    update_product_price(conn, 75.6, 6)
    delete_product(conn, 5)
    select_all_products(conn)
    select_all_products_whose_price_and_quantity_bigger_than(conn, 100, 5)



    conn.close()