# main.py

import sqlite3
from faker import Faker
import random

# connect to the db
conn = sqlite3.connect('customer_db.db')
cur = conn.cur()

# create a database table
cur.execute('''CREATE TABLE customers (
                  customerID INTEGER PRIMARY KEY,
                  name TEXT,
                  city TEXT,
                  email TEXT,
                  num_orders INTEGER,
                  discount INTEGER DEFAULT 2)''')


# create a Faker object 
fake = Faker()
Faker.seed(42)

for _ in range(15):
    name = fake.name()
    city = fake.city()
    d = fake.domain_name()
    email = f"{name[:2]}.{city[:2]}@{d}"
    num_orders = random.choice(range(200))
    db_cursor.execute('INSERT INTO customers (name, city, email, num_orders) \
    VALUES (?,?,?,?)', (name,city,email,num_orders))

# commit the transaction 
conn.commit()
cur.close()
conn.close()
