import unittest
import paramunittest
from numpy.testing._private.parameterized import parameterized
from base.assembler import Assembler
from browser_common import BrowserCommon
from erp_data import ErpData
from erp_create_products_page import ErpCreateProductPage
from erp_search_products_page import ErpSearchProductPage
from erp_transfer_page import ErpTransferPage
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
    @parameterized.expand(ErpData.test_search_product_data)
    def test_search_product(self, description, product_name, product_id, product_code):
        # log 信息
        log().info(f"ERP Search Product, Environment: " + self.env + " Language: " + self.lan)
        erp = ErpCreateProductPage(self.driver)
        tran_page = ErpTransferPage(self.driver)
        log().info("Go ERP")
        BrowserCommon.jump_to(self, ErpData.url)
        erp.login(ErpData.user_name, ErpData.pass_word)
        erp.go_inventory()
        erp.select_products_dropdown()
        erp.search_products_by_product_name(product_name)
        self.assertTrue(ErpSearchProductPage.is_product_existing(self, product_name),
                        "Product is searched out successfully by: " + product_name)
        erp.select_products_dropdown()
        erp.search_products_by_product_name(product_id)
        self.assertTrue(ErpSearchProductPage.is_product_existing(self, product_name),
                        "Product is searched out successfully by: " + str(product_id))
        erp.select_products_dropdown()
        erp.search_products_by_product_name(product_code)
        self.assertTrue(ErpSearchProductPage.is_product_existing(self, product_name),
                        "Product is searched out successfully by: " + str(product_code))


if __name__ == "__main__":
    # 使用 unittest 依次执行当前模块中 test 打头的方法
    # verbosity=0 静默模式，仅仅获取总的测试用例数以及总的结果
    # verbosity=1 默认模式，在每个成功的用例前面有个’.’,每个失败的用例前面有个’F’
    # verbosity=2 详细模式，测试结果会显示每个测试用例的所有相关信息
    unittest.main(verbosity=0)
