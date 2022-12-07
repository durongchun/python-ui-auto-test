#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import random
import time

from selenium.common import TimeoutException
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from decimal import Decimal
from selenium import webdriver

import driver
from common.browser_common import BrowserCommon


# Page 项目无关页面类封装基本页面操作
class PageCommon(BrowserCommon):

    ############################## 基本方法再封装 ##############################
    # 依据 xpath 找到指定元素
    def find_element_by_xpath(self, xpath):
        """
        通过 xpath 找元素
        :param xpath: 元素定位
        :return: 原生通过 xpath 找元素方法
        """
        return self.driver.find_element_by_xpath(xpath)

    # 找到指定元素
    def find_element(self, *args):
        """
        找元素
        :param args: 定位与通过什么定位
        :return: 原生找元素方法
        """
        return self.driver.find_element(*args)

    # 依据 xpath 找到指定的一批元素
    def find_elements_by_xpath(self, xpath):
        """
        通过 xpath 找多元素
        :param xpath: 多元素定位
        :return: 原生通过 xpath 找多元素方法
        """
        return self.driver.find_elements_by_xpath(xpath)

    # 找到指定的一批元素
    def find_elements(self, *args):
        """
        找多元素
        :param args: 定位与通过什么定位
        :return: 原生找多元素方法
        """
        return self.driver.find_elements(*args)

    ############################## 单个元素操作 ##############################
    # 点击元素
    def click_element_by_xpath(self, xpath):
        """
        点击元素
        :param xpath: 元素定位
        :return: 返回原生点击事件
        """
        # 显示等待元素可点击
        WebDriverWait(self.driver, 10, 0.1).until(expected_conditions.element_to_be_clickable(("xpath", xpath)))
        # 点击元素
        self.driver.find_element_by_xpath(xpath).click()

    # 输入框输入数据
    def input_by_xpath(self, xpath, value):
        """
        输入值
        :param xpath: 元素定位
        :param value: 输入值
        :return: 返回 send_keys 原生方法
        """
        # 显示等待元素可点击
        WebDriverWait(self.driver, 10, 0.1).until(expected_conditions.element_to_be_clickable(("xpath", xpath)))
        # 输入框输入数据
        self.driver.find_element_by_xpath(xpath).send_keys(value)

    # 输入内容方法
    def input(self, type, value, inputvalue):
        if type == "xpath":
            self.driver.find_element(By.XPATH, value).clear()
            self.driver.find_element(By.XPATH, value).send_keys(inputvalue)
        elif type == "class_name":
            self.driver.find_element(By.CLASS_NAME, value).clear()
            self.driver.find_element(By.CLASS_NAME, value).send_keys(inputvalue)
        elif type == "id":
            self.driver.find_element(By.ID, value).clear()
            self.driver.find_element(By.ID, value).send_keys(inputvalue)
        elif type == "name":
            self.driver.find_element(By.NAME, value).clear()
            self.driver.find_element(By.NAME, value).send_keys(inputvalue)
        elif type == "link_text":
            self.driver.find_element(By.LINK_TEXT, value).clear()
            self.driver.find_element(By.LINK_TEXT, value).send_keys(inputvalue)
        elif type == "partial_link_text":
            self.driver.find_element(By.PARTIAL_LINK_TEXT, value).clear()
            self.driver.find_element(By.PARTIAL_LINK_TEXT, value).send_keys(inputvalue)

    # 鼠标事件方法一
    def click(self, type, value):
        if type == "xpath":
            self.driver.find_element(By.XPATH, value).click()
        elif type == "class_name":
            self.driver.find_element(By.CLASS_NAME, value).click()
        elif type == "id":
            self.driver.find_element(By.ID, value).click()
        elif type == "name":
            self.driver.find_element(By.NAME, value).click()
        elif type == "link_text":
            self.driver.find_element(By.LINK_TEXT, value).click()
        elif type == "css_selector":
            self.driver.find_element(By.CSS_SELECTOR, value).click()
        elif type == "partial_link_text":
            self.driver.find_element(By.PARTIAL_LINK_TEXT, value).click()

    # 鼠标事件方法二
    def clear(self, type, value):
        if type == "xpath":
            self.driver.find_element(By.XPATH, value).clear()
        elif type == "id":
            self.driver.find_element(By.ID, value).clear()
        elif type == "name":
            self.driver.find_element(By.NAME, value).clear()
        elif type == "link_text":
            self.driver.find_element(By.LINK_TEXT, value).clear()
        elif type == "css_selector":
            self.driver.find_element(By.CSS_SELECTOR, value).clear()
        elif type == "partial_link_text":
            self.driver.find_element(By.PARTIAL_LINK_TEXT, value).clear()

    # 验证元素是否存在
    def check_element(self, type, value):
        if type == "xpath":
            self.driver.find_element(By.XPATH, value)
        elif type == "id":
            self.driver.find_element(By.ID, value)
        elif type == "name":
            self.driver.find_element(By.NAME, value)
        elif type == "link_text":
            self.driver.find_element(By.LINK_TEXT, value)
        elif type == "css_selector":
            self.driver.find_element(By.CSS_SELECTOR, value)
        elif type == "partial_link_text":
            self.driver.find_element(By.PARTIAL_LINK_TEXT, value)

    # 获取子元素
    def select_child_elements(self, type, value1, value2):
        if type == "xpath":
            self.highlight(self.find_element(By.XPATH, value1))
            Select(self.driver.find_element(By.XPATH, value1)).select_by_visible_text(value2)
        elif type == "id":
            self.highlight(self.find_element(By.ID, value1))
            Select(self.driver.find_element(By.ID, value1)).select_by_visible_text(value2)
        elif type == "name":
            self.highlight(self.find_element(By.NAME, value1))
            Select(self.driver.find_element(By.NAME, value1)).select_by_visible_text(value2)
        elif type == "link_text":
            self.highlight(self.find_element(By.LINK_TEXT, value1))
            Select(self.driver.find_element(By.LINK_TEXT, value1)).select_by_visible_text(value2)
        elif type == "partial_link_text":
            self.highlight(self.find_element(By.PARTIAL_LINK_TEXT, value1))
            Select(self.driver.find_element(By.PARTIAL_LINK_TEXT, value1)).select_by_visible_text(value2)
        elif type == "css_selector":
            self.highlight(self.find_element(By.CSS_SELECTOR, value1))
            Select(self.driver.find_element(By.CSS_SELECTOR, value1)).select_by_visible_text(value2)

    # 获取输入框的值
    def get_attribute(self, type, value1, value2):
        if type == "xpath":
            Value = self.driver.find_element_by_xpath(value1).get_attribute(value2)
            return Value
        elif type == "name":
            Value = self.driver.find_element_by_name(value1).get_attribute(value2)
            return Value
        elif type == "link_text":
            Value = self.driver.find_element_by_link_text(value1).get_attribute(value2)
            return Value
        elif type == "class_name":
            Value = self.driver.find_element_by_class_name(value1).get_attribute(value2)
            return Value
        elif type == "id":
            Value = self.driver.find_element_by_id(value1).get_attribute(value2)
            return Value

    # 获取下拉框的文本的值
    def get_text(self, type, value):
        if type == "xpath":
            text = self.driver.find_element(By.XPATH, value).text
            return text
        elif type == "name":
            text = self.driver.find_element(By.NAME, value).text
            return text
        elif type == "link_text":
            text = self.driver.find_element(By.LINK_TEXT, value).text
            return text
        elif type == "class_name":
            text = self.driver.find_element(By.CLASS_NAME, value).text
            return text
        elif type == "id":
            text = self.driver.find_element(By.ID, value).text
            return text
        elif type == "css_selector":
            text = self.driver.find_element(By.CSS_SELECTOR, value).text
            return text

    # 显性等待时间
    def webDriverWait(self, MaxTime: object, MinTime: object, value: object) -> object:
        element = self.driver.find_element(By.XPATH, value)
        WebDriverWait(self.driver, MaxTime, MinTime).until(expected_conditions.presence_of_element_located(element))

    def wait_element(self, ele):
        try:
            WebDriverWait(self.driver, 30).until(ele)
        except TimeoutException:
            print("Timed out waiting for page to load")

    def page_has_loaded(self):
        # self.log.info("Checking if {} page is loaded.".format(self.driver.current_url))
        for index in range(100):
            page_state = self.driver.execute_script('return document.readyState;')
            if page_state == 'complete':
                break

    # # 鼠标移动点击机制
    def move_action(self, type, value):
        if type == "xpath":
            ele = self.driver.find_element(By.XPATH, value)
            ActionChains(self.driver).move_to_element(ele).click(ele).perform()
        elif type == "id":
            ele = self.driver.find_element(By.ID, value)
            ActionChains(self.driver).move_to_element(ele).click(ele).perform()
        elif type == "name":
            ele = self.driver.find_element(By.NAME, value)
            ActionChains(self.driver).move_to_element(ele).click(ele).perform()
        elif type == "link_text":
            ele = self.driver.find_element(By.LINK_TEXT, value)
            ActionChains(self.driver).move_to_element(ele).click(ele).perform()

    # 校验按钮是否为选中状态
    def is_selected(self, type, value):
        if type == "xpath":
            self.driver.find_element(By.XPATH, value).is_selected()
        elif type == "id":
            self.driver.find_element(By.ID, value).is_selected()
        elif type == "name":
            self.driver.find_element(By.NAME, value).is_selected()
        elif type == "link_text":
            self.driver.find_element(By.LINK_TEXT, value).is_selected()
        elif type == "css_selector":
            self.driver.find_element(By.CSS_SELECTOR, value).is_selected()
        elif type == "partial_link_text":
            self.driver.find_element(By.PARTIAL_LINK_TEXT, value).is_selected()

    # ############################## common method ##############################

    @staticmethod
    def get_project_path():
        """得到项目路径"""
        project_path = os.path.join(
            os.path.dirname(__file__),
            "..",
        )
        return project_path

    def login(self, username, password, user_xpath, pw_xpath, login_xpath):
        actions = ActionChains(self.driver)
        actions.move_to_element(self.driver.find_element(By.ID, user_xpath)). \
            click_and_hold().perform()
        self.driver.find_element(By.ID, user_xpath).send_keys(username)
        actions.move_to_element(self.driver.find_element(By.ID, pw_xpath)).click_and_hold().perform()
        self.driver.find_element(By.ID, pw_xpath). \
            send_keys(password)
        self.driver.implicitly_wait(500)
        self.driver.find_element(By.XPATH, login_xpath).click()
        self.driver.implicitly_wait(3000)

    @staticmethod
    def test_convert_data(test_data):
        result_list = []
        for data in test_data:
            result_list.append(tuple(data.values()))
        print(result_list)
        return result_list

    @staticmethod
    def get_data_path():
        file_path = os.path.abspath(__file__)
        parent_path = os.path.dirname(file_path)
        parent2_path = os.path.dirname(parent_path)
        data_path = parent2_path + "\\data\\excel_data\\test_data_erp.xlsx"
        return data_path

    @staticmethod
    def get_ui_test_path():
        file_path = os.path.abspath(__file__)
        parent_path = os.path.dirname(file_path)
        parent2_path = os.path.dirname(parent_path)
        return parent2_path

    @staticmethod
    def get_firefox_driver():
        file_path = os.path.abspath(__file__)
        parent_path = os.path.dirname(file_path)
        parent2_path = os.path.dirname(parent_path)
        browser_driver_path = parent2_path + "\\resource\\driver"
        return webdriver.Firefox(browser_driver_path)

    @staticmethod
    def get_chrome_driver():
        file_path = os.path.abspath(__file__)
        parent_path = os.path.dirname(file_path)
        parent2_path = os.path.dirname(parent_path)
        browser_driver_path = parent2_path + "\\resource\\driver\\chromedriver.exe"
        return webdriver.Chrome(browser_driver_path)

    @staticmethod
    def random_number():
        randon_number = random.randint(1, 10000)
        print(randon_number)
        return randon_number

    # 删除小数点后多余的0
    def delete_extra_zero(n):
        if isinstance(n, int):
            return n
        if isinstance(n, float):
            n = str(n).rstrip('0')  # 删除小数点后多余的0
            n = int(n.rstrip('.')) if n.endswith('.') else float(n)  # 只剩小数点直接转int，否则转回float
            return n

    @staticmethod
    def convert_to_decimal(number):
        number = Decimal(number).quantize(Decimal("0.00"))
        return number

    def active_dropdown(self, ele):
        action = ActionChains(self.driver)
        action.move_to_element(ele).click(ele).perform()

    def click_and_hold(self, ele):
        action = ActionChains(self.driver)
        action.move_to_element(ele).click_and_hold().perform()

    def highlight(self, element):
        """Highlights a Selenium webdriver element"""
        self.driver = element._parent
        def apply_style(s):
            self.driver.execute_script("arguments[0].setAttribute('style', arguments[1])", element, s)

        orignal_style = element.get_attribute('style')
        apply_style("border:6px solid red; background:yellow")
        # apply_style("border: 4px solid red")
        if (element.get_attribute("style") != None):
            time.sleep(1)
        apply_style(orignal_style)
