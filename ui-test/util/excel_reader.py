# coding: utf8
import os
import pandas as pd


class ExcelReader:

    @staticmethod
    def get_test_add_MtB_xls(data_path):  # xls_name填写用例的Excel名称 sheet_name该Excel的sheet名称
        # 获取用例文件路径
        ex_data = pd.read_excel(data_path, dtype=object, keep_default_na=False, sheet_name="test_add_MtB",
                                engine='openpyxl')
        head_list = list(ex_data.columns)  # 拿到表头: [A, B, C, D]
        list_dic = []

        for i in ex_data.values:  # i 为每一行的value的列表：[a2, b2, c2, d2]
            a_line = dict(zip(head_list, i))  # a_line: {"A": "a2", "B": "b2", "C": "c2", "D": "d2"}
            list_dic.append(a_line)

        print(tuple(list_dic))

        return list_dic

    @staticmethod
    def get_test_add_rust_xls(data_path):  # xls_name填写用例的Excel名称 sheet_name该Excel的sheet名称
        # 获取用例文件路径
        ex_data = pd.read_excel(data_path, dtype=object, keep_default_na=False, sheet_name="test_add_Rust",
                                engine='openpyxl')
        head_list = list(ex_data.columns)  # 拿到表头: [A, B, C, D]
        list_dic = []

        for i in ex_data.values:  # i 为每一行的value的列表：[a2, b2, c2, d2]
            a_line = dict(zip(head_list, i))  # a_line: {"A": "a2", "B": "b2", "C": "c2", "D": "d2"}
            list_dic.append(a_line)

        print(tuple(list_dic))

        return list_dic

    @staticmethod
    def get_test_delivery_orders_transfer_xls(data_path):  # xls_name填写用例的Excel名称 sheet_name该Excel的sheet名称
        # 获取用例文件路径
        ex_data = pd.read_excel(data_path, dtype=object, keep_default_na=False,
                                sheet_name="test_transfer_delivery_order",
                                engine='openpyxl')
        head_list = list(ex_data.columns)  # 拿到表头: [A, B, C, D]
        list_dic = []

        for i in ex_data.values:  # i 为每一行的value的列表：[a2, b2, c2, d2]
            a_line = dict(zip(head_list, i))  # a_line: {"A": "a2", "B": "b2", "C": "c2", "D": "d2"}
            list_dic.append(a_line)

        print(tuple(list_dic))

        return list_dic

    @staticmethod
    def get_test_internal_transfer_xls(data_path):  # xls_name填写用例的Excel名称 sheet_name该Excel的sheet名称
        # 获取用例文件路径
        ex_data = pd.read_excel(data_path, dtype=object, keep_default_na=False,
                                sheet_name="test_internal_transfer",
                                engine='openpyxl')
        head_list = list(ex_data.columns)  # 拿到表头: [A, B, C, D]
        list_dic = []

        for i in ex_data.values:  # i 为每一行的value的列表：[a2, b2, c2, d2]
            a_line = dict(zip(head_list, i))  # a_line: {"A": "a2", "B": "b2", "C": "c2", "D": "d2"}
            list_dic.append(a_line)

        print(tuple(list_dic))

        return list_dic
