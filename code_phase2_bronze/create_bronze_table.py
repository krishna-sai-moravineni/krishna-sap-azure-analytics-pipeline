import sqlite3 as sl

def create_table_bronze_watermark(cursor):
    sqlquery = (
                    """CREATE TABLE IF NOT EXISTS bronze_watermarks 
                       (
                        table_name VARCHAR(50) PRIMARY KEY,
                        last_watermark TIMESTAMP,
                        is_active bool
                       )
                    """
                )
    cursor.execute(sqlquery)


def create_table_customer_master(cursor):
    sqlquery = """CREATE TABLE IF NOT EXISTS customer_master (
                    bronze_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    customer_id VARCHAR(50),
                    customer_name VARCHAR(255),
                    city VARCHAR(100),
                    country VARCHAR(100),
                    load_timestamp TIMESTAMP,
                    source_file VARCHAR(255)
                  )"""
    cursor.execute(sqlquery)


def create_table_vendor_master(cursor):
    sqlquery = """CREATE TABLE IF NOT EXISTS vendor_master (
                    bronze_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    vendor_id VARCHAR(50),
                    vendor_name VARCHAR(255),
                    city VARCHAR(100),
                    country VARCHAR(100),
                    load_timestamp TIMESTAMP,
                    source_file VARCHAR(255)
                  )"""
    cursor.execute(sqlquery)


def create_table_material_master(cursor):
    sqlquery = """CREATE TABLE IF NOT EXISTS material_master (
                    bronze_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    material_id VARCHAR(50),
                    material_name VARCHAR(255),
                    material_group VARCHAR(100),
                    unit_price REAL,
                    load_timestamp TIMESTAMP,
                    source_file VARCHAR(255)
                  )"""
    cursor.execute(sqlquery)


def create_table_sales_order_header(cursor):
    sqlquery = """CREATE TABLE IF NOT EXISTS sales_order_header (
                    bronze_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    order_id VARCHAR(50),
                    customer_id VARCHAR(50),
                    order_date DATE,
                    order_status VARCHAR(50),
                    updatedatetime TIMESTAMP,
                    load_timestamp TIMESTAMP,
                    source_file VARCHAR(255)
                  )"""
    cursor.execute(sqlquery)


def create_table_sales_order_line(cursor):
    sqlquery = """CREATE TABLE IF NOT EXISTS sales_order_line (
                    bronze_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    order_id VARCHAR(50),
                    material_id VARCHAR(50),
                    item_number INTEGER,
                    quantity INTEGER,
                    amount REAL,
                    load_timestamp TIMESTAMP,
                    source_file VARCHAR(255)
                  )"""
    cursor.execute(sqlquery)


def create_table_finance_header(cursor):
    sqlquery = """CREATE TABLE IF NOT EXISTS finance_header (
                    bronze_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    posting_id VARCHAR(50),
                    vendor_id VARCHAR(50),
                    document_date DATE,
                    document_type VARCHAR(50),
                    updatedatetime TIMESTAMP,
                    load_timestamp TIMESTAMP,
                    source_file VARCHAR(255)
                  )"""
    cursor.execute(sqlquery)


def create_table_finance_line(cursor):
    sqlquery = """CREATE TABLE IF NOT EXISTS finance_line (
                    bronze_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    posting_id VARCHAR(50),
                    line_number INTEGER,
                    posting_key VARCHAR(50),
                    amount REAL,
                    load_timestamp TIMESTAMP,
                    source_file VARCHAR(255)
                  )"""
    cursor.execute(sqlquery)