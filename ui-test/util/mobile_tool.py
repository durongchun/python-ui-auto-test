#!/usr/bin/env python
# -*- coding: utf-8 -*-
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

from erp_data import ErpData
import time
from selenium import webdriver


# mobile tool
class MobileTool:
    # 初始化 mysql 连接
    def __init__(self):
        self.desired_caps = None

    def connect_mobile_browser(self):
        url = ErpData.url
        self.desired_caps = {
            # 移动设备平台
            'platformName': 'Android',
            # 平台OS版本号,写整数位即可
            'plathformVersion': '9',
            # 设备的名称--值可以随便写
            'deviceName': 'test0106',
            # 直接指定浏览器名称参数为chrome【重点添加了这一步】
            'browserName': 'Chrome',
            # 确保自动化之后不重置app
            'noReset': True

        }
        driver = webdriver.Remote('http://localhost:4723/wd/hub', self.desired_caps)
        print('浏览器启动成功')
        driver.implicitly_wait(10)
        driver.get(url)

    @staticmethod
    def mobile_emulator():
        mobileEmulation = {'deviceName': 'iPhone 6'}
        options = webdriver.ChromeOptions()
        options.add_experimental_option('mobileEmulation', mobileEmulation)
        driver = webdriver.Chrome(chrome_options=options)
        driver.get('http://www.baidu.com')
        time.sleep(3)
        return driver
