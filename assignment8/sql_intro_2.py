import sqlite3
import pandas as pd
import os


## Task 5: Read Data into a DataFrame

with sqlite3.connect("../db/lesson.db") as conn:
    sql_statement = """SELECT l.line_item_id, l.quantity, l.product_id, p.product_name, p.price FROM line_items l JOIN products p ON l.product_id = p.product_id ;"""
    df = pd.read_sql_query(sql_statement, conn)
    print(f"\n\nFirst five rows of dataframe extracted from the database:\n\n{df.head(5)}\n\n")

    df['total'] = df['quantity'] * df['price'] ## Adding new column with total price
    print(f"\n\nFirst five rows of dataframe with added total column:\n\n{df.head(5)}\n\n")

    df = df.groupby('product_id').agg({'line_item_id': 'count', 'total': 'sum', 'product_name': 'first'}) ## grouping all products by product_id aggregating data

    print(f"\n\nFirst five rows of dataframe grouped:\n\n{df.head(5)}\n\n")

    df = df.sort_values(by='product_name',ascending=True) ## Sorting dataframe by product name

    print(f"\n\nFirst five rows of dataframe sorted by product name:\n\n{df.head(5)}\n\n")

    df.to_csv("order_summary.csv", sep=",", index=True, header=True, encoding=None) ## Saving dataframe to csv









