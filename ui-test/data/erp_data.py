# 百度首页数据驱动
import pytest

from excel_reader import ExcelReader
from page_common import PageCommon


class ErpMainData:
    test_data = PageCommon.test_convert_data(ExcelReader.get_xls(PageCommon.get_data_path()))
    user_name = "lucy.du@holinova.com"
    pass_word = "durongchun123~"
