# user/bin/python3
# coding:utf-8

import os
import unittest
import test_erp_sample_out
from util.config_reader import ConfigReader
from util.report_tool import ReportTool
import yagmail

# 报告存放路径
report_path = os.path.abspath(os.path.dirname(__file__))[
              :os.path.abspath(os.path.dirname(__file__)).find("python-ui-auto-test") + len(
                  "python-ui-auto-test")] + "/ui-test" + ConfigReader().read("html")["htmlfile_path"]
# 报告名字
report_name = ConfigReader().read("html")["htmlfile_name"]


# 运行所有用例（单线程

def send_mail(report):
    yag = yagmail.SMTP(user="durongchun123@163.com", password="FLMLUFPOVZYHUWPS", host='smtp.163.com')
    subject = "自动化测试报告"
    contents = "自动化用例已执行完毕，详细报告请查看附件"
    yag.send('durongchun@hotmail.com', subject, contents, report)
    print("邮件已经发送成功！")


if __name__ == "__main__":
    # 创建测试套
    suites = unittest.TestSuite()
    loader = unittest.TestLoader()

    # erp测试流程添加到测试套
    suites.addTests(loader.loadTestsFromModule(test_erp_sample_out))

    # 报告生成器，运行用例并生成报告，对 BeautifulReport 套了一层外壳
    ReportTool(suites).run(filename=report_name, description='demo', report_dir=report_path, theme="theme_cyan")

    html_report = r'C:\Users\lucy\PycharmProjects\python-ui-auto-test\ui-test\report\html\UI_Test_Report.html'
    # 这个要注意要带目录路径，如果直接附文件名，程序会找不到路径
    send_mail(html_report)
