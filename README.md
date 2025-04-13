Kurriku Keebs: Mechanical Keyboard Shop GUI

This desktop GUI app manages the keyboard shop's database.
Built using Python, Tkinter, and SQlite.

---------

Schema:
- Customers       (customer_id PK, first_name, last_name, email)
- Employees       (employee_id PK, first_name, last_name, position)
- Products        (product_id PK, name, category, price)
- Transactions    (trans_id PK, customer_id FK, employee_id FK, trans_date, item_total, total_amount)
- Purchase_items  (p_i_id PK, trans_id FK, product_id FK, sale_price)

Predefined reports: (predifined SQL queries)
- Display transactions and their info. for a selected customer (JOIN transactions and employees for name)
- Display products previously purchased by customer (JOIN purchased_products and products)

files:
- 'app.py' (Python GUI using Tkinter)
- 'create.sql' (Creates tables with constraints)
- 'insert.sql' (Inserts data into tables)
- 'crud.sql' (Performs CRUD operations)
- 'README.md'

---------

How to run:

clone repo
git clone https://github.com/rmakoto77/kurriku-keebs
cd project1

run GUI
python app.py