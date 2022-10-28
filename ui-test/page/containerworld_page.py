import os
import time
from aifc import Error
from datetime import datetime
from telnetlib import EC
from typing import List, AnyStr

from selenium.webdriver.common.by import By
from selenium.webdriver.common.devtools.v106 import browser
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

import containerworld_data
import driver
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
    def login(self):
        actions = ActionChains(self.driver)
        actions.move_to_element(self.driver.find_element(By.ID, ContainerWorldMainLocator.user_name)). \
            click_and_hold().perform()
        self.driver.find_element(By.ID, ContainerWorldMainLocator.user_name2).send_keys(ContainerWorldMainData.user)
        actions.move_to_element(self.driver.find_element(By.CSS_SELECTOR, ContainerWorldMainLocator.
                                                         pass_word)).click_and_hold().perform()
        self.driver.find_element(By.CSS_SELECTOR, ContainerWorldMainLocator.pass_word2). \
            send_keys(ContainerWorldMainData.passwd)
        self.driver.find_element(By.NAME, ContainerWorldMainLocator.login_btn).click()

    # select dropdown list
    def select_online_tools(self):
        self.driver.find_element(By.CSS_SELECTOR, "li:nth-child(6) > h1").click()
        self.driver.implicitly_wait(3)
        self.driver.find_element(By.LINK_TEXT, "Online Tools").click()

    # select PDS Product Inventory by SKU
    def select_pds_product_inventory_by_sku(self):
        self.driver.find_element(By.XPATH, "//div[@id='accordion']/h3[3]").click()
        self.driver.implicitly_wait(5)
        time.sleep(3)
        ActionChains(self.driver).move_to_element(
            self.driver.find_element(By.LINK_TEXT, "PDS Product Inventory by SKU")).click_and_hold().perform()
        self.driver.find_element(By.LINK_TEXT, "PDS Product Inventory by SKU").click()
        self.driver.implicitly_wait(5)
        self.page_has_loaded()

    # select warehouse and download csv
    def select_warehouse(self):
        self.download_dir = os.path.expanduser("~") + "/Downloads/"
        self.download_file = "rwservlet.csv"
        obj_select: Select = Select(self.driver.find_element(By.NAME, "whse_list"))
        wh = ["Commercial Logistics Vancouver", "Richmond Distribution Centre", "Kelowna Distribution",
              "Kelowna Storage"]

        for i, opt in enumerate(wh):
            obj_select.select_by_visible_text(opt)
            print("processing for WH: ", opt)
            self.driver.implicitly_wait(20)

            # download file
            download_element = self.driver.find_element(
                By.XPATH, "//img[@name='download_file']")

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
            self.open_and_process_file(file_path)
            self.driver.find_element(By.NAME, "whse_list")

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
                    expected_conditions.text_to_be_present_in_element((By.XPATH, "//html/body/center/h1[1]"),
                                                                      "DOWNLOAD COMPLETED"))
                self.driver.close()
                self.driver.switch_to.window(p)
                break
                time.sleep(0.9)

        self.driver.implicitly_wait(20)
        time.sleep(2)

    # open file & process file
    def open_and_process_file(self, file_path):
        # update_time = str(datetime.datetime.now())

        if os.path.exists(file_path):
            PostgreSQLTool.clear_ods_data(self)
            f = open(file_path, "rb")
            lines: List[AnyStr] = f.readlines()
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

                item_tuple = (
                    sku_num, product_id, product_name,
                    active, warehouse,
                    count, threshold, avail_count,
                    'CW-' + ContainerWorldMainData.company,
                    warehouse, prod_size, vintage,
                    self.summary_date, "")

                PostgreSQLTool.write_to_db(self, item_tuple)

            f.close()
        else:
            print("The download_file does not exist: ", file_path)

        self.driver.implicitly_wait(3)
        # self.driver.find_element(By.XPATH, "/html/body/div/div/div[1]/div[1]/div[2]/div/div[2]/a[4]").click()
        # self.driver.close()
        time.sleep(3)
