import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from common.page_common import PageCommon
from erp_locator import ErpLocator
from erp_transfer_page import ErpTransferPage
from log_tool import log


# ERP页面类
class ErpMakeOrdersPage(PageCommon):
    def __init__(self, driver=None):
        super().__init__(driver)

    def go_manufacturing_orders(self):
        self.highlight(self.find_element(By.XPATH, ErpLocator.orders))
        self.find_element(By.XPATH, ErpLocator.orders).click()
        self.highlight(self.find_element(By.XPATH, ErpLocator.make_orders_option))
        self.move_action("xpath", ErpLocator.make_orders_option)
        time.sleep(1)

    def click_create_button(self):
        self.highlight(self.find_element(By.XPATH, ErpLocator.create_button))
        self.find_element(By.XPATH, ErpLocator.create_button).click()

    def select_product(self, product):
        self.highlight(self.find_element(By.XPATH, ErpLocator.product_box))
        self.find_element(By.XPATH, ErpLocator.product_box).click()
        lis = self.find_elements(By.XPATH, ErpLocator.product_options)
        for li in lis:
            if "Search More..." == li.text:
                self.highlight(li)
                li.click()
                break
        time.sleep(1)
        self.search_product_vintage_category(product)

    def search_product_vintage_category(self, product_name):
        log().info("Search product and add it to line")
        product = product_name.split("(")[0]
        pro_sub = product_name.split("(")[1]
        vintage = pro_sub.split(",")[0]
        category = pro_sub.split(",")[1]

        self.highlight(self.driver.find_element(By.CSS_SELECTOR, ErpLocator.location_search_box))
        self.driver.find_element(By.CSS_SELECTOR, ErpLocator.location_search_box).send_keys(product)
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, ErpLocator.location_search_box).send_keys(Keys.ENTER)
        time.sleep(1)
        self.highlight(self.driver.find_element(By.XPATH, ErpLocator.product_vintage_category_search_results.
                                                format(vintage, category)))
        self.driver.find_element(By.XPATH, ErpLocator.product_vintage_category_search_results.
                                 format(vintage, category)).click()
        time.sleep(2)

    def input_quantity(self, qty):
        self.highlight(By.XPATH, ErpLocator.quantity_input)
        self.input("xpath", ErpLocator.quantity_input, qty)

    def select_unit(self, unit):
        self.highlight(self.find_element(By.XPATH, ErpLocator.quantity_uom))
        self.find_element(By.XPATH, ErpLocator.quantity_uom).click()
        lis = self.find_elements(By.XPATH, ErpLocator.quantity_uom_options)
        for li in lis:
            if unit == li.text:
                self.highlight(li)
                li.click()
                break

    def click_miscellaneous_tab(self):
        self.highlight(self.find_element(By.CSS_SELECTOR, ErpLocator.miscellaneous_tab))
        self.find_element(By.CSS_SELECTOR, ErpLocator.miscellaneous_tab).click()

    def click_component_tab(self):
        self.highlight(self.find_element(By.CSS_SELECTOR, ErpLocator.component_tab))
        self.find_element(By.CSS_SELECTOR, ErpLocator.component_tab).click()

    def select_operation_type(self, operation_type):
        self.highlight(self.find_element(By.XPATH, ErpLocator.operation_type_box))
        self.find_element(By.XPATH, ErpLocator.operation_type_box).click()
        lis = self.find_elements(By.XPATH, ErpLocator.operation_type_options)
        for li in lis:
            if operation_type == li.text:
                self.highlight(li)
                li.click()
                break

    def select_component_location(self, component_location):
        self.highlight(self.find_element(By.XPATH, ErpLocator.component_location_box))
        self.find_element(By.XPATH, ErpLocator.component_location_box).click()
        lis = self.find_elements(By.XPATH, ErpLocator.component_location_options)
        for li in lis:
            if "Search More..." == li.text:
                self.highlight(li)
                li.click()
                break
        ErpTransferPage.search_location(component_location)

    def select_finished_products_location(self, finished_products_location):
        self.highlight(self.find_element(By.XPATH, ErpLocator.finished_product_location_box))
        self.find_element(By.XPATH, ErpLocator.finished_product_location_box).click()
        lis = self.find_elements(By.XPATH, ErpLocator.finished_product_location_options)
        for li in lis:
            if "Search More..." == li.text:
                self.highlight(li)
                li.click()
                break
        ErpTransferPage.search_location(finished_products_location)

    def add_component(self, component1, consume1):
        product = component1.split("(")[0]
        sub_pro = component1.split("(")[1]
        category = sub_pro.replace("(,)", "")
        ErpTransferPage.select_product(product)
        self.input("xpath", ErpLocator.transfer_demand_box, consume1)

