import sqlite3 as sl
import pandas as pd
import os
import datetime
import table_utils_bronze_watermark

local_timestamp = datetime.datetime.now().isoformat(timespec="seconds")


def load_table_dimension_type(csv_path, table_name, connection):
    df_table = pd.read_csv(csv_path)
    df_table["load_timestamp"] = local_timestamp
    df_table["source_file"] = csv_path

    df_table.to_sql(
        name=table_name,
        con=connection,
        if_exists="append",
        index=False
    )


def load_table_fact_type(csv_path_header, table_name_header, csv_path_line, table_name_line, key_column, connection):

    # define local variables
    local_cursor = connection.cursor()
    watermark_data = table_utils_bronze_watermark.get_bronze_watermark(cursor=local_cursor, table_name=table_name_header)
    if watermark_data:
        local_watermark = pd.to_datetime(watermark_data[0][1])
    else:
        local_watermark = None

    # header table processing
    df_header_table = pd.read_csv(csv_path_header)
    df_header_table["load_timestamp"] = local_timestamp
    df_header_table["source_file"] = csv_path_header

    df_header_table["updatedatetime"] = pd.to_datetime(df_header_table["updatedatetime"])

    if local_watermark is None:
        filter_df = df_header_table
    else:
        filter_df = df_header_table[df_header_table["updatedatetime"] >= local_watermark]

    filter_df.to_sql(
        name=table_name_header,
        con=connection,
        if_exists="append",
        index=False
    )

    changed_key_column_data = filter_df[key_column].to_list()

    # line table processing
    df_line_table = pd.read_csv(csv_path_line)
    df_line_table["load_timestamp"] = local_timestamp
    df_line_table["source_file"] = csv_path_line

    filter_line_df = df_line_table[df_line_table[key_column].isin(changed_key_column_data)]

    filter_line_df.to_sql(
        name=table_name_line,
        con=connection,
        if_exists="append",
        index=False
    )

    table_utils_bronze_watermark.create_update_bronze_watermark(cursor=local_cursor, table_name=table_name_header, timestamp=local_timestamp, is_active=True)
