from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions

import excel_reader
from common.page_common import PageCommon
from data.baidu_main_data import BaiduMainData
from erp_data import ErpData
from erp_locator import ErpLocator
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

    def select_products_dropdown(self):
        self.webDriverWait(self, 10).until(
            expected_conditions.presence_of_element_located(By.XPATH, ErpLocator.products))
        actions = ActionChains(self.driver)
        actions.move_to_element(self.driver.find_element(By.XPATH, ErpLocator.products)).click_and_hold().perform()
        self.driver.find_element(By.LINK_TEXT, ErpLocator.products_dropdown).click()
        self.page_has_loaded()

    def create_product(self, product_name ):
        self.driver.find_element(By.XPATH, ErpLocator.create).click()
        self.input(ErpLocator.product_name, product_name)

    def add_vintage(self, year):
        self.driver.find_element(By.XPATH, ErpLocator.attributes_Variants).click()
        self.driver.find_element(By.LINK_TEXT, ErpLocator.add_line).click()
        self.input(ErpLocator.attribute_box, "vintage")
        self.input(ErpLocator.values_box, year)



