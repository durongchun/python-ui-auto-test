#!/usr/bin/env python
# -*- coding: utf-8 -*-


from time import sleep

import self as self
from appium import webdriver


# mobile tool
class MobileTool:
    # 初始化 mysql 连接
    def __init__(self):
        self.desired_caps = None

    def connect_mobile_browser(self):
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
            'noReset': True,
            # 设置session的超时时间，单位秒
            'newCommandTimeout': 6000,
            # 如果不想每次都安装UI2驱动，可以这么设置
            # 指定自动化驱动
            # 'automationName':'UiAutomator2',
            # 'skipServerInstallation':True
            # 使用指定的浏览器驱动-匹配手机上的谷歌浏览器
            'chromedriverExecutableDir': r'C:\Users\user\Desktop\py\sq_appium\d5\chromedriver 81'
        }
        driver = webdriver.Remote('http://localhost:4723/wd/hub', self.desired_caps)

        driver.implicitly_wait(10)