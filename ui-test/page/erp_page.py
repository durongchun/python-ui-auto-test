import excel_reader
from common.page_common import PageCommon
from data.baidu_main_data import BaiduMainData
from locator.baidu_main_locator import BaiduMainLocator


# 百度首页页面类
class ErpPage(PageCommon):
    # 百度首页进入页面操作
    def jump_to(self):
        self.driver.get("http://23.16.247.137:9069/web/login")


    # 搜索数据
    def search(self):
        self.input(BaiduMainLocator.search_input, BaiduMainData.data)
        self.click_element(BaiduMainLocator.search_btn)

