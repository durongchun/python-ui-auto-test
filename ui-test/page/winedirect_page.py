import os
import datetime
from typing import List, AnyStr
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from common.page_common import PageCommon
from util.postgresql_tool import PostgreSQLTool
from winedirect_data import WineDirectData
from winedirect_locator import WineDirectLocator
import pandas as pd


class WineDirectPage(PageCommon):
    # container world首页进入页面操作
    def __init__(self, driver=None):
        super().__init__(driver)
        self.summary_date = None

    # login
    def login_ecommerce(self):
        actions = ActionChains(self.driver)
        actions.move_to_element(self.driver.find_element(By.CSS_SELECTOR, WineDirectLocator.login_link)). \
            click_and_hold().perform()
        self.driver.find_element(By.LINK_TEXT, WineDirectLocator.ecommerce).click()
        self.driver.find_element(By.ID, WineDirectLocator.user_name).click()
        self.driver.find_element(By.ID, WineDirectLocator.user_name).send_keys(WineDirectData.user)
        self.driver.find_element(By.ID, WineDirectLocator.pass_word).send_keys(WineDirectData.passwd)
        self.driver.implicitly_wait(500)
        self.driver.find_element(By.ID, WineDirectLocator.login_btn).click()
        self.page_has_loaded()
        self.driver.implicitly_wait(500)

    # go store
    def go_store(self):
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.XPATH, WineDirectLocator.store).click()

    # select dropdown list
    def select_inventory(self):
        ActionChains(self.driver).move_to_element(self.driver.find_element(By.XPATH, WineDirectLocator.inventory_link)) \
            .click_and_hold().perform()
        self.driver.find_element(By.CSS_SELECTOR, WineDirectLocator.client_resources).click()
        self.driver.implicitly_wait(3)
        self.driver.find_element(By.LINK_TEXT, WineDirectLocator.online_tools).click()

    # request inventory page
    def get_inventory_data(self):
        self.driver.get(WineDirectData.inventory_url)
        self.summary_date = datetime.datetime.now().date()
        conn = PostgreSQLTool.get_connection_staging_db(self)
        cursor = conn.cursor()
        PostgreSQLTool.clear_wd_data(cursor, conn)

        for index in range(1, 130):
            df = pd.read_html(self.driver.page_source, attrs={'class': 'table table-hover table-striped'})
            df_result = pd.concat(df, ignore_index=True)
            file_path = "C:\\Users\\Public\\Crawl_data.csv"
            df_result.to_csv(file_path, index=False, header=False)

            self.open_and_process_file(conn, file_path, self.summary_date)
            self.driver.find_element(By.XPATH, WineDirectLocator.next_link).click()
            self.page_has_loaded()
            self.driver.implicitly_wait(20)

        PostgreSQLTool.release_postgresql_conn(conn, cursor)

    # open file & process file
    @staticmethod
    def open_and_process_file(conn, file_path, summary_date):
        if os.path.exists(file_path):
            f = open(file_path, "rb")
            lines: List[AnyStr] = f.readlines()
            item_tuple = []
            for line in lines:
                cols = line.decode("latin1").split(",")
                print(cols)

                product_name = ("%s" % cols[0]).strip()
                sku_id = ("%s" % cols[1]).strip()

                product_id = sku_id
                vintage = "NA"
                sku_id_split = sku_id.split("-")
                if len(sku_id_split) > 1 and sku_id[:1].isdigit():
                    vintage = sku_id_split[1].strip()
                    product_id = sku_id_split[0].strip()
                    if not (vintage.isdigit() and product_id.isdigit()):
                        vintage = "NA"
                        if not product_id.isdigit():
                            product_id = sku_id
                    elif len(vintage) > 4:
                        print("WARN: length of vintage is : ", len(vintage))

                count = ("%s" % cols[4]).strip().replace(',', '')
                threshold = ("0%s" % cols[5]).strip().replace(',', '')
                active = "Yes"
                pool = ("%s" % cols[3]).strip().replace(',', '')

                inventory_datas = ['WineDirect', sku_id.lstrip('0'), product_name, product_id.lstrip('0'), '', pool,
                                   'NA',  summary_date, count, 0]
                # print("line data product name = " + product_name)
                item_tuple.append(inventory_datas)

            PostgreSQLTool.write_to_db_stock_quantity(conn, item_tuple)
