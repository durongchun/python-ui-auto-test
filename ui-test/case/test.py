import unittest

import pytest
import uuid


from selenium import webdriver
from selenium.common.exceptions import TimeoutException


class TestClass:

    @staticmethod
    def test_convert_data():
        result_lit = []
        test_data = [{'UserName': 'lucy.du@holinova.com', 'PassWord': 'durongchun123~'},
                     {'UserName': 'lucy.du@holinova.com', 'PassWord': 'durongchun123~'}]
        for data in test_data:
            result_lit.append(tuple(data.values()))

        print(result_lit)


if __name__ == "__main__":
    # 使用 unittest 依次执行当前模块中 test 打头的方法
    unittest.main()

