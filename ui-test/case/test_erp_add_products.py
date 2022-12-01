import unittest
import paramunittest
from numpy.testing._private.parameterized import parameterized
from base.assembler import Assembler
from browser_common import BrowserCommon
from erp_data import ErpData
from erp_create_products_page import ErpCreateProductPage
from page_common import PageCommon
from util.config_reader import ConfigReader
from util.log_tool import start_info, end_info, log
from util.screenshot_tool import ScreenshotTool


# 参数化构建参数
@paramunittest.parametrized(
    # 参数{语言，环境}
    {"lan": ConfigReader().read("project")["lan"], "env": ConfigReader().read("project")["env"]}
)
# ods流程用例测试
class TestWareHouse(unittest.TestCase):
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
    @parameterized.expand(ErpData.test_add_MtB_data)
    def test_add_mtb_products(self, description, warehouse_name, location_name, product_name, product_id,
                              vintage1, vintage2, vintage3, vintage4, vintage5, vintage6, vintage7,
                              quantity1, quantity2, quantity3, quantity4, quantity5, quantity6, quantity7,
                              upc, scc):
        # log 信息
        log().info(f"ERP This is the first case, Environment: " + self.env + "Language: " + self.lan)
        # go ERP login Page
        erp = ErpCreateProductPage(self.driver)
        log().info("Go ERP")
        BrowserCommon.jump_to(self, ErpData.url)
        erp.login(ErpData.user_name, ErpData.pass_word)
        qty1 = PageCommon.convert_to_decimal(quantity1)
        erp.go_inventory()
        erp.select_products_dropdown()
        # clear same products created before
        # erp.clear_products(product_name, ErpLocator.products_details)
        # create product
        erp.create_product(product_name, product_id, upc)
        prod_url = erp.get_product_url()
        # add attributes and update qty if having vintages
        if vintage1 != 'NULL':
            erp.add_attributes(vintage1, vintage2, vintage3, vintage4, vintage5, vintage6, vintage7)
            erp.go_variants()
            erp.update_and_validate_vintage_quantity(PageCommon.get_url(self), vintage1, vintage2, vintage3,
                                                     vintage4, vintage5, vintage6, vintage7, warehouse_name,
                                                     location_name, quantity1, quantity2, quantity3, quantity4,
                                                     quantity5, quantity6, quantity7)
            erp.go_product_page(prod_url)
            erp.validate_all_vintage_qty(quantity1, quantity2, quantity3, quantity4, quantity5, quantity6, quantity7)
        else:
            # directly update quantity if no vintage
            erp.update_quantity(warehouse_name, location_name, quantity1)
            erp.back_product_page()
            # validate_quantity_on_hand
            self.assertEqual(erp.compare_to_quantity_on_hand(qty1), True,
                             "Updated quantity on hand is showing as expected: str(qty1)")

    # 第二个测试点
    @parameterized.expand(ErpData.test_add_rust_data)
    def test_add_rust_products(self, description, warehouse_name, location_name, product_name, product_id,
                               vintage1, vintage2, vintage3, vintage4, vintage5, vintage6, vintage7,
                               quantity1, quantity2, quantity3, quantity4, quantity5, quantity6, quantity7,
                               upc, scc):
        # log 信息
        log().info(f"ERP This is the second case, Environment: " + self.env + "Language: " + self.lan)
        erp = ErpCreateProductPage(self.driver)
        log().info("Go ERP")
        BrowserCommon.jump_to(self, ErpData.url)
        erp.login(ErpData.user_name, ErpData.pass_word)
        qty1 = PageCommon.convert_to_decimal(quantity1)
        erp.go_inventory()
        # erp.select_products_dropdown()
        erp.go_product()
        # clear same products created before
        # erp.clear_products(product_name, ErpLocator.products_details)
        # create product
        erp.create_product(product_name, product_id, upc)
        prod_url = erp.get_product_url()
        # add attributes and update qty if having vintages
        if vintage1 != 'NULL':
            erp.add_attributes(vintage1, vintage2, vintage3, vintage4, vintage5, vintage6, vintage7)
            erp.go_variants()
            erp.update_and_validate_vintage_quantity(PageCommon.get_url(self), vintage1, vintage2, vintage3,
                                                     vintage4, vintage5, vintage6, vintage7, warehouse_name,
                                                     location_name, quantity1, quantity2, quantity3, quantity4,
                                                     quantity5, quantity6, quantity7)
            erp.go_product_page(prod_url)
            erp.validate_all_vintage_qty(quantity1, quantity2, quantity3, quantity4, quantity5, quantity6, quantity7)
        else:
            # directly update quantity if no vintage
            erp.update_quantity(warehouse_name, location_name, quantity1)
            erp.back_product_page()
            # validate_quantity_on_hand
            self.assertEqual(erp.compare_to_quantity_on_hand(qty1), True,
                             "Updated quantity on hand is showing as expected: str(qty1)")


if __name__ == "__main__":
    # 使用 unittest 依次执行当前模块中 test 打头的方法
    # verbosity=0 静默模式，仅仅获取总的测试用例数以及总的结果
    # verbosity=1 默认模式，在每个成功的用例前面有个’.’,每个失败的用例前面有个’F’
    # verbosity=2 详细模式，测试结果会显示每个测试用例的所有相关信息
    unittest.main(verbosity=0)
