import sqlite3
import pandas as pd

with sqlite3.connect("../db/lesson.db") as conn:
    conn.execute("PRAGMA foreign_keys = 1")
    cursor = conn.cursor()

    try:

        order_id = 250

        # Step 1: Delete line_items for this order
        cursor.execute(
            """
            DELETE FROM line_items 
            WHERE order_id = ?
        """,
            (order_id,),
        )
        line_items_deleted = cursor.rowcount
        print(f"Deleted {line_items_deleted} line items")

        # Step 2: Delete the order
        cursor.execute(
            """
            DELETE FROM orders 
            WHERE order_id = ?
        """,
            (order_id,),
        )
        orders_deleted = cursor.rowcount
        print(f"Deleted {orders_deleted} order(s)")

        # Commit the deletion
        conn.commit()
        print("Deletion successful!")

    except Exception as e:
        conn.rollback()
        print(f"Error: {e}")
        print("Deletion rolled back.")
