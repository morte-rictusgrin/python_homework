
import sqlite3
import pandas as pd

# Task 1: Complex JOINs with Aggregation

with  sqlite3.connect("../db/lesson.db") as conn: ##connecting to database
    cursor = conn.cursor()
    ##########################################################################
    ## SQL statement: SELECT -- show these data -- order_id from orders     ## 
    ## table (alias o) and total_price of all items in every order          ##
    ## calculated as SUM of price value from products table (alias p)       ##
    ## times number of product items purchased taken from line_items table  ##
    ## (li). Taking data from orders table (shortened to o) joined by two   ##
    ## tables: line_items (alias li) correlated by order_id and from        ##
    ## products table correlated by product_id. Make the output grouped by  ##
    ## order_id and ordered by order_id. Limiting output to first 5 rows    ##
    ##########################################################################
    sql_statement = """SELECT 
                            o.order_id,
                            SUM(p.price * li.quantity) AS total_price
                        FROM orders o
                        JOIN line_items li ON o.order_id = li.order_id
                        JOIN products p ON li.product_id = p.product_id
                        GROUP BY o.order_id
                        ORDER BY o.order_id
                        LIMIT 5"""
    try:
        cursor.execute(sql_statement)                   
        results = cursor.fetchall() # fetching results
        print(f"Task 1:\n\nOrder ID | Total Price\n{'-' * 23}")    # printing output table header    
        for row in results:   
            # allocating 8 symbols for the first row width, allign right
            # second row: making result float and limiting to 2 decimal places.
            print(f"{row[0]:>8} | ${row[1]:.2f}")        
    except Exception as e:
        print("Error:", e)


# Task 2: Understanding Subqueries

with  sqlite3.connect("../db/lesson.db") as conn: ##connecting to database
    cursor = conn.cursor()
    sql_statement = """
    SELECT
        c.customer_name,
        IFNULL(AVG(order_totals.total_price), 0) AS average_total_price
    FROM customers c
    LEFT JOIN (
        SELECT 
            o.customer_id AS customer_id_b,
            SUM(p.price * li.quantity) AS total_price
        FROM orders o
        JOIN line_items li ON o.order_id = li.order_id
        JOIN products p ON li.product_id = p.product_id
        GROUP BY o.order_id
    ) AS order_totals ON c.customer_id = order_totals.customer_id_b
    GROUP BY c.customer_id, c.customer_name
    ORDER BY c.customer_id
"""
    try:
        cursor.execute(sql_statement)                   
        results = cursor.fetchall() # fetching results
        print(f"\nTask 2:\n\n{'Customer Name':<14} | Average price per order\n{'-' * 40}")    # printing output table header    
        for row in results:   
            # allocating 30 symbols for the first row width, allign right
            # second row: making result float and limiting to 2 decimal places.
            print(f"{row[0]:<30} | ${row[1]:.2f}")        
    except Exception as e:
        print("Error:", e)

# Task 3: An Insert Transaction Based on Data

with  sqlite3.connect("../db/lesson.db") as conn: # connecting to database
    conn.execute("PRAGMA foreign_keys = 1") # allowing foreign key
    cursor = conn.cursor()
    print("\n\nTask 3\n")

    try:
        # Step 1: geting customer_id for "Perez and Sons"
        customer_name = "Perez and Sons"
        cursor.execute("""
            SELECT customer_id 
            FROM customers 
            WHERE customer_name = ?
        """, (customer_name,))
        result = cursor.fetchone()
        if not result:
            print(f"\nCustomer '{customer_name}' not found!\n")
            raise Exception("Customer not found")
        customer_id = result[0]
        print(f"\nCustomer ID: {customer_id}\n")

        # Step 2: getting employee_id for Miranda Harris
        employee_first = "Miranda"  
        employee_last = "Harris"   
        cursor.execute("""
            SELECT employee_id 
            FROM employees 
            WHERE first_name = ? AND last_name = ?
        """, (employee_first, employee_last))
        result = cursor.fetchone()
        if not result:
            print(f"\nEmployee '{employee_first} {employee_last}' not found!\n")
            raise Exception("Employee not found")
        employee_id = result[0]
        print(f"\nEmployee ID: {employee_id}\n")

        # Step 3: getting 5 least expensive products from products
        cursor.execute("""
            SELECT product_id 
            FROM products 
            ORDER BY price ASC 
            LIMIT 5
        """)
        products = cursor.fetchall()
        product_ids = [row[0] for row in products]
        print(f"\nProduct IDs: {product_ids}\n")

        # Step 4: Create order record and get the order_id
        cursor.execute("""
            INSERT INTO orders (customer_id, employee_id, date)
            VALUES (?, ?, DATE('now'))
            RETURNING order_id
        """, (customer_id, employee_id))
        order_id = cursor.fetchone()[0]
        print(f"\nCreated Order ID: {order_id}\n")

        # Step 5: Create line_item records for each product (10 of each)
        for product_id in product_ids:
            cursor.execute("""
                INSERT INTO line_items (order_id, product_id, quantity)
                VALUES (?, ?, 10)
            """, (order_id, product_id))
        print(f"\nCreated {len(product_ids)} line items\n")

        conn.commit()
        print("Transaction committed successfully.")

        # Step 6: printing order details
        cursor.execute("""
            SELECT 
                li.line_item_id,
                li.quantity,
                p.product_name
            FROM line_items li
            JOIN products p ON li.product_id = p.product_id
            WHERE li.order_id = ?
            ORDER BY li.line_item_id
        """, (order_id,))
        
        results = cursor.fetchall()
        
        print(f"\n\nOrder Details for Order #{order_id}\n")
        print(f"\n{'Line Item ID':<15} | {'Quantity':<10} | Product Name")
        print("-" * 60)
        for row in results:
            print(f"{row[0]:<15} | {row[1]:<10} | {row[2]}")
    except Exception as e:
        conn.rollback()
        print(f"Error occurred: {e}")
        print("Transaction rolled back.")


# Task 4: Aggregation with HAVING

with sqlite3.connect("../db/lesson.db") as conn:
    conn.execute("PRAGMA foreign_keys = 1") # allowing foreign key
    cursor = conn.cursor()

    try:
        cursor.execute("""
            SELECT e.first_name, e.last_name, 
            COUNT(o.order_id) AS num_orders 
            FROM employees e 
            JOIN orders o 
            ON e.employee_id = o.employee_id 
            GROUP BY e.employee_id, e.first_name, e.last_name 
            HAVING num_orders > 5
        """)
        results = cursor.fetchall()
        print(f"\nTask 4\n\nEmployees with more than 5 orders:\n")
        print(f"\n{'Employee first name':<15} | {'Employee last name':<10} | Number of orders")
        print("-" * 59)
        for row in results:
            print(f"{row[0]:<19} | {row[1]:<18} | {row[2]}")
    except Exception as e:
        conn.rollback()
        print(f"Error occurred: {e}")


    
