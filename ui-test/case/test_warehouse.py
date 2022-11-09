import os
import unittest
import paramunittest
import pytest

from base.assembler import Assembler
from browser_common import BrowserCommon
from erp_locator import ErpLocator
from erp_page import ErpPage
from excel_reader import ExcelData
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
    @pytest.yield_fixture(autouse=True)
    def setUp(self):
        # 开始的 log 信息
        start_info()
        # 装配器初始化
        self.assembler = Assembler()
        # 提取驱动
        self.driver = self.assembler.get_driver()

    # @AfterTest
    @pytest.yield_fixture(autouse=True)
    def tearDown(self):
        # 结束的 log 信息
        end_info()
        # 装配器卸载
        yield
        self.assembler.disassemble_all()

    # 第一个测试点ExcelData.get_datas()
    @pytest.mark.parametrize('test_data', [{"UserName": "lucy.du@holinova.com", "PassWord": "durongchun123~"}])
    def test_warehousing(self, test_data):
        # log 信息
        log().info(f"Container World第一个用例，环境" + self.env + "语言" + self.lan)
        # 初始化百度页面
        erp_page = ErpPage(self.driver)
        # 开启ContainerWorld首页
        erp_page.jump_to()
        # 首页login
        user_name = test_data['UserName']
        pass_word = test_data['PassWord']
        PageCommon.login(user_name, pass_word, ErpLocator.user_name, ErpLocator.pass_word, ErpLocator.login_btn)


if __name__ == "__main__":
    # 使用 unittest 依次执行当前模块中 test 打头的方法
    # verbosity=0 静默模式，仅仅获取总的测试用例数以及总的结果
    # verbosity=1 默认模式，在每个成功的用例前面有个’.’,每个失败的用例前面有个’F’
    # verbosity=2 详细模式，测试结果会显示每个测试用例的所有相关信息
    unittest.main(verbosity=0)
