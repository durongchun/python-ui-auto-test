import unittest
import paramunittest
from numpy.testing._private.parameterized import parameterized
from base.assembler import Assembler
from browser_common import BrowserCommon
from erp_data import ErpData
from erp_create_products_page import ErpCreateProductPage
from erp_transfer_page import ErpTransferPage
from page_common import PageCommon
from util.config_reader import ConfigReader
from util.log_tool import start_info, end_info, log
from util.screenshot_tool import ScreenshotTool
from decimal import Decimal


# 参数化构建参数
@paramunittest.parametrized(
    # 参数{语言，环境}
    {"lan": ConfigReader().read("project")["lan"], "env": ConfigReader().read("project")["env"]}
)
# ods流程用例测试
class TestTransfer(unittest.TestCase):
    # 出错需要截图时此方法自动被调用
    def save_img(self, img_name):
        ScreenshotTool().save_img(self.driver, img_name)

    # 参数化构建方法
    def setParameters(self, lan, env):
        self.lan = lan
        self.env = env

    # @BeforeTest
    def setUp(self):
        # 开始的 log 信息
        start_info()
        # 装配器初始化
        self.assembler = Assembler()
        # 提取驱动
        self.driver = self.assembler.get_driver()

    # @AfterTest
    def tearDown(self):
        # 结束的 log 信息
        end_info()
        # 装配器卸载
        self.assembler.disassemble_all()

    # 第一个测试点
    @parameterized.expand(ErpData.test_delivery_orders_transfer_data)
    def test_delivery_orders_transfer(self, description, product1, product2, vintage1, vintage2, demand1, demand2,
                                      unit1, unit2, delivery_address, operation_type, source_location):
        # log 信息
        log().info(f"ERP This is the first case, Environment: " + self.env + " Language: " + self.lan)
        erp = ErpCreateProductPage(self.driver)
        tran_page = ErpTransferPage(self.driver)
        log().info("Go ERP")
        BrowserCommon.jump_to(self, ErpData.url)
        erp.login(ErpData.user_name, ErpData.pass_word)
        erp.go_inventory()
        # get product original qty
        origin_qty1 = tran_page.check_product_quantity(product1, vintage1)
        origin_qty2 = tran_page.check_product_quantity(product2, vintage2)
        log().info("Original quantity of " + product1 + " is: " + origin_qty1)
        log().info("Original quantity of " + product2 + " is: " + origin_qty2)
        # go transfer
        tran_page.go_transfer_page()
        tran_page.click_create_button()
        log().info("Select the 'Delivery address'")
        tran_page.select_delivery_address(delivery_address)
        tran_page.select_operation_type(operation_type)
        tran_page.select_source_location(source_location)
        tran_page.select_products_and_transfer(product1, product2, str(demand1), str(demand2))
        # get product current qty
        current_qty1 = tran_page.check_product_quantity(product1, vintage1)
        current_qty2 = tran_page.check_product_quantity(product2, vintage2)
        log().info("Current quantity of " + product1 + " is: " + origin_qty1)
        log().info("Current quantity of " + product2 + " is: " + origin_qty2)
        self.assertEqual(tran_page.compare_to_qty_stock_out(origin_qty1, current_qty1, demand1), True,
                         "Transfer with delivery orders: " + product1 + "successfully")
        self.assertEqual(tran_page.compare_to_qty_stock_out(origin_qty2, current_qty2, demand2), True,
                         "Transfer with delivery orders: " + product2 + "successfully")

    # 第二个测试点
    @parameterized.expand(ErpData.test_internal_transfer_data)
    def test_internal_transfer(self, description, product, product_code, demand, unit, contact,
                               operation_type, source_location, destination_location):
        # log 信息
        log().info(f"ERP This is the second case, Environment: " + self.env + " Language: " + self.lan)
        erp = ErpCreateProductPage(self.driver)
        tran_page = ErpTransferPage(self.driver)
        log().info("Go ERP")
        BrowserCommon.jump_to(self, ErpData.url)
        erp.login(ErpData.user_name, ErpData.pass_word)
        erp.go_inventory()
        # get product original qty
        origin_source_location_qty = tran_page.check_product_quantity_from_inventory_report(
            product_code, source_location)
        origin_destination_location_qty = tran_page.check_product_quantity_from_inventory_report(
            product_code, destination_location)
        log().info("Original quantity of " + product + " in source location is: " +
                   origin_source_location_qty)
        log().info("Original quantity of " + product + " in destination location is: " +
                   origin_destination_location_qty)
        # go transfer
        tran_page.go_transfer_page()
        tran_page.click_create_button()
        log().info("Select the 'Contact'")
        tran_page.select_delivery_address(contact)
        tran_page.select_operation_type(operation_type)
        tran_page.select_source_location(source_location)
        tran_page.select_destination_location(destination_location)
        tran_page.select_products_and_transfer(product, "", str(demand), "")
        # get product current qty
        current_source_location_qty = tran_page.check_product_quantity_from_inventory_report(
            product_code, source_location)
        current_destination_location_qty = tran_page.check_product_quantity_from_inventory_report(
            product_code, destination_location)
        log().info("Current quantity of " + product + " in source location is: " +
                   current_source_location_qty)
        log().info("Current quantity of " + product + " in destination location is: " +
                   current_destination_location_qty)
        self.assertEqual(tran_page.compare_to_qty_stock_out(
            origin_source_location_qty, current_source_location_qty, demand), True,
            "Internal Transfer: " + product + " successfully")
        self.assertEqual(tran_page.compare_to_qty_stock_in(
            origin_destination_location_qty, current_destination_location_qty, demand), True,
            "Internal Transfer: " + product + " successfully")

    # 第三个测试点
    @parameterized.expand(ErpData.test_receipts_transfer_data)
    def test_receipts_transfer(self, description, product, product_code, demand, unit, contact,
                               operation_type, destination_location):
        # log 信息
        log().info(f"ERP This is the third case, Environment: " + self.env + " Language: " + self.lan)
        erp = ErpCreateProductPage(self.driver)
        tran_page = ErpTransferPage(self.driver)
        log().info("Go ERP")
        BrowserCommon.jump_to(self, ErpData.url)
        erp.login(ErpData.user_name, ErpData.pass_word)
        erp.go_inventory()
        # get product original qty
        origin_destination_location_qty = tran_page.check_product_quantity_from_inventory_report(
            product_code, destination_location)
        log().info("Original quantity of " + product + " in destination location is: " +
                   origin_destination_location_qty)
        # go transfer
        tran_page.go_transfer_page()
        tran_page.click_create_button()
        log().info("Select the 'Contact'")
        tran_page.select_delivery_address(contact)
        tran_page.select_operation_type(operation_type)
        tran_page.select_destination_location(destination_location)
        tran_page.select_products_and_transfer(product, "", str(demand), "")
        # get product current qty
        current_destination_location_qty = tran_page.check_product_quantity_from_inventory_report(
            product_code, destination_location)
        log().info("Current quantity of " + product + " in destination location is: " +
                   current_destination_location_qty)
        self.assertEqual(tran_page.compare_to_qty_stock_in(
            origin_destination_location_qty, current_destination_location_qty, demand), True,
            "Receipts Transfer: " + product + " successfully")

    # 第四个测试点
    @parameterized.expand(ErpData.test_return_transfer_data)
    def test_returns_transfer(self, description, product, product_code, demand, unit, contact,
                              operation_type, ware_house, destination_location):
        # log 信息
        log().info(f"ERP This is the fourth case, Environment: " + self.env + " Language: " + self.lan)
        erp = ErpCreateProductPage(self.driver)
        tran_page = ErpTransferPage(self.driver)
        log().info("Go ERP")
        BrowserCommon.jump_to(self, ErpData.url)
        erp.login(ErpData.user_name, ErpData.pass_word)
        erp.go_inventory()
        # get product original qty
        origin_destination_location_qty = tran_page.check_product_quantity_from_inventory_report(
            product_code, destination_location)
        log().info("Original quantity of " + product + " in destination location is: " +
                   origin_destination_location_qty)
        # go transfer
        tran_page.go_transfer_page()
        tran_page.click_create_button()
        log().info("Select the 'Contact'")
        tran_page.select_delivery_address(contact)
        tran_page.select_operation_type_search(operation_type, ware_house)
        tran_page.select_destination_location(destination_location)
        tran_page.select_products_and_transfer(product, "", str(demand), "")
        # get product current qty
        current_destination_location_qty = tran_page.check_product_quantity_from_inventory_report(
            product_code, destination_location)
        log().info("Current quantity of " + product + " in destination location is: " +
                   current_destination_location_qty)
        self.assertEqual(tran_page.compare_to_qty_stock_in(
            origin_destination_location_qty, current_destination_location_qty, demand), True,
            "Returns Transfer: " + product + " successfully")


if __name__ == "__main__":
    # 使用 unittest 依次执行当前模块中 test 打头的方法
    # verbosity=0 静默模式，仅仅获取总的测试用例数以及总的结果
    # verbosity=1 默认模式，在每个成功的用例前面有个’.’,每个失败的用例前面有个’F’
    # verbosity=2 详细模式，测试结果会显示每个测试用例的所有相关信息
    unittest.main(verbosity=0)
