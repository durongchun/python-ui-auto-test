import unittest
import paramunittest
from base.assembler import Assembler
from postgresql_tool import PostgreSQLTool
from util.log_tool import start_info, end_info, log
from util.screenshot_tool import ScreenshotTool


# 参数化构建参数
@paramunittest.parametrized(
    # 参数{语言，环境}
    {"lan": "en_GB", "env": "UAT"}
)
# Ods 流程用例测试
class TestSyncData(unittest.TestCase):
    # 出错需要截图时此方法自动被调用
    def save_img(self, img_name):
        ScreenshotTool().save_img(self.driver, img_name)

    # 参数化构建方法
    def setParameters(self, lan, env):
        self.lan = lan
        self.env = env

    # 放在各个测试方法中首行执行
    @classmethod
    def before_setUp(self):
        # 开始的 log 信息
        start_info()
        # 装配器初始化并开启一个谷歌驱动
        self.assembler = Assembler()
        self.driver = self.assembler.get_driver()
        # 创建 csdn 页面类
        # self.csdn_page = CsdnPage(self.driver)

    # 放在各个测试方法中末行执行
    @classmethod
    def after_tearDown(self):
        # 结束的 log 信息
        end_info()
        # 装配器卸载
        self.assembler.disassemble_all()

    # 第一个测试点
    def test_sync_data(self):
        # log 信息
        log().info(f"Start to sync data")
        log().info(f"Connect to ods DB")
        # connect to live db
        conn = PostgreSQLTool.get_connection_db(self)
        cursor = conn.cursor()
        log().info(f"Clear all data from table: ods_stock_quant")
        # clear old data
        PostgreSQLTool.clear_all_data(cursor, conn)
        log().info(f"Sync data from stagingods to ods")
        # sync data from view to ods_stock_quant
        PostgreSQLTool.write_to_db_ods(conn)


# 当前用例程序入口
if __name__ == "__main__":
    # 使用 unittest 依次执行当前模块中 test 打头的方法
    # verbosity=0 静默模式，仅仅获取总的测试用例数以及总的结果
    # verbosity=1 默认模式，在每个成功的用例前面有个’.’,每个失败的用例前面有个’F’
    # verbosity=2 详细模式，测试结果会显示每个测试用例的所有相关信息
    unittest.main(verbosity=1)
