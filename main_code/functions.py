import sqlite3

# Function to create tables
def create_tables():
    with sqlite3.connect('store.db') as conn:
        cursor = conn.cursor()
        with open('schemas.sql', 'r') as schema_file:
            schema = schema_file.read()
            cursor.executescript(schema)
        conn.commit()

# Function to add a new gadget
def add_product(name, category, price):
    with sqlite3.connect("store.db") as cucu:
        cursor = cucu.cursor()
        cursor.execute("INSERT INTO products (name, category, price) VALUES (?, ?, ?)", (name, category, price))
        cucu.commit()

# Function to add a new customer
def add_customer(first_name, last_name, email):
    with sqlite3.connect("store.db") as cucu:
        cursor = cucu.cursor()
        cursor.execute("INSERT INTO customers (first_name, last_name, email) VALUES (?, ?, ?)", (first_name, last_name, email))
        cucu.commit()

# Function to add a new order
def add_order(customer_id, product_id, quantity, order_date):
    with sqlite3.connect("store.db") as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO orders (customer_id, product_id, quantity, order_date) VALUES (?, ?, ?, ?)", (customer_id, product_id, quantity, order_date))
        conn.commit()

# Function to show total sales volume
def total_sales_volume():
    with sqlite3.connect('store.db') as cucu:
        cursor = cucu.cursor()
        cursor.execute('''
            SELECT SUM(products.price * orders.quantity) AS total_sales
            FROM orders
            INNER JOIN products ON orders.product_id = products.product_id;
            ''')
        total_sales = cursor.fetchone()[0]
        print(f"Total sales volume: {total_sales}")

# Function to show total sales volume
def orders_per_customer():
    with sqlite3.connect('store.db') as cucu:
        cursor = cucu.cursor()
        cursor.execute('''
            SELECT customers.first_name, customers.last_name, COUNT(orders.order_id) AS order_count
            FROM customers
            INNER JOIN orders ON customers.customer_id = orders.customer_id
            GROUP BY customers.customer_id;
            ''')
        results = cursor.fetchall()
        for row in results:
            print(f"Customer: {row[0]} {row[1]}, Number of orders: {row[2]}")

# Funtion to show average order check
def average_order_check():
    with sqlite3.connect('store.db') as cucu:
        cursor = cucu.cursor()
        cursor.execute('''
            SELECT AVG(products.price * orders.quantity) AS average_check
            FROM orders
            INNER JOIN products ON orders.product_id = products.product_id;
        ''')
        avg_check = cursor.fetchone()[0]
        print(f"Average order check: {avg_check}")

# Function to show the most popular products category
def most_popular_category():
    with sqlite3.connect('store.db') as cucu:
        cursor = cucu.cursor()
        cursor.execute('''
            SELECT category, MAX(order_count) 
            FROM (
                SELECT products.category, COUNT(orders.order_id) AS order_count
                FROM orders
                INNER JOIN products ON orders.product_id = products.product_id
                GROUP BY products.category
            );
        ''')
        result = cursor.fetchone()
        print(f"Most popular category: {result[0]} with {result[1]} orders.")

# Function to show total products in each category
def total_products_per_category():
    with sqlite3.connect('store.db') as cucu:
        cursor = cucu.cursor()
        cursor.execute('''
            SELECT category, COUNT(product_id) AS total_products
            FROM products
            GROUP BY category;
        ''')
        results = cursor.fetchall()
        for row in results:
            print(f"Category: {row[0]}, total products in {row[0]}: {row[1]}")

# Function to update prices in "Phones" category
def update_phone_prices():
    with sqlite3.connect('store.db') as cucu:
        cursor = cucu.cursor()
        cursor.execute('''
            UPDATE products
            SET price = price * 1.10
            WHERE category = 'phones';
        ''')
        cucu.commit()
        print("Prices updated in \"Phones\" category. If it even exists.")