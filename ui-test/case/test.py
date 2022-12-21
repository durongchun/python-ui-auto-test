import unittest

import pytest
import uuid


from selenium import webdriver
from selenium.common.exceptions import TimeoutException

# created by Lucy
class TestClass:

    @staticmethod
    def test_convert_data():
        size = 0.2
        count = 2.3
        bottle = count.split('.')[1]
        if count.__contains__('.') or size <= 0.75:
            qty = (count * 12) + bottle
        else:
            qty = count * 12

        print(qty)


if __name__ == "__main__":
    # 使用 unittest 依次执行当前模块中 test 打头的方法
    unittest.main()

