# coding: utf8
import os
import pandas as pd


class ExcelReader:

    @staticmethod
    def get_xls(data_path):  # xls_name填写用例的Excel名称 sheet_name该Excel的sheet名称
        # 获取用例文件路径
        ex_data = pd.read_excel(data_path, sheet_name="test_add_MtB", engine='openpyxl')  # 默认读取第一个sheet的内容
        head_list = list(ex_data.columns)  # 拿到表头: [A, B, C, D]
        list_dic = []

        for i in ex_data.values:  # i 为每一行的value的列表：[a2, b2, c2, d2]
            a_line = dict(zip(head_list, i))  # a_line: {"A": "a2", "B": "b2", "C": "c2", "D": "d2"}
            list_dic.append(a_line)

        print(tuple(list_dic))

        return list_dic

