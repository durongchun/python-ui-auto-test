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


# ERP页面类
class ErpPage(PageCommon):
    def __init__(self, driver=None):
        super().__init__(driver)

    # ERP首页进入页面操作
    def jump_to(self):
        self.driver.get("http://23.16.247.137:9069/web/login")

    def login(self, username, password):
        actions = ActionChains(self.driver)
        actions.move_to_element(self.driver.find_element(By.ID, ErpLocator.user_name)).click_and_hold().perform()
        self.driver.find_element(By.ID, ErpLocator.user_name).send_keys(username)
        actions.move_to_element(self.driver.find_element(By.ID, ErpLocator.pass_word)).click_and_hold().perform()
        self.driver.find_element(By.ID, ErpLocator.pass_word).send_keys(password)
        time.sleep(1)
        self.driver.find_element(By.XPATH, ErpLocator.login_btn).click()
        time.sleep(2)
        self.page_has_loaded()

    def wait_element_presence(self):
        try:
            element_present = expected_conditions.presence_of_element_located((By.XPATH, ErpLocator.inventory_app))
            WebDriverWait(self.driver, 30).until(element_present)
        except TimeoutException:
            print("Timed out waiting for page to load")

    def go_product(self):
        BrowserCommon.jump_to(self, ErpData.product_url)
        time.sleep(2)
        self.page_has_loaded()

    def go_inventory(self):
        self.driver.refresh()
        self.wait_element_presence()
        self.driver.find_element(By.XPATH, ErpLocator.inventory_app).click()
        time.sleep(2)
        self.page_has_loaded()

    def select_products_dropdown(self):
        actions = ActionChains(self.driver)
        try:
            element_present = expected_conditions.presence_of_element_located((By.XPATH, ErpLocator.products_dropdown))
            WebDriverWait(self.driver, 30).until(element_present)
        except TimeoutException:
            print("Timed out waiting for page to load")
        self.driver.find_element(By.XPATH, ErpLocator.products_dropdown).click()
        try:
            element_present = expected_conditions.presence_of_element_located((By.XPATH, ErpLocator.products_dropdown))
            WebDriverWait(self.driver, 30).until(element_present)
        except TimeoutException:
            print("Timed out waiting for page to load")
        actions.move_to_element(self.driver.find_element(By.XPATH, ErpLocator.products_dropdown)). \
            click_and_hold().perform()
        self.driver.find_element(By.XPATH, ErpLocator.products_dropdown).click()

    def create_product(self, product_name, product_id, upc):
        frid_number = str(product_id) + str(self.random_number())
        barcode = upc + str(self.random_number())
        self.driver.find_element(By.XPATH, ErpLocator.create).click()
        self.driver.find_element(By.NAME, ErpLocator.product_name).send_keys(product_name)
        self.driver.find_element(By.NAME, ErpLocator.barcode).send_keys(barcode)
        self.driver.find_element(By.NAME, ErpLocator.rfid_number).send_keys(frid_number)
        self.driver.find_element(By.XPATH, ErpLocator.save_button).click()
        time.sleep(2)
        self.page_has_loaded()

    def update_quantity(self, warehouse_name, location_name, quantity1):
        self.driver.find_element(By.NAME, ErpLocator.update_quantity).click()
        self.driver.find_element(By.XPATH, ErpLocator.create_qty).click()
        location_name = self.get_location(warehouse_name, location_name)
        self.select_location(location_name)
        self.driver.find_element(By.XPATH, ErpLocator.counted_qty).clear()
        self.driver.find_element(By.XPATH, ErpLocator.counted_qty).send_keys(quantity1)
        self.driver.find_element(By.XPATH, ErpLocator.counted_qty).send_keys(Keys.ENTER)
        time.sleep(2)
        # self.driver.find_element(By.XPATH, ErpLocator.save_record_button).click()
        self.driver.find_element(By.CSS_SELECTOR, ErpLocator.apply_button).click()
        self.page_has_loaded()

    def update_vintage_quantity(self, vintage1, vintage2):
        variants = self.driver.find_elements(By.CSS_SELECTOR, ErpLocator.variant_value)
        for variant in variants:
            if vintage1 == variant.text:
                variant.click()



    def go_variants(self):
        self.driver.find_element(By.CSS_SELECTOR, ErpLocator.variants)
        self.page_has_loaded()

    def dd_attributes(self, vintage1, vintage2):
        action = ActionChains(self.driver)
        self.driver.find_element(By.XPATH, ErpLocator.attributes_Variants).click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, ErpLocator.add_line).click()
        time.sleep(2)
        self.select_attribute("Vintage")
        self.select_vintage_value(vintage1, vintage2)
        self.driver.find_element(By.XPATH, ErpLocator.save_button).click()

    def add_vintage_quantity(self, vintage, product_code):
        self.driver.find_element(By.XPATH, ErpLocator.values_box.format(vintage)).click
        self.driver.find_element(By.XPATH, ErpLocator.internal_reference_box).send_keys(product_code)
        self.driver.find_element(By.XPATH, ErpLocator.barcode_box).send_keys(product_code)
        self.driver.find_element(By.XPATH, ErpLocator.save_record_button)

    def clear_products(self, product_name, products_by_xpath):
        self.search_products_by_product_name(product_name)
        if self.is_product_showing():
            elements = self.driver.find_elements(By.CSS_SELECTOR, products_by_xpath)
            action = ActionChains(self.driver)
            action.move_to_element(elements[0]).click_and_hold().perform()
            elements[0].click()
            self.page_has_loaded()
            for index in range(len(elements)):
                self.action_delete()
                time.sleep(2)
                break

    def action_delete(self):
        action = ActionChains(self.driver)
        self.driver.find_element(By.CSS_SELECTOR, ErpLocator.action).click()
        action.move_to_element(self.driver.find_element(By.CSS_SELECTOR, ErpLocator.delete)).click_and_hold().perform()
        self.driver.find_element(By.CSS_SELECTOR, ErpLocator.delete).click()
        self.driver.find_element(By.XPATH, ErpLocator.ok_confirm).click()
        time.sleep(2)
        self.page_has_loaded()
        # self.driver.find_element(By.CSS_SELECTOR, ErpLocator.action)

    def search_products_by_product_name(self, product_name):
        self.driver.find_element(By.CSS_SELECTOR, ErpLocator.products_input).send_keys(product_name)
        self.driver.find_element(By.CSS_SELECTOR, ErpLocator.products_input).send_keys(Keys.ENTER)
        self.page_has_loaded()
        time.sleep(2)

    def is_product_showing(self):
        try:
            self.driver.find_element(By.CSS_SELECTOR, ErpLocator.products_details)
        except NoSuchElementException:
            print("is not _product_showing")
            return False
        else:
            print("is product_showing")
            return True

    def select_location(self, location):
        # 激活下拉框
        ele = self.driver.find_element(By.CSS_SELECTOR, ErpLocator.location_box)
        ActionChains(self.driver).move_to_element(ele).click(ele).perform()
        time.sleep(2)
        # 提取此下拉框中的所有元素
        lis = self.driver.find_elements(By.XPATH, ErpLocator.vintage_dropdown_options)
        # 判断需要的元素在哪里，点击
        for li in lis:
            if "Search More..." in li.text:
                print(li.text)
                li.click()
                break
        time.sleep(2)

        self.driver.find_element(By.CSS_SELECTOR, ErpLocator.location_search_box).send_keys(location)
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, ErpLocator.location_search_box).send_keys(Keys.ENTER)
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, ErpLocator.location_search_result).click()
        time.sleep(2)

    def select_attribute(self, vintage):
        # 激活下拉框
        ele = self.driver.find_element(By.XPATH, ErpLocator.attribute_box)
        ActionChains(self.driver).move_to_element(ele).click(ele).perform()
        time.sleep(2)
        # 提取此下拉框中的所有元素
        lis = self.driver.find_elements(By.XPATH, ErpLocator.attribute_dropdown_options)
        # 判断需要的元素在哪里，点击
        for li in lis:
            if vintage in li.text:
                print(li.text)
                li.click()
                break
        time.sleep(2)

    def select_vintage_value(self, vintage1, vintage2):
        # 激活下拉框
        ele = self.driver.find_element(By.XPATH, ErpLocator.values_box)
        ActionChains(self.driver).move_to_element(ele).click(ele).perform()
        time.sleep(2)
        # 提取此下拉框中的所有元素
        lis = self.driver.find_elements(By.XPATH, ErpLocator.vintage_dropdown_options)
        # 判断需要的元素在哪里，点击
        for li in lis:
            if "Search More..." in li.text:
                print(li.text)
                li.click()
                break
        time.sleep(2)

        self.select_years(vintage1, vintage2)

    def select_years(self, vintage1, vintage2):
        years = self.driver.find_elements(By.XPATH, ErpLocator.year_options)
        check_boxes = self.driver.find_elements(By.XPATH, ErpLocator.check_boxes)
        for index in range(len(years)):
            if years[index].text in (str(vintage1), str(vintage2)):
                check_boxes[index].click()
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, ErpLocator.year_select_button).click()

    @staticmethod
    def get_location(warehouse_name, location_name):
        if warehouse_name == "Winery":
            location = "WH" + "/" + location_name
        return location

    def validate_quantity_on_hand(self, quantity1):
        self.driver.refresh()
        self.page_has_loaded()
        qty = self.driver.find_element(By.XPATH, ErpLocator.qty_on_hand).text
        assert qty == quantity1
        print("The added quantity is showing: " + qty)

    def back_product_page(self):
        self.driver.find_element(By.CSS_SELECTOR, ErpLocator.product_breadcrumb).click()
        self.page_has_loaded()
