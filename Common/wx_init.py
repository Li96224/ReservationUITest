import time

from Common.dir_path import config_yaml_path, chrome_driver_path
from Common.yaml_handler import YamlHandler
from appium import webdriver


# class Singleton(object):
#     driver = None
#
#     def __new__(cls, *args, **kw):
#         if not hasattr(cls, '_instance'):
#             orig = super(Singleton, cls)
#             desired_caps = YamlHandler(config_yaml_path).get_yaml_data()
#             desired_caps['chromedriverExecutable'] = chrome_driver_path
#             cls._instance = orig.__new__(cls, *args, **kw)
#             cls._instance.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
#         return cls._instance
#
#
# class DriverClient(Singleton):
#
#     def getDriver(self):
#         self.driver.implicitly_wait(20)
#         self.driver.find_element_by_android_uiautomator('new UiSelector().text("发现")').click()
#
#         self.driver.find_element_by_android_uiautomator('new UiSelector().text("小程序")').click()
#
#         self.driver.find_element_by_android_uiautomator('new UiSelector().text("超级猩猩")').click()
#
#         self.driver.switch_to.context('WEBVIEW_com.tencent.mm:appbrand0')
#
#         return self.driver
#
#


class DriverClient():

    def get_driver(self):
        desired_caps = YamlHandler(config_yaml_path).get_yaml_data()

        desired_caps['chromedriverExecutable'] = chrome_driver_path

        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

        self.driver.implicitly_wait(20)

        self.driver.find_element_by_android_uiautomator('new UiSelector().text("发现")').click()

        self.driver.find_element_by_android_uiautomator('new UiSelector().text("小程序")').click()

        self.driver.find_element_by_android_uiautomator('new UiSelector().text("超级猩猩")').click()
        time.sleep(1.5)
        self.driver.switch_to.context('WEBVIEW_com.tencent.mm:appbrand0')

        return self.driver




if __name__ == '__main__':
    desired_caps = YamlHandler(config_yaml_path).get_yaml_data()
    print(desired_caps)
