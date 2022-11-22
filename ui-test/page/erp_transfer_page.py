from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from erp_locator import ErpLocator
import time
from page_common import PageCommon


# ERP页面类
class ErpTransferPage(PageCommon):
    def __init__(self, driver=None):
        super().__init__(driver)

    def go_transfer_page(self):
        self.wait_element(expected_conditions.presence_of_element_located((By.XPATH, ErpLocator.operations_menu)))
        # self.find_element(By.XPATH, ErpLocator.operations_menu).click()
        # ele = self.find_element(By.XPATH, ErpLocator.operations_menu)
        self.active_dropdown(self.find_element(By.XPATH, ErpLocator.operations_menu))

        self.click_and_hold(self.find_element(By.XPATH, ErpLocator.transfer_dropdown_option))
        self.find_element(By.XPATH, ErpLocator.transfer_dropdown_option).click()
        self.page_has_loaded()
        time.sleep(2)

    def select_operation_type(self, operation_type):
        self.driver.find_element(By.XPATH, ErpLocator.create).click()
        self.click("css_selector", ErpLocator.operation_type)
        lis = self.find_elements(By.XPATH, ErpLocator.operation_type_dropdown_options)
        for li in lis:
            if operation_type == li.text:
                li.click()
                break

    def select_source_location(self, source_location):
        self.click("css_selector", ErpLocator.source_location)
        lis = self.find_elements((By.XPATH, ErpLocator.source_location_dropdown_options))
        for li in lis:
            if source_location == li.text:
                li.click()
                break

    def select_destination_location(self, destination_location):
        self.click("css_selector", ErpLocator.destination_location)
        lis = self.find_elements(By.XPATH, ErpLocator.destination_location_dropdown_options)
        for li in lis:
            if destination_location == lis.text:
                li.click()
                break

