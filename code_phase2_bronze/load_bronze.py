import pandas as pd
import sqlite3 as sl
import os
import datetime

# Function: Connect to Database for the given filepath
def connect_to_db(db_path):
    connection = sl.connect(database = db_path)
    return connection




# Function: Create database table for bronze_watermarks
def create_bronze_watermark(cursor):
    sqlquery = (
                 """CREATE TABLE IF NOT EXISTS bronze_watermarks (
                    table_name VARCHAR(50) PRIMARY KEY,
                    last_watermark TIMESTAMP 
                    )"""
                )
    cursor.execute(sqlquery)


# Function: Read Watermark (Last Updated Date time stamp) for the given table name
def read_watermark(cursor, table_name):
    sqlquery = f"SELECT * FROM bronze_watermarks where table_name = ?"
    cursor.execute(sqlquery, (table_name,))
    result = cursor.fetchall()
    return result
    


# Function: Create or Update Watermark for the given table name
def create_update_watermark(cursor, table_name, timestamp):
    check_query = """INSERT INTO bronze_watermarks (table_name, last_watermark)
                     VALUES (?, ?)
                     ON CONFLICT(table_name)
                     DO UPDATE SET last_watermark = ?"""

    try:
        cursor.execute(check_query, (table_name, timestamp, timestamp,))
        
    except sl.Error as er:
        print(f"Exception: {er}")


# Program execution path 

# Make a new folder (if not exist) inside data parent folder
os.makedirs(name="data/bronze/", exist_ok=True)

# Create a connection and assign to cursor
db_path_bronze = "data/bronze/bronze.db"

try:
    connection = connect_to_db(db_path=db_path_bronze)
    print(f"Successfully connected to: {db_path_bronze}")
    cursor = connection.cursor()

except sl.Error as er:
    print(f"Exception raised while connecting to '{db_path_bronze}': {er}")


create_bronze_watermark(cursor=cursor)

current_timestamp = datetime.datetime.now().isoformat(timespec="milliseconds")
table_name_customers = "customers"

create_update_watermark(cursor=cursor, table_name=table_name_customers, timestamp=current_timestamp)
connection.commit()

try:
    result = read_watermark(cursor=cursor, table_name=table_name_customers)
    #if result.count() != 0:
    for i in result:
        print(i)

    print(f"Number of rows in '{table_name_customers}':\n", result.__len__())

except sl.Error as er:
    print(f"Exception occured while reading '{table_name_customers}': {er}")

connection.close()

