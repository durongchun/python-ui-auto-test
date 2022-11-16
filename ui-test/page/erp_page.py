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
        self.driver.implicitly_wait(500)
        self.driver.find_element(By.XPATH, ErpLocator.login_btn).click()
        self.driver.implicitly_wait(1500)
        self.page_has_loaded()

    def wait_element_presence(self):
        try:
            element_present = expected_conditions.presence_of_element_located((By.XPATH, ErpLocator.inventory_app))
            WebDriverWait(self.driver, 30).until(element_present)
        except TimeoutException:
            print("Timed out waiting for page to load")

    def go_product(self):
        BrowserCommon.jump_to(self, ErpData.product_url)

    def go_inventory(self):
        self.driver.refresh
        self.wait_element_presence()
        self.driver.find_element(By.XPATH, ErpLocator.inventory_app).click()
        self.driver.implicitly_wait(20)
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

    def create_product(self, product_name, product_id):
        frid_number = str(product_id) + str(self.random_number())
        prod_name = product_name + str(self.random_number())
        self.driver.find_element(By.XPATH, ErpLocator.create).click()
        self.driver.find_element(By.NAME, ErpLocator.product_name).send_keys(product_name)
        self.driver.find_element(By.NAME, ErpLocator.rfid_number).send_keys(frid_number)
        self.driver.find_element(By.XPATH, ErpLocator.save_button).click()

    def update_quantity(self, location_name, quantity1, quantity2, vintage1, vintage2):
        if vintage1 != 'NULL':
            self.driver.find_element(By.XPATH, ErpLocator.variants).click()
            self.driver.find_element(By.XPATH, ErpLocator.values_box.format(vintage1)).click

        else:
            self.driver.find_element(By.NAME, ErpLocator.update_quantity).click()
            self.driver.find_element(By.XPATH, ErpLocator.create_qty).click()
            self.driver.find_element(By.XPATH, ErpLocator.location_box).send_keys(location_name)
            self.driver.find_element(By.XPATH, ErpLocator.counted_qty).send_keys(quantity1)
            self.driver.find_element(By.XPATH, ErpLocator.save_record_button).click()
            self.driver.find_element(By.XPATH, ErpLocator.apply_button).click()

    def add_attributes(self, vintage1, vintage2):
        action = ActionChains(self.driver)
        self.driver.find_element(By.XPATH, ErpLocator.attributes_Variants).click()
        self.driver.implicitly_wait(30)
        self.driver.find_element(By.XPATH, ErpLocator.add_line).click()
        self.select_attribute("Vintage")
        ele = self.driver.find_element(By.XPATH, ErpLocator.values_box)
        ActionChains(self.driver).move_to_element(ele).click(ele).perform()
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.XPATH, ErpLocator.values_box).send_keys(vintage1)
        self.driver.find_element(By.XPATH, ErpLocator.values2_box).send_keys(Keys.ENTER)
        ActionChains(self.driver).move_to_element(ele).click(ele).perform()
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.XPATH, ErpLocator.values2_box).send_keys(vintage2)
        self.driver.find_element(By.XPATH, ErpLocator.values2_box).send_keys(Keys.ENTER)

        # element = self.driver.find_element(By.XPATH, ErpLocator.attribute_box)
        # self.driver.execute_script("arguments[0].click()", element)
        # self.driver.find_element(By.XPATH, ErpLocator.attribute_box).send_keys("Vintage")
        # self.driver.implicitly_wait(30)
        # self.driver.find_element(By.XPATH, ErpLocator.attribute_box).send_keys(Keys.TAB)
        # self.driver.implicitly_wait(30)
        # self.driver.find_element(By.CSS_SELECTOR, ErpLocator.warning).click()
        # self.driver.find_element(By.XPATH, ErpLocator.values_box).click()
        # self.driver.find_element(By.XPATH, ErpLocator.values_box).send_keys(vintage1)
        # # self.driver.implicitly_wait(30)
        # # self.driver.find_element(By.CSS_SELECTOR, ErpLocator.warning).click()
        # self.driver.find_element(By.XPATH, ErpLocator.values_box).send_keys(Keys.ENTER)
        # self.driver.implicitly_wait(30)
        # # self.driver.find_element(By.XPATH, ErpLocator.values2_box).click()
        # self.driver.find_element(By.XPATH, ErpLocator.values2_box).send_keys(vintage2)
        # self.driver.implicitly_wait(30)
        # self.driver.find_element(By.XPATH, ErpLocator.values2_box).send_keys(Keys.ENTER)
        # self.driver.implicitly_wait(30)
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
            for element in elements:
                self.action_delete(element)
                self.page_has_loaded()

    def action_delete(self, element):
        action = ActionChains(self.driver)
        action.move_to_element(element).click_and_hold().perform()
        element.click()
        action.move_to_element(self.driver.find_element(By.CSS_SELECTOR, ErpLocator.delete)).click_and_hold().perform()
        self.driver.find_element(By.CSS_SELECTOR, ErpLocator.delete).click()
        self.driver.find_element(By.XPATH, ErpLocator.ok_confirm).click()

    def search_products_by_product_name(self, product_name):
        self.driver.find_element(By.CSS_SELECTOR, ErpLocator.products_input).send_keys(product_name)
        self.driver.find_element(By.CSS_SELECTOR, ErpLocator.products_input).send_keys(Keys.ENTER)

    def is_product_showing(self):
        try:
            self.driver.find_element(By.CSS_SELECTOR, ErpLocator.products_details)
        except NoSuchElementException:
            print("is not _product_showing")
            return False
        else:
            print("is product_showing")
            return True

    def select_attribute(self, Vintage):
        # 激活下拉框
        ele = self.driver.find_element(By.XPATH, ErpLocator.attribute_box)
        ActionChains(self.driver).move_to_element(ele).click(ele).perform()
        self.driver.implicitly_wait(10)
        # 提取此下拉框中的所有元素
        lis = self.driver.find_elements(By.XPATH, "//ul[contains(@class,'ui-autocomplete dropdown-menu ui-front')]//li//a")
        # 判断需要的元素在哪里，点击
        for li in lis:
            if Vintage in li.text:
                print(li.text)
                li.click()
                break
        self.driver.implicitly_wait(30)

    def select_vintage_value(self, Vintage):
        # 激活下拉框
        ele = self.driver.find_element(By.XPATH, ErpLocator.attribute_box)
        ActionChains(self.driver).move_to_element(ele).click(ele).perform()
        self.driver.implicitly_wait(10)
        # 提取此下拉框中的所有元素
        lis = self.driver.find_elements(By.XPATH,
                                        "//ul[contains(@class,'ui-autocomplete dropdown-menu ui-front')]//li//a[1]")
        # 判断需要的元素在哪里，点击
        for li in lis:
            if "Search More..." in li.text:
                print(li.text)
                li.click()
                break
        self.driver.implicitly_wait(30)