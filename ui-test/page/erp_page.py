from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from common.page_common import PageCommon
from erp_locator import ErpLocator


# ERP页面类
class ErpPage(PageCommon):
    def __init__(self, driver=None):
        super().__init__(driver)

    # ERP首页进入页面操作
    def jump_to(self):
        self.driver.get("http://23.16.247.137:9069/web/login")

    # 搜索数据
    def go_inventory(self):
        self.driver.find_element(By.XPATH, ErpLocator.inventory_app).click()
        self.driver.implicitly_wait(20)
        self.page_has_loaded()

    def select_products_dropdown(self):
        # WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located
        #                                      (By.XPATH, ErpLocator.products))
        actions = ActionChains(self.driver)
        self.driver.find_element(By.XPATH, ErpLocator.products).click()
        actions.move_to_element(self.driver.find_element(By.XPATH, ErpLocator.products_dropdown)). \
            click_and_hold().perform()
        self.driver.find_element(By.XPATH, ErpLocator.products_dropdown).click()

    def create_product(self, product_name, product_id):
        frid_number = str(product_id) + str(self.random_number())
        prod_name = product_name + str(self.random_number())
        self.driver.find_element(By.XPATH, ErpLocator.create).click()
        self.driver.find_element(By.NAME, ErpLocator.product_name).send_keys(prod_name)
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
        self.driver.find_element(By.XPATH, ErpLocator.attributes_Variants).click()
        self.driver.find_element(By.XPATH, ErpLocator.add_line).click()
        self.driver.find_element(By.XPATH, ErpLocator.attribute_box).send_keys("vintage")
        self.driver.find_element(By.XPATH, ErpLocator.values_box).send_keys(vintage1)
        self.driver.find_element(By.XPATH, ErpLocator.values_box).send_keys(vintage2)
        self.driver.find_element(By.XPATH, ErpLocator.save_button).click()

    def add_vintage_quantity(self, vintage, product_code):
        self.driver.find_element(By.XPATH, ErpLocator.values_box.format(vintage)).click
        self.driver.find_element(By.XPATH, ErpLocator.internal_reference_box).send_keys(product_code)
        self.driver.find_element(By.XPATH, ErpLocator.barcode_box).send_keys(product_code)
        self.driver.find_element(By.XPATH, ErpLocator.save_record_button)
