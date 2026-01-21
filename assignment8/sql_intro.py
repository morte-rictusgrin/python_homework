import sqlite3
import pandas as pd

## Task 2: Defining Database Structure: 

def add_publisher(cursor, publisher_name):
    try:
        cursor.execute("INSERT INTO publishers (publisher_name) VALUES (?)", (publisher_name,))
    except sqlite3.IntegrityError:
        print(f"{publisher_name} is already in the database.")


def add_magazine(cursor, magazine_name, publisher_id):
    cursor.execute("SELECT * FROM publishers WHERE publisher_id = ?", (publisher_id,))
    results = cursor.fetchall()
    if len(results) > 0:
        pass
    else:
        print(f"There is no publisher with ID {publisher_id}.")
        return
    try:
        cursor.execute("INSERT INTO magazines (magazine_name, publisher_id) VALUES (?,?)", (magazine_name, publisher_id))
    except sqlite3.IntegrityError:
        print(f"{magazine_name} is already in the database.")


def add_subscriber(cursor, subscriber_name, subscriber_address):
    cursor.execute("SELECT * FROM subscribers WHERE subscriber_name = ? AND subscriber_address = ?", (subscriber_name, subscriber_address))
    results = cursor.fetchall()    
    if len(results) > 0:
        print(f"\n\n{subscriber_name} with {subscriber_address} already exists!")
        return        
    try:
        cursor.execute("INSERT INTO subscribers (subscriber_name, subscriber_address) VALUES (?,?)", (subscriber_name, subscriber_address))
    except sqlite3.IntegrityError:
        print(f"{subscriber_name} is already in the database.")

def subscriptions(cursor, subscriber_name, magazine_name, expiration_date): # Adding subscriptions
    
    cursor.execute("SELECT * FROM subscribers WHERE subscriber_name = ?", (subscriber_name,))
    results = cursor.fetchall()
    if len(results) > 0:
        subscriber_id = results[0][0]
    else:
        print(f"There was no subscriber named {subscriber_name}.")
        return
    cursor.execute("SELECT * FROM magazines WHERE magazine_name = ?", (magazine_name,))
    results = cursor.fetchall()
    if len(results) > 0:
        magazine_id = results[0][0]
    else:
        print(f"There was no magazine named {magazine_name}.")
        return
    cursor.execute("SELECT * FROM subscriptions WHERE subscriber_id = ? AND magazine_id = ?", (subscriber_id, magazine_id))
    results = cursor.fetchall()
    if len(results) > 0:
        print(f"Subscriber {subscriber_name} is already subscribed to {magazine_name}.")
        return
    cursor.execute("INSERT INTO subscriptions (subscriber_id, magazine_id, expiration_date) VALUES (?, ?, ?)", (subscriber_id, magazine_id, expiration_date))


## Task 1: Creating database

with sqlite3.connect("../db/magazines.db") as conn:                             ## creating new database
    conn.execute("PRAGMA foreign_keys = 1")                                     ## permitting foreign keys
    print("Database created and connected successfully.")
    cursor = conn.cursor()                                                      ## defining function
    

    # Create tables                                                             ## creating tables and defining their structure
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS publishers (                                     
        publisher_id INTEGER PRIMARY KEY,
        publisher_name TEXT NOT NULL UNIQUE
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS magazines (
        magazine_id INTEGER PRIMARY KEY,
        magazine_name TEXT NOT NULL UNIQUE,
        publisher_id INTEGER NOT NULL,
        FOREIGN KEY (publisher_id) REFERENCES publishers (publisher_id)
            ON DELETE CASCADE
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS subscribers (
        subscriber_id INTEGER PRIMARY KEY,
        subscriber_name TEXT NOT NULL,
        subscriber_address TEXT NOT NULL
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS subscriptions (
        subscription_id INTEGER PRIMARY KEY,
        subscriber_id INTEGER NOT NULL,
        magazine_id INTEGER NOT NULL,           
        expiration_date TEXT NOT NULL,
        FOREIGN KEY (subscriber_id) REFERENCES subscribers (subscriber_id)
            ON DELETE CASCADE,
        FOREIGN KEY (magazine_id) REFERENCES magazines (magazine_id)
            ON DELETE CASCADE,
        UNIQUE (subscriber_id, magazine_id)
    )
    """)

    print("Tables created successfully.")
    conn.commit()

## Task 3: Populate Tables with Data:

with sqlite3.connect("../db/magazines.db") as conn:                             ## connecting to db
    conn.execute("PRAGMA foreign_keys = 1")                                     ## permitting foreign keys
    cursor = conn.cursor()

    # Insert sample data into tables

    add_publisher(cursor, "TSR")  
    add_publisher(cursor, "WotC")
    add_publisher(cursor, "Black Library")
    
    add_magazine(cursor, "Planescape", 1)
    add_magazine(cursor, "Vecna", 2)
    add_magazine(cursor, "Eisenhorn", 3)

    add_subscriber(cursor, "Alice", "555, Test street, New York, NY, 444333")
    add_subscriber(cursor, "Kirk", "444, Vecna ave, Mezz, OK, 123456")
    add_subscriber(cursor, "Malcador", "40000, Machine crt, WH, 132445")
	
    subscriptions(cursor, "Alice", "Planescape", "10.09.2026")
    subscriptions(cursor, "Kirk", "Planescape", "10.11.2026")
    subscriptions(cursor, "Kirk", "Vecna", "10.09.2026")
    subscriptions(cursor, "Malcador", "Planescape", "12.09.2028")
    subscriptions(cursor, "Malcador", "Eisenhorn", "10.01.2026")
    
    conn.commit()

## Task 4: SQL Queries 

with sqlite3.connect("../db/magazines.db") as conn:                             ## connecting to database
    print("Connected to database.")
    cursor = conn.cursor()                                                      
    cursor.execute("SELECT * FROM subscribers")
    result = cursor.fetchall()
    print(f"\n\nThe list of subscribers:\n\n")
    for row in result:
        print(row)
    
    cursor.execute("SELECT * FROM magazines ORDER BY magazine_name ASC")
    result = cursor.fetchall()
    print(f"\n\nAll the magazines sorted alphabetically:\n\n")
    for row in result:
        print(row)   

    cursor.execute("SELECT m.magazine_name FROM magazines m JOIN publishers p ON m.publisher_id = p.publisher_id WHERE p.publisher_name = 'TSR'")
    result = cursor.fetchall()
    print(f"\n\nMagazines published by TSR:\n\n") 
    for row in result:
        print(row)   

