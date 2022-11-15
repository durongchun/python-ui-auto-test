# 百度首页数据驱动
import pytest

from excel_reader import ExcelReader
from page_common import PageCommon


class ErpData:
    test_data = PageCommon.test_convert_data(ExcelReader.get_xls(PageCommon.get_data_path()))

    url = "http://23.16.247.137:9069/web/login"
    user_name = "lucy.du@holinova.com"
    pass_word = "durongchun123~"
    product_url = "https://erp.mtboucherie.com/web#menu_id=243&action=390&model=product.template&view_type=kanban"


