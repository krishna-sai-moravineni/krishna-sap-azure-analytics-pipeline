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


def 