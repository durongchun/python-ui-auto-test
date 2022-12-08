from selenium.webdriver.common.by import By
from common.page_common import PageCommon
from erp_locator import ErpLocator
from selenium.common.exceptions import TimeoutException, NoSuchElementException


# ERP页面类
class ErpSearchProductPage(PageCommon):
    def __init__(self, driver=None):
        super().__init__(driver)

    def is_product_existing(self, product_name):
        try:
            self.driver.find_element(By.XPATH, ErpLocator.search_result.format(product_name))
        except NoSuchElementException:
            print("Product is not showing")
            return False
        else:
            print("Product is showing")
            return True
