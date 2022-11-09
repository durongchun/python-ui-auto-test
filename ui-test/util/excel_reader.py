# coding: utf8
import os

import pandas as pd
import pytest


class ExcelData(object):
    def __init__(self, data_path, sheetname):
        self.list_dic = []
        self.data_path = data_path
        self.sheetname = sheetname

    def get_xls(self, data_path):  # xls_name填写用例的Excel名称 sheet_name该Excel的sheet名称
        # 获取用例文件路径
        ex_data = pd.read_excel(data_path)  # 默认读取第一个sheet的内容
        head_list = list(ex_data.columns)  # 拿到表头: [A, B, C, D]

        for i in ex_data.values:  # i 为每一行的value的列表：[a2, b2, c2, d2]
            a_line = dict(zip(head_list, i))  # a_line: {"A": "a2", "B": "b2", "C": "c2", "D": "d2"}
            self.list_dic.append(a_line)
        print(self.list_dic)

        return self.list_dic

    @staticmethod
    def get_datas():
        file_path = os.path.abspath(__file__)
        parent_path = os.path.dirname(file_path)
        parent2_path = os.path.dirname(parent_path)

        data_path = parent2_path + "\\data\\excel_data\\test_data_erp.xlsx"
        sheetname = "test_warehouse"
        get_data = ExcelData(data_path, sheetname)
        datas = get_data.get_xls(data_path)

        return datas

# if __name__ == "__main__":
#     file_path = os.path.abspath(__file__)
#     parent_path = os.path.dirname(file_path)
#     parent2_path = os.path.dirname(parent_path)
#
#     data_path = parent2_path + "\\data\\excel_data\\test_data_erp.xlsx"
#     sheetname = "test_warehouse"
#     get_data = ExcelData(data_path, sheetname)
#     datas = get_data.get_xls(data_path)
