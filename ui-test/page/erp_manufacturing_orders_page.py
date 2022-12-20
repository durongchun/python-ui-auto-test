import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions

from common.page_common import PageCommon
from erp_create_products_page import ErpCreateProductPage
from erp_locator import ErpLocator
from erp_transfer_page import ErpTransferPage
from log_tool import log


# ERP页面类
class ErpMakeOrdersPage(PageCommon):
    def __init__(self, driver=None):
        super().__init__(driver)

    def go_manufacturing_orders(self):
        self.highlight(self.find_element(By.CSS_SELECTOR, ErpLocator.orders))
        self.find_element(By.CSS_SELECTOR, ErpLocator.orders).click()
        self.highlight(self.find_element(By.XPATH, ErpLocator.make_orders_option))
        self.move_action("xpath", ErpLocator.make_orders_option)
        time.sleep(1)

    def click_create_button(self):
        self.highlight(self.find_element(By.XPATH, ErpLocator.create_button))
        self.find_element(By.XPATH, ErpLocator.create_button).click()

    def select_product(self, product, category):
        self.highlight(self.find_element(By.XPATH, ErpLocator.product_box))
        self.find_element(By.XPATH, ErpLocator.product_box).click()
        lis = self.find_elements(By.XPATH, ErpLocator.product_options)
        for li in lis:
            if "Search More..." == li.text:
                self.highlight(li)
                li.click()
                break
        time.sleep(1)
        ErpTransferPage.search_product_vintage(self, product, category)

    def search_product_vintage_category(self, product_name):
        log().info("Search product and add it to line")
        product = product_name.split("(")[0]
        pro_sub = product_name.split("(")[1]
        vintage = pro_sub.split(",")[0]
        category_sub = pro_sub.split(",")[1]
        category = category_sub.replace(")", "")

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
        self.highlight(self.find_element(By.XPATH, ErpLocator.quantity_input))
        self.change_quantity(qty)

    def change_quantity(self, qty):
        self.driver.execute_script("document.getElementsByName(arguments[0])[0].value=arguments[1]",
                                   ErpLocator.quantity_input2, str(qty))

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
        ErpTransferPage.search_location(self, component_location)

    def select_finished_products_location(self, finished_products_location):
        self.highlight(self.find_element(By.XPATH, ErpLocator.finished_product_location_box))
        self.find_element(By.XPATH, ErpLocator.finished_product_location_box).click()
        lis = self.find_elements(By.XPATH, ErpLocator.finished_product_location_options)
        for li in lis:
            if "Search More..." == li.text:
                self.highlight(li)
                li.click()
                break
        ErpTransferPage.search_location(self, finished_products_location)

    def add_component(self, component1, component2, component3, consume1, consume2, consume3):
        components = (component1, component2, component3)
        consumes = (consume1, consume2, consume3)
        nums = (0, 1, 2)
        for num in nums:
            if not components[num] == "NULL":
                product = components[num].split('(')[0]
                pre_vintage = components[num].split('(')[1]
                vintage = pre_vintage.replace(")", "")
                self.click_add_line()
                self.search_product(product)
                ErpTransferPage.search_product_vintage(self, product, vintage)
                ErpTransferPage.add_demand_quantity(self, consumes[num])
                time.sleep(1)

    def search_product(self, product):
        log().info("Select products")
        self.highlight(self.find_element(By.CSS_SELECTOR, ErpLocator.orders_product_box))
        self.move_action("css_selector", ErpLocator.orders_product_box)
        time.sleep(2)
        lis = self.find_elements(By.XPATH, ErpLocator.orders_product_box_options)
        for li in lis:
            if "Search More..." == li.text:
                log().info("Click 'Search More...'")
                self.highlight(li)
                li.click()
                break
        time.sleep(2)

    def save_process(self):
        ErpTransferPage.click_save_button(self)
        log().info("Click the 'Make as to do' button")
        self.highlight(self.find_element(By.CSS_SELECTOR, ErpLocator.confirm_button))
        self.find_element(By.CSS_SELECTOR, ErpLocator.confirm_button).click()
        time.sleep(1)
        self.wait_element(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ErpLocator.make_as_done)))
        self.highlight(self.find_element(By.CSS_SELECTOR, ErpLocator.make_as_done))
        self.find_element(By.CSS_SELECTOR, ErpLocator.make_as_done).click()
        time.sleep(1)
        log().info("Click the 'Apply' button")
        self.wait_element(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ErpLocator.apply)))
        self.highlight(self.find_element(By.CSS_SELECTOR, ErpLocator.apply))
        self.find_element(By.CSS_SELECTOR, ErpLocator.apply).click()

    def click_add_line(self):
        self.highlight(self.find_element(By.XPATH, ErpLocator.orders_add_line))
        self.find_element(By.XPATH, ErpLocator.orders_add_line).click()
        time.sleep(2)

    def check_product_quantity_vintage_category(self, product, vintage, category):
        ErpCreateProductPage.select_products_dropdown(self)
        ErpCreateProductPage.search_products_by_product_name(self, product)
        self.highlight(self.find_element(By.CSS_SELECTOR, ErpLocator.product_item))
        self.click("css_selector", ErpLocator.product_item)
        ErpCreateProductPage.go_variants(self)
        qty = self.get_vintage_category_qty(vintage, category)
        return qty

    def get_vintage_category_qty(self, vintage, category):
        qty = self.find_element(By.XPATH, ErpLocator.vintage_category_qty_on_hand.
                                format(vintage, category)).text
        return qty

    @staticmethod
    def get_product_name(product):
        return product.split("(")[0]

    @staticmethod
    def get_vintage(product):
        pro_sub = product.split("(")[1]
        return pro_sub.split(",")[0]

    @staticmethod
    def get_category(product):
        pro_sub = product.split("(")[1]
        return pro_sub.replace(")", "")

    @staticmethod
    def get_category_bulk_wine(product):
        pro_sub = product.split("(")[1]
        category_sub = pro_sub.split(",")[1]
        category = category_sub.replace(")", "")
        return category
