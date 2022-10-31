import os
import time
import datetime
from aifc import Error
from typing import List, AnyStr

from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from common.page_common import PageCommon
from data.containerworld_data import ContainerWorldMainData
from locator.containerworld_locator import ContainerWorldMainLocator
from util.postgresql_tool import PostgreSQLTool


# container world首页页面类
class ContainerWorldMainPage(PageCommon):
    # container world首页进入页面操作
    def __init__(self, driver=None):
        super().__init__(driver)
        self.download_file = None
        self.download_dir = None
        self.summary_date = ""

    def jump_to(self):
        self.driver.get(ContainerWorldMainData.url)

    # login
    def login(self, username, password):
        actions = ActionChains(self.driver)
        actions.move_to_element(self.driver.find_element(By.ID, ContainerWorldMainLocator.user_name)). \
            click_and_hold().perform()
        self.driver.find_element(By.ID, ContainerWorldMainLocator.user_name2).send_keys(username)
        actions.move_to_element(self.driver.find_element(By.CSS_SELECTOR, ContainerWorldMainLocator.
                                                         pass_word)).click_and_hold().perform()
        self.driver.find_element(By.CSS_SELECTOR, ContainerWorldMainLocator.pass_word2). \
            send_keys(password)
        self.driver.find_element(By.NAME, ContainerWorldMainLocator.login_btn).click()

    # select dropdown list
    def select_online_tools(self):
        self.driver.find_element(By.CSS_SELECTOR, ContainerWorldMainLocator.client_resources).click()
        self.driver.implicitly_wait(3)
        self.driver.find_element(By.LINK_TEXT, ContainerWorldMainLocator.online_tools).click()

    # select PDS Product Inventory by SKU
    def select_pds_product_inventory_by_sku(self):
        self.driver.find_element(By.XPATH, ContainerWorldMainLocator.pds).click()
        self.driver.implicitly_wait(10)
        ActionChains(self.driver).move_to_element(
            self.driver.find_element(By.LINK_TEXT, "PDS Product Inventory by SKU")).click_and_hold().perform()
        self.driver.find_element(By.LINK_TEXT, "PDS Product Inventory by SKU").click()
        self.driver.implicitly_wait(5)
        self.page_has_loaded()

    # select PDS Product Available Inquiry
    def select_pds_product_available_inquiry(self):
        self.driver.find_element(By.XPATH, ContainerWorldMainLocator.pds).click()
        self.driver.implicitly_wait(10)
        ActionChains(self.driver).move_to_element(
            self.driver.find_element(By.LINK_TEXT, "PDS Product Available Inquiry")).click_and_hold().perform()
        self.driver.find_element(By.LINK_TEXT, "PDS Product Available Inquiry").click()
        self.driver.implicitly_wait(5)
        self.page_has_loaded()

    # select warehouse and download csv
    def select_warehouse(self):
        self.download_dir = os.path.expanduser("~") + "/Downloads/"
        self.download_file = "rwservlet.csv"
        self.summary_date = datetime.datetime.now().date()
        conn = PostgreSQLTool.get_connection(self)
        cursor = conn.cursor()
        if self.is_rust_existing():
            PostgreSQLTool.clear_cw_rust_data(cursor, conn)
        else:
            PostgreSQLTool.clear_cw_mtb_data(cursor, conn)

        obj_select: Select = Select(self.driver.find_element(By.NAME, "whse_list"))
        wh = ["Commercial Logistics Vancouver", "Richmond Distribution Centre", "Kelowna Distribution",
              "Kelowna Storage"]

        for i, opt in enumerate(wh):
            obj_select.select_by_visible_text(opt)
            print("processing for WH: ", opt)
            self.driver.implicitly_wait(20)
            # download file
            download_element = self.driver.find_element(
                By.XPATH, ContainerWorldMainLocator.download_file)
            # file_path = "E:\\Chuny\\Downloads\\rwservlet.csv"
            file_path = self.download_dir + self.download_file

            if os.path.exists(file_path):
                os.remove(file_path)
            # prints parent window title
            print("Parent window title: " + self.driver.title)
            # get current window handle
            p = self.driver.current_window_handle

            download_element.click()
            self.close_windows()
            self.process_file(conn, file_path, self.summary_date)
            self.driver.find_element(By.NAME, "whse_list")

        PostgreSQLTool.release_postgresql_conn(conn, cursor)

    # process file for different company
    def process_file(self, conn, file_path, summary_date):
        if self.is_rust_existing():
            self.open_and_process_file_rust(conn, file_path, summary_date)
        else:
            self.open_and_process_file(conn, file_path, summary_date)

    # get first child window
    def close_windows(self):
        p = self.driver.current_window_handle
        child_wnd = self.driver.window_handles
        for w in child_wnd:
            # switch focus to child window
            if w != p:
                self.driver.switch_to.window(w)
                print("Child window title: " + self.driver.title)
                self.driver.switch_to.frame(0)
                WebDriverWait(self.driver, 20).until(
                    expected_conditions.text_to_be_present_in_element((By.XPATH,
                                                                       ContainerWorldMainLocator.download_complete),
                                                                      "DOWNLOAD COMPLETED"))
                self.driver.close()
                self.driver.switch_to.window(p)
                break
                time.sleep(0.9)

        self.driver.implicitly_wait(20)
        time.sleep(2)

    def is_rust_existing(self):
        try:
            WebDriverWait(self.driver, 20).until(
                expected_conditions.presence_of_element_located(
                    (By.XPATH, ContainerWorldMainLocator.rust_wine_co)))

        except TimeoutException as ex:
            print("Exception has been thrown. " + str(ex))
            return False
        else:
            return True

    # open file & process file
    def open_and_process_file(self, conn, file_path, summary_date):
        if os.path.exists(file_path):
            f = open(file_path, "rb")
            lines: List[AnyStr] = f.readlines()
            item_tuple = []
            for line in lines:
                cols = line.decode("latin1").split(",")
                print(cols)

                product_name = ("%s" % cols[3]).strip()
                product_num = ("%s" % cols[2]).strip()
                sku_num = ("%s" % cols[1]).strip()

                product_id = product_num
                vintage = "NA"
                if len(sku_num) > len(product_num):
                    vintage = sku_num[len(product_num):]
                # if len(product_id.split("-")) > 1:
                #     vintage = product_id.split("-")[1].strip()
                #     product_id = product_id.split("-")[0].strip()

                count = ("%s" % cols[6]).strip().replace(',', '')
                avail_count = ("%s" % cols[10]).strip().replace(',', '')
                threshold = 0  # ("0%s" % td_array[5].text).strip().replace(',', '')
                active = "Yes"
                # if td_array[2].text:
                #     active = td_array[2].text.strip()
                warehouse = cols[5].strip()  # wh / location
                prod_size = cols[4].strip()  # size

                company_name = 'CW-' + ContainerWorldMainData.company

                inventory_datas = ['CW', sku_num.lstrip('0'), product_name, product_id.lstrip('0'), company_name,
                                   warehouse, 'N/A', 'N/A',
                                   summary_date,
                                   count, 0]
                print("line data product name=" + product_name + "  sku_id=" + sku_num + "   location" + warehouse +
                      "   product_id" + product_id)
                item_tuple.append(inventory_datas)

            PostgreSQLTool.write_to_db_stock_quantity(conn, item_tuple)

            f.close()
        else:
            print("The download_file does not exist: ", file_path)

        self.driver.implicitly_wait(3)
        time.sleep(3)

    # open file & process file
    @staticmethod
    def open_and_process_file_rust(conn, file_path, summary_date):
        if os.path.exists(file_path):
            f = open(file_path, "rb")
            lines: List[AnyStr] = f.readlines()
            item_tuple = []
            for line in lines:
                cols = line.decode("latin1").split(",")
                print(cols)

                vintage = ("%s" % cols[2]).strip()
                product_name = ("%s" % cols[1]).strip()
                sku_id = ("%s" % cols[0]).strip()
                product_id = sku_id

                if len(vintage) > 1:
                    if vintage.isdigit() and len(vintage) == 4:
                        vintage = vintage[2:]
                        sku_id = product_id + "-" + vintage

                count = ("%s" % cols[5]).strip().replace(',', '')
                prod_avail = ("%s" % cols[8]).strip().replace(',', '')
                threshold = 0
                active = "Yes"
                warehouse = cols[17].strip()  # wh / location
                prod_size = ""  # size
                company_name = 'CW-' + ContainerWorldMainData.company2

                inventory_datas = ['CW', sku_id.lstrip('0'), product_name, product_id.lstrip('0'), company_name,
                                   warehouse, 'N/A', 'N/A',
                                   summary_date,
                                   count, 0]
                item_tuple.append(inventory_datas)

            PostgreSQLTool.write_to_db_stock_quantity(conn, item_tuple)

            f.close()
        else:
            print("The download_file does not exist: ", file_path)
