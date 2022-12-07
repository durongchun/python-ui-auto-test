from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from browser_common import BrowserCommon
from common.page_common import PageCommon
from erp_data import ErpData
from erp_locator import ErpLocator
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time
import unittest
import paramunittest

from erp_transfer_page import ErpTransferPage
from log_tool import log


# ERP页面类
class ErpAddWarehouseLocationPage(PageCommon):
    def __init__(self, driver=None):
        super().__init__(driver)

    def go_warehouses(self):
        self.highlight(self.find_element(By.XPATH, ErpLocator.configuration))
        self.find_element(By.XPATH, ErpLocator.configuration).click()
        self.highlight(self.find_element(By.XPATH, ErpLocator.warehouse_option))
        self.move_action("xpath", ErpLocator.warehouse_option)
        time.sleep(1)

    def add_warehouse(self, warehouse_name, short_name, address):
        self.highlight(self.find_element(By.CSS_SELECTOR, ErpLocator.warehouse_create))
        self.find_element(By.CSS_SELECTOR, ErpLocator.warehouse_create).click()
        time.sleep(1)
        self.highlight(self.find_element(By.NAME, ErpLocator.warehouse_name))
        self.input("name", ErpLocator.warehouse_name, warehouse_name)
        time.sleep(1)
        self.highlight(self.find_element(By.NAME, ErpLocator.short_name))
        self.input("name", ErpLocator.short_name, short_name)
        self.select_address(address)

    def select_address(self, address):
        self.active_dropdown(self.find_element(By.XPATH, ErpLocator.address))
        self.highlight(self.find_element(By.XPATH, ErpLocator.address))
        lis = self.find_elements(By.XPATH, ErpLocator.address_dropdown_options)
        for li in lis:
            if "Search More..." == li.text:
                self.highlight(li)
                li.click()
                break

        ErpTransferPage.search_location(self, address)
        self.highlight(self.find_element(By.CSS_SELECTOR, ErpLocator.save_button))
        self.find_element(By.CSS_SELECTOR, ErpLocator.save_button).click()

    def go_locations(self):
        self.highlight(self.find_element(By.XPATH, ErpLocator.configuration))
        self.find_element(By.XPATH, ErpLocator.configuration).click()
        self.highlight(self.find_element(By.XPATH, ErpLocator.location_option))
        self.move_action("xpath", ErpLocator.location_option)
        time.sleep(1)

    def add_location(self, location_name, parent_location, location_type):
        self.highlight(self.find_element(By.CSS_SELECTOR, ErpLocator.warehouse_create))
        self.find_element(By.CSS_SELECTOR, ErpLocator.warehouse_create).click()
        self.highlight(self.find_element(By.NAME, ErpLocator.warehouse_name))
        self.input("name", ErpLocator.warehouse_name, location_name)
        self.select_parent_location(parent_location)
        self.select_location_type(location_type)
        self.highlight(self.find_element(By.CSS_SELECTOR, ErpLocator.save_button))
        self.find_element(By.CSS_SELECTOR, ErpLocator.save_button).click()

    def select_parent_location(self, parent_location):
        self.active_dropdown(self.find_element(By.NAME, ErpLocator.parent_location))
        lis = self.find_elements(By.XPATH, ErpLocator.address_dropdown_options)
        for li in lis:
            if "Search More..." == li.text:
                self.highlight(li)
                li.click()
                break
        ErpTransferPage.search_location_with_parameter(self, parent_location)

    def select_location_type(self, location_type):
        self.highlight(self.find_element(By.NAME, ErpLocator.location_type))
        self.find_element(By.NAME, ErpLocator.location_type).click()
        self.highlight(self.find_element(By.XPATH, ErpLocator.location_type_option.format(location_type)))
        self.select_child_elements("name", ErpLocator.location_type, location_type)

    def validation_error_displaying(self):
        try:
            WebDriverWait(self.driver, 5).until(
                expected_conditions.presence_of_element_located(
                    (By.XPATH, ErpLocator.validation_error)))
        except TimeoutException as ex:
            # print("Exception has been thrown. " + str(ex))
            return False
        else:
            return True

    def get_warning_text(self):
        return self.find_element(By.CSS_SELECTOR, ErpLocator.warning).text

    def click_ok_button(self):
        self.highlight(self.find_element(By.CSS_SELECTOR, ErpLocator.ok_button))
        self.find_element(By.CSS_SELECTOR, ErpLocator.ok_button).click()

    def click_discard_button(self):
        self.highlight(self.find_element(By.CSS_SELECTOR, ErpLocator.discard_button))
        self.find_element(By.CSS_SELECTOR, ErpLocator.discard_button).click()
