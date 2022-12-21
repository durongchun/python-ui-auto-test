import unittest
import paramunittest
from numpy.testing._private.parameterized import parameterized
from browser_common import BrowserCommon
from erp_data import ErpData
from erp_create_products_page import ErpCreateProductPage
from erp_transfer_page import ErpTransferPage
from page_common import PageCommon
from util.config_reader import ConfigReader
from util.log_tool import start_info, end_info, log
from util.screenshot_tool import ScreenshotTool

# created by Lucy
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
        print("Test Starts")
        # 开启一个Firefox驱动
        self.driver = PageCommon.get_chrome_driver()

    # @AfterTest
    def tearDown(self):
        print("Test Ends")
        # 驱动退出
        self.driver.quit()

    # 第一个测试点
    @parameterized.expand(ErpData.test_harvest_data)
    def test_harvest(self, description, product, vintage1, vintage2, vintage3, demand1, demand2, demand3, unit,
                       contact, operation_type, ware_house, source_location, destination_location):
        # log 信息
        log().info(f"ERP Harvest, Environment: " + self.env + " Language: " + self.lan)
        erp = ErpCreateProductPage(self.driver)
        tran_page = ErpTransferPage(self.driver)
        log().info("Go ERP")
        BrowserCommon.jump_to(self, ErpData.url)
        erp.login(ErpData.user_name, ErpData.pass_word)
        erp.go_inventory()
        # get product original qty
        origin_qty1 = tran_page.check_product_quantity(product, vintage1)
        origin_qty2 = tran_page.check_product_quantity(product, vintage2)
        origin_qty3 = tran_page.check_product_quantity(product, vintage3)
        log().info(
            "Original quantity of " + product + "(" + vintage1 + ")" + " in destination location is: " + origin_qty1)
        log().info(
            "Original quantity of " + product + "(" + vintage2 + ")" + " in destination location is: " + origin_qty2)
        log().info(
            "Original quantity of " + product + "(" + vintage3 + ")" + " in destination location is: " + origin_qty3)
        # go transfer
        tran_page.go_transfer_page()
        tran_page.click_create_button()
        log().info("Select the 'Contact'")
        tran_page.select_delivery_address(contact)
        tran_page.select_operation_type_search(operation_type, ware_house)
        tran_page.select_source_location(source_location)
        tran_page.select_destination_location(destination_location)
        tran_page.select_products_vintages_and_transfer(product, vintage1, vintage2, vintage3, str(demand1),
                                                        str(demand2), str(demand3))
        # get product current qty
        current_qty1 = tran_page.check_product_quantity(product, vintage1)
        current_qty2 = tran_page.check_product_quantity(product, vintage2)
        current_qty3 = tran_page.check_product_quantity(product, vintage3)
        log().info("Current quantity of " + product + "(" + vintage1 + ")" + " is: " + current_qty1)
        log().info("Current quantity of " + product + "(" + vintage2 + ")" + " is: " + current_qty2)
        log().info("Current quantity of " + product + "(" + vintage3 + ")" + " is: " + current_qty3)
        self.assertEqual(tran_page.compare_to_qty_stock_in(origin_qty1, current_qty1, demand1), True,
                         "Harvest: " + product + " successfully")
        self.assertEqual(tran_page.compare_to_qty_stock_in(origin_qty2, current_qty2, demand2), True,
                         "Harvest: " + product + " successfully")
        self.assertEqual(tran_page.compare_to_qty_stock_in(origin_qty3, current_qty3, demand3), True,
                         "Harvest: " + product + " successfully")


if __name__ == "__main__":
    # 使用 unittest 依次执行当前模块中 test 打头的方法
    # verbosity=0 静默模式，仅仅获取总的测试用例数以及总的结果
    # verbosity=1 默认模式，在每个成功的用例前面有个’.’,每个失败的用例前面有个’F’
    # verbosity=2 详细模式，测试结果会显示每个测试用例的所有相关信息
    unittest.main(verbosity=0)
