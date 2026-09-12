import pandas as pd
import sqlite3 as sl
import os
import datetime

# Function: Connect to Database for the given filepath
def connect_to_db(db_path):
    connection = sl.connect(database = db_path)
    return connection

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


connection.close()

