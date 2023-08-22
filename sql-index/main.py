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
                  first_name TEXT,
                  last_name TEXT,
                  city TEXT,
                  num_orders INTEGER)''')

# create a Faker object
fake = Faker()
Faker.seed(27)

# create and insert 1 million records
num_records = 1_000_000

for _ in range(num_records):
    first_name = fake.first_name()
    last_name = fake.last_name()
    city = fake.city()
    num_orders = random.randint(0,100)
    db_cursor.execute('INSERT INTO customers (first_name, last_name, city, num_orders) VALUES (?,?,?,?)', (first_name, last_name, city, num_orders))

# commit the transaction and close the cursor and connection
db_conn.commit()
db_cursor.close()
db_conn.close()

