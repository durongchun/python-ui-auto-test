#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : abcnull
# @Time : 2019/12/2 17:37
# @E-Mail : abcnull@qq.com
# @CSDN : abcnull
# @GitHub : abcnull
from aifc import Error
from datetime import datetime

import psycopg2 as psycopg2
import pymysql as pymysql

from util.config_reader import ConfigReader


# PostgreSQL 连接工具
class PostgreSQLTool:
    # 初始化 postgresql 连接
    def __init__(self):
        self.summary_date = None
        self.vars = {}
        self.db_url = '38.88.127.10:43819'
        self.db_port = 5432
        self.db_name = 'ods'
        self.db_user = 'ods'
        self.db_passwd = 'zzz@1234'
        self.connection = None

        try:
            self.connection = psycopg2.connect(user=self.db_user,
                                               password=self.db_passwd,
                                               host=self.db_url,
                                               port=self.db_port,
                                               database=self.db_name)

        except (Exception, Error) as error:
            print("Error while connecting to PostgreSQL", error)

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
    def write_to_db(self, data_tuple):
        try:
            # insert data
            cursor = self.connection.cursor()

            # Executing a SQL query to insert data into  table
            insert_query = """ INSERT INTO ods_inventory_summary (sku_id, product_id, product_name, active, 
            pool, count, threshold, avail_qty,source,warehouse,product_size, vintage, summary_date, update_time) 
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) ON CONFLICT ON CONSTRAINT 
            ods_stock_summary_unique DO NOTHING"""
            cursor.execute(insert_query, data_tuple)
            self.connection.commit()

        except (Exception, Error) as error:
            print("Error while connecting to PostgreSQL", error)

        finally:
            if self.connection and cursor:
                cursor.close()

    # clean table
    def clear_summary_of_same_date(self, summary_date, source):
        self.summary_date = datetime.datetime.now().date()
        try:
            cursor = self.connection.cursor()

            # Executing a SQL query to delete data
            insert_query = """ DELETE FROM ods_inventory_summary where source = %s and summary_date = %s"""
            cursor.execute(insert_query, (source, summary_date))
            self.connection.commit()

        except (Exception, Error) as error:
            print("Error while connecting to PostgreSQL", error)

        finally:
            if self.connection and cursor:
                cursor.close()

    # 获取 PostgreSQL 连接
    def get_mysql_conn(self):
        return self.self.connection

    # PostgreSQL 连接释放
    def release_mysql_conn(self):
        if self.connection:
            self.connection.close()
            print("PostgreSQL connection is closed")

        self.driver.close()
        self.driver.quit()
