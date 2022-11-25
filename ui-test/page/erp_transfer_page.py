from selenium.webdriver import ActionChains, Keys
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
        self.click("css_selector", ErpLocator.operation_type)
        lis = self.find_elements(By.XPATH, ErpLocator.operation_type_dropdown_options)
        for li in lis:
            if operation_type == li.text:
                self.highlight(li)
                li.click()
                break

    def select_source_location(self, source_location):
        self.click("css_selector", ErpLocator.source_location)
        lis = self.find_elements(By.XPATH, ErpLocator.source_location_dropdown_options)
        for li in lis:
            if "Search More..." == li.text:
                li.click()
                break
        time.sleep(1)
        self.search_location(source_location)

    def select_destination_location(self, destination_location):
        self.click("css_selector", ErpLocator.destination_location)
        lis = self.find_elements(By.XPATH, ErpLocator.destination_location_dropdown_options)
        for li in lis:
            if "Search More..." == lis.text:
                li.click()
                break
        time.sleep(1)
        self.search_location(destination_location)

    def select_product_transfer(self):
        self.highlight(self.find_element(By.LINK_TEXT, ErpLocator.transfer_add_line))
        self.click("link_text", ErpLocator.transfer_add_line)

    def select_product(self):
        self.click("xpath", ErpLocator.transfer_product_box)

    def search_location(self, location):
        self.highlight(self.driver.find_element(By.CSS_SELECTOR, ErpLocator.location_search_box))
        self.driver.find_element(By.CSS_SELECTOR, ErpLocator.location_search_box).send_keys(location)
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, ErpLocator.location_search_box).send_keys(Keys.ENTER)
        time.sleep(1)
        self.highlight(self.driver.find_element(By.CSS_SELECTOR, ErpLocator.location_search_result))
        self.driver.find_element(By.CSS_SELECTOR, ErpLocator.location_search_result).click()
        time.sleep(2)

    def select_deliver_address(self, deliver_address):
        self.highlight(self.driver.find_element(By.CSS_SELECTOR, ErpLocator.deliver_address))
        self.active_dropdown((self.driver.find_element(By.CSS_SELECTOR, ErpLocator.deliver_address)))
        lis = self.find_elements(By.XPATH, ErpLocator.deliver_address_dropdown_options)
        for li in lis:
            if "Search More..." == lis.text:

                self.highlight(li)
                li.click()
                break
        time.sleep(1)
        self.highlight(self.driver.find_element(By.CSS_SELECTOR, ErpLocator.location_search_box))
        self.driver.find_element(By.CSS_SELECTOR, ErpLocator.location_search_box).send_keys(deliver_address)
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, ErpLocator.location_search_box).send_keys(Keys.ENTER)
        time.sleep(1)
        self.highlight(self.driver.find_element(By.CSS_SELECTOR, ErpLocator.deliver_address_search_results))
        self.driver.find_element(By.CSS_SELECTOR, ErpLocator.location_search_result).click()
        time.sleep(2)

    def click_create_button(self):
        self.highlight(self.driver.find_element(By.XPATH, ErpLocator.create))
        self.driver.find_element(By.XPATH, ErpLocator.create).click()
