#!/usr/bin/env python
# -*- coding: utf-8 -*-
from aifc import Error
import psycopg2 as psycopg2


# PostgreSQL 连接工具
class PostgreSQLTool:
    # 初始化 postgresql 连接    
    def __init__(self):
        self.summary_date = None
        self.vars = {}
        # self.db_url = '127.0.0.1'
        # self.db_port = 5432
        # self.db_name = 'ods'
        # self.db_user = 'ods'
        # self.db_passwd = 'ods'
        self.connection = None

    # connect to db
    def get_connection(self):
        self.connection = psycopg2.connect(user='qauser',
                                           password='oc575vtude',
                                           host='23.16.247.137',
                                           port=5432,
                                           database='stagingods')
        return self.connection

    # write db
    @staticmethod
    def write_to_db(conn, data_tuple):
        try:  #
            cursor = conn.cursor()
            # cursor.execute("SELECT * from public.ods_stock_quant")  # Fetch result
            # record = cursor.fetchone()
            # print("查询记录= ", record, "\n")
            insert_query = """INSERT INTO ods_inventory_summary (sku_id, product_id, product_name, active,
                        pool, count, threshold, avail_qty,source,warehouse,product_size, vintage, summary_date, update_time)
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
            cursor.execute(insert_query, data_tuple)
            conn.commit()
        except (Exception, Error) as error:
            print("Error while connecting to PostgreSQL", error)
        finally:
            if conn and cursor:
                cursor.close()
                print("PostgreSQL cursor is closed")

    # write_to_db_stock_quantity for Rust
    @staticmethod
    def write_to_db_stock_quantity_rust(conn, data_tuple):
        try:
            cursor = conn.cursor()
            insert_query = """INSERT INTO public.ods_stock_quant("source", product_code, product_name, product_id,
             company_name, location_name, warehouse_name, lot_serial, summary_date, quantity, 
             reserved_quantity, po_doc_num)                        
             VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
            cursor.executemany(insert_query, data_tuple)
            conn.commit()

        except (Exception, Error) as error:
            print("Error while connecting to PostgreSQL", error)
        finally:
            if conn and cursor:
                cursor.close()
        # write_to_db_stock_quantity for Rust

    @staticmethod
    def write_to_db_stock_quantity(conn, data_tuple):
        try:
            cursor = conn.cursor()
            insert_query = """INSERT INTO public.ods_stock_quant("source", product_code, product_name, product_id,
                company_name, location_name, warehouse_name, lot_serial, summary_date, quantity, 
                reserved_quantity)                        
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
            cursor.executemany(insert_query, data_tuple)
            conn.commit()

        except (Exception, Error) as error:
            print("Error while connecting to PostgreSQL", error)
        finally:
            if conn and cursor:
                cursor.close()

    # clean CW MTB data
    @staticmethod
    def clear_cw_mtb_data(cursor, conn):
        try:
            # Executing a SQL query to delete data
            insert_query = """ DELETE FROM public.ods_stock_quant WHERE company_name = 'CW-MtB'  """
            cursor.execute(insert_query)
            conn.commit()

        except (Exception, Error) as error:
            print("Error while connecting to PostgreSQL", error)
        finally:
            if conn and cursor:
                cursor.close()
        #         # self.conn.close()
        #         print("PostgreSQL connection is closed")

    # clean CW Rust data
    @staticmethod
    def clear_cw_rust_data(cursor, conn):
        try:
            # Executing a SQL query to delete data
            insert_query = """ DELETE FROM public.ods_stock_quant WHERE company_name = 'CW-Rust'  """
            cursor.execute(insert_query)
            conn.commit()

        except (Exception, Error) as error:
            print("Error while connecting to PostgreSQL", error)
        finally:
            if conn and cursor:
                cursor.close()
        #         # self.conn.close()
        #         print("PostgreSQL connection is closed")

    # clean DW data
    @staticmethod
    def clear_wd_data(cursor, conn):
        try:
            # Executing a SQL query to delete data
            insert_query = """ DELETE FROM public.ods_stock_quant WHERE source = 'WD'"""
            cursor.execute(insert_query)
            conn.commit()

        except (Exception, Error) as error:
            print("Error while connecting to PostgreSQL", error)
        finally:
            if conn and cursor:
                cursor.close()

    # 获取 PostgreSQL 连接
    def get_postgresql_conn(self):
        return self.connection

    # PostgreSQL 连接释放
    @staticmethod
    def release_postgresql_conn(conn, cursor):
        if conn and cursor:
            cursor.close()
            conn.close()
            print("PostgreSQL connection is closed")
