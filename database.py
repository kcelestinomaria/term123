import sqlite3
from typing import List
import datetime
from model import Product


conn = sqlite3.connect('product.db')
c = conn.cursor()


def create_table():
    c.execute("""CREATE TABLE IF NOT EXISTS products (
        product text,
        category text,
        date_added text,
        date_buy text,
        status integer,
        position integer
    )""")

create_table()


def insert_product(product: Product):
    c.execute('select count(*) FROM products')
    count = c.fetchone()[0]
    product.position = count if count else 0
    with conn: # parameter substitution below is what prevents SQL INJECTION Attacks
        c.execute('INSERT INTO products VALUES (:product, :category, :date_added, :date_buy, :status, :position)' ,
        {'product': product.product, 'category': product.category, 'date_added': product.date_added, 
        'date_buy': product.date_buy, 'status': product.status, 'position': product.position })


def get_all_products() -> List[Product]:
    c.execute('select * from products')
    results = c.fetchall()
    products = []
    for result in results:
        products.append(Product(*result))
    return products


def delete_product(position):
    c.execute('select count(*) from products')
    count = c.fetchone()[0]

    with conn: # conn -> context manager
        c.execute("DELETE from products WHERE position=:position", {"position": position})
        for pos in range(position+1, count):
            change_position(pos, pos-1, False)

def change_position(old_position: int, new_position: int, commit=True):
    c.execute('UPDATE products SET position = :position_new WHERE positon = :position_old',
    {'position_old': old_position, 'position_new': new_position})

    if commit:
        conn.commit()


def update_product(position: int, product: str, category: str):
    with conn:
        if product is not None and category is not None:
            c.execute('UPDATE products SET products = :product, category = :category WHERE position = :position',
            {'position': position, 'product': product, 'category': category})
        elif product is not None:
            c.execute('UPDATE products SET task = :product WHERE position = :position',
            {'position': position, 'product': product})
        elif category is not None:
            c.execute('UPDATE products SET category = :category WHERE position = :position',
            {'position': position, 'category': category})

def buy_product(position: int):
    with conn:
        c.execute('UPDATE products SET status = 2, date_buy = :date_buy WHERE position = :position',
        {'position': position, 'date_buy': datetime.datetime.now().isoformat()})

