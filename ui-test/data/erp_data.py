# 百度首页数据驱动
import pytest

from excel_reader import ExcelReader
from page_common import PageCommon


class ErpData:
    test_add_MtB_data = PageCommon.test_convert_data(
        ExcelReader.get_test_add_MtB_xls(PageCommon.get_data_path()))

    test_add_rust_data = PageCommon.test_convert_data(
        ExcelReader.get_test_add_rust_xls(PageCommon.get_data_path()))

    test_delivery_orders_transfer_data = PageCommon.test_convert_data(
        ExcelReader.get_test_delivery_orders_transfer_xls(PageCommon.get_data_path()))

    test_internal_transfer_data = PageCommon.test_convert_data(
        ExcelReader.get_test_receipts_transfer_xls(PageCommon.get_data_path()))

    test_receipts_transfer_data = PageCommon.test_convert_data(
        ExcelReader.get_test_receipts_transfer_xls(PageCommon.get_data_path()))

    test_return_transfer_data = PageCommon.test_convert_data(
        ExcelReader.get_test_return_transfer_xls(PageCommon.get_data_path()))

    url = "https://dev.mtboucherie.com/web#cids=1"
    user_name = "lucy.du@holinova.com"
    pass_word = "durongchun123~"
    product_url = "https://dev.mtboucherie.com/web#menu_id=243&action=390&model=product.template&view_type=kanban"


