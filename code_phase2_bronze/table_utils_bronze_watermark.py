import sqlite3 as sl

def get_bronze_watermark(cursor, table_name):
    sqlquery = f"SELECT * FROM bronze_watermarks where table_name = ?"
    cursor.execute(sqlquery, (table_name,))
    result = cursor.fetchall()
    return result


def create_update_bronze_watermark(cursor, table_name, timestamp, is_active):  
    upsert_query = """INSERT INTO bronze_watermarks (table_name, last_watermark, is_active)
                     VALUES (?, ?, ?)
                     ON CONFLICT(table_name)
                     DO UPDATE SET last_watermark = ?,
                                   is_active = ?"""

    try:
        cursor.execute(upsert_query, (table_name, timestamp, is_active, timestamp, is_active))
        return True
        
    except sl.Error as er:
        print(f"Upsert 'bronze_watermark' Exception: {er}")
        return False


def soft_delete_bronze_watermark(cursor, table_name, timestamp):
    delete_query = """UPDATE bronze_watermarks
                      SET last_watermark = ?,
                          is_active = False
                      WHERE table_name = ?
                    """
    try:
        cursor.execute(delete_query, (timestamp, table_name))
        return True
    except sl.Error as er:
        print(f"Soft Delete 'bronze_watermark' Excetion: {er}")
        return False