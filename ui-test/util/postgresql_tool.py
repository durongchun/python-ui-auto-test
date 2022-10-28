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
                                           database='ods')
        return self.connection

    # execute 任何操作
    def execute(self, sql):
        """
        执行 sql 语句
        :param sql: sql 语句
        :return: select 语句返回
        """
        # 从 postgresql 连接中获取一个游标对象
        cursor = self.connection.cursor()
        # sql 语句执行返回值
        ret = None
        try:
            # 执行 sql 语句
            ret = cursor.execute(sql)
            # 提交
            self.connection.commit()
        except Exception as e:
            # 异常回滚数据
            self.connection.rollback()
        # 关闭游标
        cursor.close()
        # 返回
        return format(ret)

    # write db
    @staticmethod
    def write_to_db(conn, data_tuple):
        try:
            # Connect to an existing database
            # self.connection = psycopg2.connect(user='ods',
            #                                    password='ods',
            #                                    host='127.0.0.1',
            #                                    port=5432,
            #                                    database='ods')
            #
            cursor = conn.cursor()

            cursor.execute("SELECT * from ods.ods_inventory_summary")  # Fetch result
            record = cursor.fetchone()
            print("查询记录= ", record, "\n")

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
                # self.connection.close()
                print("PostgreSQL cursor is closed")

    # write_to_db_stock_quantity
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

    # clean table
    @staticmethod
    def clear_ods_data(cursor, conn):
        try:
            # Executing a SQL query to delete data
            # cursor = conn.cursor
            insert_query = """ DELETE FROM public.ods_stock_quant """
            cursor.execute(insert_query)
            conn.commit()

        except (Exception, Error) as error:
            print("Error while connecting to PostgreSQL", error)
        finally:
            if conn and cursor:
                cursor.close()
        #         # self.conn.close()
        #         print("PostgreSQL connection is closed")

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
