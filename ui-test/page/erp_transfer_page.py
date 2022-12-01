from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions

from erp_create_products_page import ErpCreateProductPage
from erp_locator import ErpLocator
import time

from log_tool import log
from page_common import PageCommon


# ERP页面类
class ErpTransferPage(PageCommon):
    def __init__(self, driver=None):
        super().__init__(driver)

    def go_transfer_page(self):
        log().info("Go Transfer page")
        self.wait_element(expected_conditions.presence_of_element_located((By.XPATH, ErpLocator.operations_menu)))
        self.highlight(self.find_element(By.XPATH, ErpLocator.operations_menu))
        self.active_dropdown(self.find_element(By.XPATH, ErpLocator.operations_menu))
        self.click_and_hold(self.find_element(By.XPATH, ErpLocator.transfer_dropdown_option))
        self.highlight(self.find_element(By.XPATH, ErpLocator.transfer_dropdown_option))
        self.find_element(By.XPATH, ErpLocator.transfer_dropdown_option).click()
        self.page_has_loaded()
        time.sleep(2)

    def select_operation_type(self, operation_type):
        log().info("Select the 'Operation Type'")
        time.sleep(1)
        self.highlight(self.find_element(By.CSS_SELECTOR, ErpLocator.operation_type))
        self.click("css_selector", ErpLocator.operation_type)
        time.sleep(1)
        lis = self.find_elements(By.XPATH, ErpLocator.operation_type_dropdown_options)
        for li in lis:
            if operation_type == li.text:
                self.highlight(li)
                li.click()
                break
        time.sleep(1)

    def select_operation_type_search(self, operation_type, ware_house):
        log().info("Select the 'Operation Type' from searching results")
        time.sleep(1)
        self.highlight(self.find_element(By.CSS_SELECTOR, ErpLocator.operation_type))
        self.click("css_selector", ErpLocator.operation_type)
        time.sleep(1)
        lis = self.find_elements(By.XPATH, ErpLocator.operation_type_dropdown_options)
        for li in lis:
            if "Search More..." == li.text:
                self.highlight(li)
                li.click()
                break
        time.sleep(1)
        self.search_operation_type(operation_type, ware_house)

    def select_source_location(self, source_location):
        log().info("Select the 'Source location'")
        self.highlight(self.find_element(By.CSS_SELECTOR, ErpLocator.source_location))
        self.click("css_selector", ErpLocator.source_location)
        lis = self.find_elements(By.XPATH, ErpLocator.source_location_dropdown_options)
        for li in lis:
            if "Search More..." == li.text:
                self.highlight(li)
                li.click()
                break
        time.sleep(1)
        self.search_location(source_location)

    def select_destination_location(self, destination_location):
        log().info("Select the 'Destination location'")
        self.highlight(self.find_element(By.CSS_SELECTOR, ErpLocator.destination_location))
        self.click("css_selector", ErpLocator.destination_location)
        lis = self.find_elements(By.XPATH, ErpLocator.destination_location_dropdown_options)
        for li in lis:
            if "Search More..." == li.text:
                self.highlight(li)
                li.click()
                break
        time.sleep(1)
        self.search_location(destination_location)

    def click_add_line(self):
        log().info("Click the 'Add a line'")
        self.highlight(self.find_element(By.XPATH, ErpLocator.transfer_add_line))
        self.find_element(By.XPATH, ErpLocator.transfer_add_line).click()
        time.sleep(2)

    def select_product(self, product):
        log().info("Select products")
        self.highlight(self.find_element(By.XPATH, ErpLocator.transfer_product_box))
        self.move_action("xpath", ErpLocator.transfer_product_box)
        time.sleep(2)
        lis = self.find_elements(By.XPATH, ErpLocator.product_box_options)
        for li in lis:
            if "Search More..." == li.text:
                log().info("Click 'Search More...'")
                self.highlight(li)
                li.click()
                break
        time.sleep(2)
        self.search_product(product)

    def search_product(self, product):
        log().info("Search product and add it to line")
        self.highlight(self.driver.find_element(By.CSS_SELECTOR, ErpLocator.location_search_box))
        self.driver.find_element(By.CSS_SELECTOR, ErpLocator.location_search_box).send_keys(product)
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, ErpLocator.location_search_box).send_keys(Keys.ENTER)
        time.sleep(1)
        self.highlight(self.driver.find_element(By.CSS_SELECTOR, ErpLocator.product_search_result))
        self.driver.find_element(By.CSS_SELECTOR, ErpLocator.product_search_result).click()
        time.sleep(2)

    def select_delivery_address(self, deliver_address):
        self.active_dropdown((self.driver.find_element(By.CSS_SELECTOR, ErpLocator.deliver_address)))
        self.highlight(self.driver.find_element(By.CSS_SELECTOR, ErpLocator.deliver_address))
        lis = self.find_elements(By.XPATH, ErpLocator.deliver_address_dropdown_options)
        for li in lis:
            if "Search More..." == li.text:
                self.highlight(li)
                li.click()
                break
        self.search_location(deliver_address)

    def search_location(self, deliver_address):
        self.highlight(self.driver.find_element(By.CSS_SELECTOR, ErpLocator.location_search_box))
        self.driver.find_element(By.CSS_SELECTOR, ErpLocator.location_search_box).send_keys(deliver_address)
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, ErpLocator.location_search_box).send_keys(Keys.ENTER)
        time.sleep(1)
        self.highlight(self.driver.find_element(By.CSS_SELECTOR, ErpLocator.deliver_address_search_results))
        self.driver.find_element(By.CSS_SELECTOR, ErpLocator.deliver_address_search_results).click()
        time.sleep(2)

    def search_operation_type(self, operation_type, ware_house):
        self.highlight(self.driver.find_element(By.CSS_SELECTOR, ErpLocator.location_search_box))
        self.driver.find_element(By.CSS_SELECTOR, ErpLocator.location_search_box).send_keys(operation_type)
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, ErpLocator.location_search_box).send_keys(Keys.ENTER)
        time.sleep(1)
        self.highlight(self.find_element(By.XPATH, ErpLocator.operation_type_search_result.format(
            ware_house, operation_type)))
        self.active_dropdown(self.find_element(By.XPATH, ErpLocator.operation_type_search_result.format(
            ware_house, operation_type)))
        time.sleep(2)

    def click_create_button(self):
        log().info("Click the 'Create' button")
        self.highlight(self.driver.find_element(By.CSS_SELECTOR, ErpLocator.transfer_create_highlight))
        self.driver.find_element(By.XPATH, ErpLocator.create_button).click()

    def add_demand_quantity(self, demand):
        log().info("Add the quantity of demand")
        time.sleep(2)
        self.highlight(self.find_element(By.XPATH, ErpLocator.transfer_demand_box))
        self.input("xpath", ErpLocator.transfer_demand_box, demand)
        self.find_element(By.XPATH, ErpLocator.transfer_demand_box).send_keys(Keys.ENTER)

    def select_products_and_transfer(self, product1, product2, demand1, demand2):
        log().info("Select the product and add it to transfer")
        prods = (product1, product2)
        demands = (demand1, demand2)
        nums = (0, 1)
        for num in nums:
            if prods[num] == "":
                break
            self.click_add_line()
            self.select_product(prods[num])
            self.add_demand_quantity(demands[num])
            time.sleep(1)

        self.click_save_button()
        log().info("Click the 'Make as to do' button")
        self.highlight(self.find_element(By.CSS_SELECTOR, ErpLocator.make_as_to_do))
        self.find_element(By.CSS_SELECTOR, ErpLocator.make_as_to_do).click()
        time.sleep(1)
        log().info("Click the 'Validate' button")
        self.highlight(self.find_element(By.CSS_SELECTOR, ErpLocator.validate))
        self.find_element(By.CSS_SELECTOR, ErpLocator.validate).click()
        time.sleep(1)
        log().info("Click the 'Apply' button")
        self.highlight(self.find_element(By.CSS_SELECTOR, ErpLocator.apply))
        self.find_element(By.CSS_SELECTOR, ErpLocator.apply).click()

    def click_save_button(self):
        log().info("Click the Save button")
        self.highlight(self.find_element(By.CSS_SELECTOR, ErpLocator.save_button))
        self.find_element(By.CSS_SELECTOR, ErpLocator.save_button).click()
        time.sleep(1)

    def check_product_quantity(self, product, vintage):
        ErpCreateProductPage.select_products_dropdown(self)
        ErpCreateProductPage.search_products_by_product_name(self, product)
        self.highlight(self.find_element(By.CSS_SELECTOR, ErpLocator.product_item))
        self.click("css_selector", ErpLocator.product_item)
        ErpCreateProductPage.go_variants(self)
        qty = self.get_vintage_qty(vintage)
        return qty

    def get_vintage_qty(self, vintage):
        self.highlight(self.driver.find_element(By.XPATH, ErpLocator.vintage_qty_on_hand.format(vintage)))
        qty = self.driver.find_element(By.XPATH, ErpLocator.vintage_qty_on_hand.format(vintage)).text
        return qty

    @staticmethod
    def compare_to_qty_stock_in(origin_qty, current_qty, demand):
        ori_qty = origin_qty.strip().replace(',', '')
        cur_qty = current_qty.strip().replace(',', '')
        if float(cur_qty) == float(ori_qty) + float(demand):
            return True
        else:
            return False

    @staticmethod
    def compare_to_qty_stock_out(origin_qty, current_qty, demand):
        ori_qty = origin_qty.strip().replace(',', '')
        cur_qty = current_qty.strip().replace(',', '')
        if float(ori_qty) == float(cur_qty) + float(demand):
            return True
        else:
            return False

    def check_product_quantity_from_inventory_report(self, product_code, location):
        self.go_inventory_report()
        ErpCreateProductPage.search_products_by_product_name(self, product_code)
        self.highlight(self.find_element(By.CSS_SELECTOR, ErpLocator.top_category))
        self.find_element(By.CSS_SELECTOR, ErpLocator.top_category).click()
        self.highlight(self.find_element(By.XPATH, ErpLocator.location_category.format(location)))
        self.find_element(By.XPATH, ErpLocator.location_category.format(location)).click()
        available_qty = self.find_element(By.XPATH, ErpLocator.available_quantity.format(location)).text
        return available_qty

    def go_inventory_report(self):
        log().info("Go Inventory Report page")
        self.highlight(self.find_element(By.XPATH, ErpLocator.reporting))
        self.find_element(By.XPATH, ErpLocator.reporting).click()
        self.highlight(self.find_element(By.XPATH, ErpLocator.inventory_report_option))
        self.find_element(By.XPATH, ErpLocator.inventory_report_option).click()
        time.sleep(1)
        self.page_has_loaded()
