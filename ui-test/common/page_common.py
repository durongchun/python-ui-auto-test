#!/usr/bin/env python
# -*- coding: utf-8 -*-

from telnetlib import EC

from selenium.webdriver import ActionChains
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

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
            self.driver.find_element_by_xpath(value).send_keys(inputvalue)
        elif type == "class_name":
            self.driver.find_element_by_class_name(value).send_keys(inputvalue)
        elif type == "id":
            self.driver.find_element_by_id(value).send_keys(inputvalue)
        elif type == "name":
            self.driver.find_element_by_name(value).send_keys(inputvalue)
        elif type == "link_text":
            self.driver.find_element_by_link_text(value).send_keys(inputvalue)
        elif type == "partial_link_text":
            self.driver.find_element_by_partial_link_text(value).send_keys(inputvalue)

    # 鼠标事件方法一
    def click(self, type, value):
        if type == "xpath":
            self.driver.find_element_by_xpath(value).click()
        elif type == "class_name":
            self.driver.find_element_by_class_name(value).click()
        elif type == "id":
            self.driver.find_element_by_id(value).click()
        elif type == "name":
            self.driver.find_element_by_name(value).click()
        elif type == "link_text":
            self.driver.find_element_by_link_text(value).click()
        elif type == "partial_link_text":
            self.driver.find_element_by_partial_link_text(value).click()

    # 鼠标事件方法二
    def clear(self, type, value):
        if type == "xpath":
            self.driver.find_element_by_xpath(value).clear()
        elif type == "id":
            self.driver.find_element_by_id(value).clear()
        elif type == "name":
            self.driver.find_element_by_name(value).clear()
        elif type == "link_text":
            self.driver.find_element_by_link_text(value).clear()
        elif type == "partial_link_text":
            self.driver.find_element_by_partial_link_text(value).clear()

    # 验证元素是否存在
    def check_element(self, type, value):
        if type == "xpath":
            self.driver.find_element_by_xpath(value)
        elif type == "id":
            self.driver.find_element_by_id(value)
        elif type == "name":
            self.driver.find_element_by_name(value)
        elif type == "link_text":
            self.driver.find_element_by_link_text(value)
        elif type == "partial_link_text":
            self.driver.find_element_by_partial_link_text(value)

    # 获取子元素
    def select_child_elements(self, type, value1, value2):
        if type == "xpath":
            Select(self.driver.find_element_by_xpath(value1)).select_by_visible_text(value2)
        elif type == "id":
            Select(self.driver.find_element_by_id(value1)).select_by_visible_text(value2)
        elif type == "name":
            Select(self.driver.find_element_by_name(value1)).select_by_visible_text(value2)
        elif type == "link_text":
            Select(self.driver.find_element_by_link_text(value1)).select_by_visible_text(value2)
        elif type == "partial_link_text":
            Select(self.driver.find_element_by_partial_link_text(value1)).select_by_visible_text(value2)

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
            text = self.driver.find_element_by_xpath(value).text
            return text
        elif type == "name":
            text = self.driver.find_element_by_name(value).text
            return text
        elif type == "link_text":
            text = self.driver.find_element_by_link_text(value).text
            return text
        elif type == "class_name":
            text = self.driver.find_element_by_class_name(value).text
            return text
        elif type == "id":
            text = self.driver.find_element_by_id(value).text
            return text

    # 显性等待时间
    def webDriverWait(self, MaxTime, MinTime, value):
        element = self.driver.find_element(By.ID, value)
        WebDriverWait(self.driver, MaxTime, MinTime).until(EC.presence_of_element_located(element))

    def page_has_loaded(self):
        # self.log.info("Checking if {} page is loaded.".format(self.driver.current_url))
        for index in range(100):
            page_state = self.driver.execute_script('return document.readyState;')
            if page_state == 'complete':
                break

    # # 鼠标移动点击机制
    def move_action(self, type, value):
        if type == "xpath":
            xm = self.driver.find_element_by_xpath(value)
            webdriver.ActionChains(self.driver).click(xm).perform()
        elif type == "id":
            xm = self.driver.find_element_by_id(value)
            webdriver.ActionChains(self.driver).click(xm).perform()
        elif type == "name":
            xm = self.driver.find_element_by_name(value)
            webdriver.ActionChains(self.driver).click(xm).perform()
        elif type == "link_text":
            xm = self.driver.find_element_by_link_text(value)
            webdriver.ActionChains(self.driver).click(xm).perform()

    # 校验按钮是否为选中状态
    def is_selected(self, type, value):
        if type == "id":
            self.driver.find_element_by_id(value).is_selected()
        elif type == "xpath":
            self.driver.find_element_by_xpath(value).is_selected()
        elif type == "class_name":
            self.driver.find_element_by_class_name(value).is_selected()
        elif type == "name":
            self.driver.find_element_by_name(value).is_selected()
        elif type == "link_text":
            self.driver.find_element_by_link_text(value).is_selected()

    ############################## common method ##############################
