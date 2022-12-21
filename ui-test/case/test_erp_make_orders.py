import unittest
import paramunittest
from numpy.testing._private.parameterized import parameterized
from base.assembler import Assembler
from browser_common import BrowserCommon
from erp_data import ErpData
from erp_create_products_page import ErpCreateProductPage
from erp_manufacturing_orders_page import ErpMakeOrdersPage
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
class TestMakeOrders(unittest.TestCase):
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
    @parameterized.expand(ErpData.test_make_orders_data)
    def test_make_orders(self, description, product, quantity, unit, operation_type, component_location,
                         finished_products_location, components1, components2, components3,
                         consume1, consume2, consume3, uom):
        # log 信息
        log().info(f"ERP Make Orders, Environment: " + self.env + " Language: " + self.lan)
        erp = ErpCreateProductPage(self.driver)
        m_order = ErpMakeOrdersPage(self.driver)
        tran_page = ErpTransferPage(self.driver)
        log().info("Go ERP")
        BrowserCommon.jump_to(self, ErpData.url)
        erp.login(ErpData.user_name, ErpData.pass_word)
        erp.go_inventory()
        # get product original qty
        origin_qty1 = tran_page.check_product_quantity(m_order.get_product_name(components1),
                                                       m_order.get_category(components1))
        origin_qty2 = tran_page.check_product_quantity(m_order.get_product_name(components2),
                                                       m_order.get_category(components2))
        origin_product_qty = tran_page.check_product_quantity(m_order.get_product_name(product),
                                                              m_order.get_category(product))
        log().info("Original quantity of " + components1 + " is: " + origin_qty1)
        log().info("Original quantity of " + components2 + " is: " + origin_qty2)
        log().info("Original quantity of " + product + " is: " + origin_product_qty)
        m_order.go_manufacturing_orders()
        m_order.click_create_button()
        m_order.select_product(m_order.get_product_name(product), m_order.get_category(product))
        m_order.select_unit(unit)
        m_order.input_quantity(quantity)
        m_order.click_miscellaneous_tab()
        m_order.select_operation_type(operation_type)
        m_order.select_component_location(component_location)
        m_order.select_finished_products_location(finished_products_location)
        m_order.click_component_tab()
        m_order.add_component(components1, components2, components3, consume1, consume2, consume3)
        m_order.save_process()
        # get product current qty
        current_qty1 = tran_page.check_product_quantity(m_order.get_product_name(components1),
                                                        m_order.get_category(components1))
        current_qty2 = tran_page.check_product_quantity(m_order.get_product_name(components2),
                                                        m_order.get_category(components2))
        current_product_qty = tran_page.check_product_quantity(m_order.get_product_name(product),
                                                               m_order.get_category(product))
        log().info("Current quantity of " + components1 + " is: " + current_qty1)
        log().info("Current quantity of " + components2 + " is: " + current_qty2)
        log().info("Current quantity of " + product + " is: " + current_product_qty)
        self.assertEqual(tran_page.compare_to_qty_stock_out(origin_qty1, current_qty1, consume1), True,
                         "Transfer with delivery orders: " + components1 + "successfully")
        self.assertEqual(tran_page.compare_to_qty_stock_out(origin_qty2, current_qty2, consume2), True,
                         "Transfer with delivery orders: " + components2 + "successfully")
        self.assertEqual(tran_page.compare_to_qty_stock_in(origin_qty2, current_qty2, consume2), True,
                         "Transfer with delivery orders: " + components2 + "successfully")


if __name__ == "__main__":
    # 使用 unittest 依次执行当前模块中 test 打头的方法
    # verbosity=0 静默模式，仅仅获取总的测试用例数以及总的结果
    # verbosity=1 默认模式，在每个成功的用例前面有个’.’,每个失败的用例前面有个’F’
    # verbosity=2 详细模式，测试结果会显示每个测试用例的所有相关信息
    unittest.main(verbosity=0)
