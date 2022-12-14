import os
import unittest

import test_container_world
import test_mobile_andriod
import test_wine_direct
from case import test_baidu_case, test_csdn_case, test_other_case
from util.config_reader import ConfigReader
from util.report_tool import ReportTool

# 报告存放路径
report_path = os.path.abspath(os.path.dirname(__file__))[
              :os.path.abspath(os.path.dirname(__file__)).find("python-ui-auto-test") + len(
                  "python-ui-auto-test")] + "/ui-test" + ConfigReader().read("html")["htmlfile_path"]
# 报告名字
report_name = ConfigReader().read("html")["htmlfile_name"]

# 运行所有用例（单线程）
if __name__ == "__main__":
    # 创建测试套
    suites = unittest.TestSuite()
    loader = unittest.TestLoader()

    # ods测试流程添加到测试套
    suites.addTests(loader.loadTestsFromModule(test_container_world))
    suites.addTests(loader.loadTestsFromModule(test_wine_direct))
    # suites.addTests(loader.loadTestsFromModule(test_mobile_andriod))

    # 报告生成器，运行用例并生成报告，对 BeautifulReport 套了一层外壳
    ReportTool(suites).run(filename=report_name, description='demo', report_dir=report_path, theme="theme_cyan")
