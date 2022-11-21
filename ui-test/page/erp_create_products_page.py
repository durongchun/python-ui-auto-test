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


# ERP页面类
class ErpCreateProductPage(PageCommon):
    def __init__(self, driver=None):
        super().__init__(driver)

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

    def go_product(self):
        BrowserCommon.jump_to(self, ErpData.product_url)
        time.sleep(2)
        self.page_has_loaded()

    def go_inventory(self):
        self.driver.refresh()
        element_present = expected_conditions.presence_of_element_located((By.XPATH, ErpLocator.inventory_app))
        self.wait_element(element_present)
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
        prod_name = product_name + " (T" + str(self.random_number()) + ")"
        self.driver.find_element(By.XPATH, ErpLocator.create).click()
        self.driver.find_element(By.NAME, ErpLocator.product_name).send_keys(prod_name)
        self.driver.find_element(By.NAME, ErpLocator.barcode).send_keys(barcode)
        self.driver.find_element(By.NAME, ErpLocator.rfid_number).send_keys(frid_number)
        self.driver.find_element(By.XPATH, ErpLocator.save_button).click()
        time.sleep(2)
        self.page_has_loaded()

    def get_product_url(self):
        return self.get_url()

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
        self.wait_element(expected_conditions.presence_of_element_located((By.XPATH, ErpLocator.apply_button)))
        self.driver.find_element(By.XPATH, ErpLocator.apply_button).click()
        time.sleep(3)
        self.page_has_loaded()

    def update_and_validate_vintage_quantity(self, url, vintage1, vintage2, vintage3,
                                             vintage4, vintage5, vintage6, vintage7, warehouse_name,
                                             location_name, quantity1, quantity2, quantity3, quantity4,
                                             quantity5, quantity6, quantity7):
        time.sleep(2)
        self.wait_element(expected_conditions.presence_of_all_elements_located
                          ((By.XPATH, ErpLocator.vintage_values)))
        lis = self.driver.find_elements(By.XPATH, ErpLocator.vintage_values)
        print("vintage lis: " + str(len(lis)))
        qty = (quantity1, quantity2, quantity3, quantity4, quantity5, quantity6, quantity7)
        vintage = (str(vintage1), str(vintage2), str(vintage3), str(vintage4), str(vintage5),
                   str(vintage6), str(vintage7))

        for index in range(len(lis)):
            vintage_text = lis[index].text
            li = vintage_text.split(":")[1].strip()
            if li in vintage:
                time.sleep(2)
                lis[index].click()
                self.update_quantity(warehouse_name, location_name, qty[index])
                self.back_to_variants_page(url)
            self.wait_element(expected_conditions.presence_of_all_elements_located
                              ((By.XPATH, ErpLocator.vintage_values)))
            self.validate_vintage_quantity(vintage[index], qty[index])
            lis = self.driver.find_elements(By.XPATH, ErpLocator.vintage_values)

    def validate_all_vintage_qty(self, quantity1, quantity2, quantity3, quantity4, quantity5, quantity6, quantity7):
        qtys = (quantity1, quantity2, quantity3, quantity4, quantity5, quantity6, quantity7)
        all_qty = 0
        for qty in qtys:
            if qty != 'NULL':
                all_qty = all_qty + qty

        qty = self.driver.find_element(By.XPATH, ErpLocator.qty_on_hand).text
        print("qty on hand: " + qty.replace(',', ''))
        print("all qty from data: " + str(all_qty))
        assert qty.replace(',', '') == str(PageCommon.convert_to_decimal(all_qty))

    def validate_vintage_quantity(self, vintage, quantity):
        self.driver.refresh()
        self.page_has_loaded()
        self.wait_element(expected_conditions.presence_of_element_located
                          ((By.XPATH, ErpLocator.vintage_qty_on_hand.format(vintage))))
        qty = self.driver.find_element(By.XPATH, ErpLocator.vintage_qty_on_hand.format(vintage)).text
        print("xpath: " + qty.replace(',', ''))
        print("vintage qty in ERP: " + qty)
        assert qty.replace(',', '') == str(PageCommon.convert_to_decimal(quantity))

    def back_to_variants_page(self, url):
        BrowserCommon.jump_to(self, url)
        self.driver.refresh()
        time.sleep(4)
        self.page_has_loaded()

    def go_variants(self):
        self.wait_element(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, ErpLocator.variants)))
        self.driver.find_element(By.CSS_SELECTOR, ErpLocator.variants).click()
        time.sleep(2)
        self.page_has_loaded()

    def add_attributes(self, vintage1, vintage2, vintage3, vintage4, vintage5, vintage6, vintage7):
        self.driver.find_element(By.XPATH, ErpLocator.attributes_Variants).click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, ErpLocator.add_line).click()
        time.sleep(2)
        self.select_attribute("Vintage")
        self.select_vintage_value(vintage1, vintage2, vintage3, vintage4, vintage5, vintage6, vintage7)
        self.wait_element(expected_conditions.presence_of_element_located((By.XPATH, ErpLocator.save_button)))
        self.driver.find_element(By.XPATH, ErpLocator.save_button).click()
        time.sleep(4)

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

    def select_vintage_value(self, vintage1, vintage2, vintage3, vintage4, vintage5, vintage6, vintage7):
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

        self.select_years(vintage1, vintage2, vintage3, vintage4, vintage5, vintage6, vintage7)

    def select_years(self, vintage1, vintage2, vintage3, vintage4, vintage5, vintage6, vintage7):
        years = self.driver.find_elements(By.XPATH, ErpLocator.year_options)
        check_boxes = self.driver.find_elements(By.XPATH, ErpLocator.check_boxes)
        for index in range(len(years)):
            if years[index].text in (str(vintage1), str(vintage2), str(vintage3), str(vintage4),
                                     str(vintage5), str(vintage6), str(vintage7)):
                check_boxes[index].click()
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, ErpLocator.year_select_button).click()

    @staticmethod
    def get_location(warehouse_name, location_name):
        if warehouse_name == "Winery":
            location = "WH" + "/" + location_name
        return location

    def compare_to_quantity_on_hand(self, quantity1):
        self.driver.refresh()
        self.page_has_loaded()
        self.wait_element(expected_conditions.presence_of_element_located((By.XPATH, ErpLocator.qty_on_hand)))
        qty = self.driver.find_element(By.XPATH, ErpLocator.qty_on_hand).text
        if qty != str(quantity1):
            return False
        return qty == str(quantity1)

    def back_product_page(self):
        self.wait_element(expected_conditions.presence_of_element_located
                          ((By.CSS_SELECTOR, ErpLocator.product_breadcrumb)))
        self.driver.find_element(By.CSS_SELECTOR, ErpLocator.product_breadcrumb).click()
        time.sleep(2)
        self.page_has_loaded()

    def go_product_page(self, url):
        self.jump_to(url)
        time.sleep(1)
        self.page_has_loaded()
