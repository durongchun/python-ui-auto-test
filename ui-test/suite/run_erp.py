import os
import unittest

import test_erp_add_warehouse_location
import test_erp_harvest
import test_erp_make_orders
import test_erp_sample_in
import test_erp_sample_out
import test_erp_search_product
import test_erp_transfer
import test_erp_add_products
from util.config_reader import ConfigReader
from util.report_tool import ReportTool

# 报告存放路径
report_path = os.path.abspath(os.path.dirname(__file__))[
              :os.path.abspath(os.path.dirname(__file__)).find("python-ui-auto-test") + len(
                  "python-ui-auto-test")] + "/ui-test" + ConfigReader().read("html")["htmlfile_path"]
# Report name
report_name = ConfigReader().read("html")["htmlfile_name"]

# 运行所有用例（单线程
if __name__ == "__main__":
    # create test suite
    suites = unittest.TestSuite()
    loader = unittest.TestLoader()

    # erp测试流程添加到测试套
    suites.addTests(loader.loadTestsFromModule(test_erp_add_products))
    suites.addTests(loader.loadTestsFromModule(test_erp_transfer))
    suites.addTests(loader.loadTestsFromModule(test_erp_sample_out))
    suites.addTests(loader.loadTestsFromModule(test_erp_sample_in))
    suites.addTests(loader.loadTestsFromModule(test_erp_harvest))
    suites.addTests(loader.loadTestsFromModule(test_erp_add_warehouse_location))
    suites.addTests(loader.loadTestsFromModule(test_erp_make_orders))
    suites.addTests(loader.loadTestsFromModule(test_erp_search_product))

    # 报告生成器，运行用例并生成报告，对 BeautifulReport 套了一层外壳
    ReportTool(suites).run(filename=report_name, description='ERP', report_dir=report_path, theme="theme_cyan")
