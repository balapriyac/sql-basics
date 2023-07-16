# imports
import sqlite3
from faker import Faker
import random

# connect to the db
db_conn = sqlite3.connect('customer_db.db')
db_cursor = db_conn.cursor()

# create table
db_cursor.execute('''CREATE TABLE customers (
                  id INTEGER PRIMARY KEY,
                  name TEXT,
                  email TEXT,
                  city TEXT,
                  job TEXT,
                  num_orders INTEGER)''')


# create and insert records
fake = Faker()
Faker.seed(20)


for _ in range(15):
    name = fake.name()
    domain = fake.domain_name()
    city = fake.city()
    email = f"{name[:2]}{city}@{domain}"
    job = fake.job()
    num_orders = random.choice(range(200))
    db_cursor.execute('INSERT INTO customers (name, email, city, job, num_orders) VALUES (?,?,?,?,?)', (name,email,city,job,num_orders))

# commit the transaction and close the cursor and db connection
db_conn.commit()
db_cursor.close()
db_conn.close()
