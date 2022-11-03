import unittest
from time import sleep

from appium import webdriver
from selenium import webdriver


class MyTestCase(unittest.TestCase):

    def setUp(self):
        capabilities = {
            "platformName": "Android",
            # Mobile OS类型
            "platformVersion": "11",
            # Mobile OS版本
            "deviceName": "Redmi Note 9",
            # Mobile OS版本
            "udid": "599pgukbu8s8pzau",
            # adb devices
            "browserName": "Chrome",
            # Chrome浏览器
            "appPackage": "com.android.browser",
            # Chrome的包名
            "appActivity": ".BrowserActivity",
            # Chrome的启动页
            "unicodeKeyboard": True,
            # 支持中文输入，默认false
            "resetKeyboard": True,
            # 重置输入法为系统默认
            "noReset": True,
            # 不重新安装apk
            "noSign": True,

            'chromedriverExecutableDir': r'C:\Users\LucyDu\Desktop\driver'
        }
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", capabilities)
        sleep(1)

    def test_chromeApp(self):
        url = "https://m.taobao.com"
        # 手机淘宝H5
        driver = self.driver
        driver.get(url)
        sleep(1)
        driver.find_element_by_id("search-placeholder").click()
        # 点击淘宝搜索框
        sleep(1)
        driver.find_element_by_name("q").send_keys("华硕官方旗舰店")
        sleep(1)
        driver.find_element_by_class_name("icons-search").click()
        sleep(3)
        assert driver.page_source.__contains__("asus华硕官方旗舰店")

    def tearDown(self):
        self.driver.close_app()
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
