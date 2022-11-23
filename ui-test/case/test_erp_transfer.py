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

    # 第一个测试点ExcelData.get_datas()
    @parameterized.expand(ErpData.test_internal_transfer_data)
    def test_warehousing(self, description, warehouse_name, location_name, product_name, product_id,
                         vintage1, vintage2, product_code1, product_code2, quantity1, quantity2,
                         upc, scc, operation_type, source_location, destination_location):
        # log 信息
        log().info(f"Container World第一个用例，环境" + self.env + "语言" + self.lan)
        # go ERP login Page
        erp = ErpCreateProductPage(self.driver)
        tran_page = ErpTransferPage(self.driver)
        BrowserCommon.jump_to(self, ErpData.url)
        # login
        # PageCommon.login(self, ErpData.user_name, ErpData.pass_word, ErpLocator.user_name,
        #                  ErpLocator.pass_word, ErpLocator.login_btn)
        erp.login(ErpData.user_name, ErpData.pass_word)
        print("description: " + description)
        print("warehouse_name: " + warehouse_name)
        qty1 = PageCommon.convert_to_decimal(quantity1)
        print("quantity: " + str(qty1))

        erp.go_inventory()
        # go transfer
        tran_page.go_transfer_page()
        tran_page.select_operation_type(operation_type)
        tran_page.select_source_location(source_location)
        tran_page.select_destination_location(destination_location)


if __name__ == "__main__":
    # 使用 unittest 依次执行当前模块中 test 打头的方法
    # verbosity=0 静默模式，仅仅获取总的测试用例数以及总的结果
    # verbosity=1 默认模式，在每个成功的用例前面有个’.’,每个失败的用例前面有个’F’
    # verbosity=2 详细模式，测试结果会显示每个测试用例的所有相关信息
    unittest.main(verbosity=0)
