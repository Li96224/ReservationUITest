from appium import webdriver
import time

from Common.basepage import BasePage
from Common.dir_path import chrome_driver_path
import pickle

from PageObject.bottom_tab import BottomTab

desired_caps = {
    "automationName": "UiAutomator2",
    "platformName": "Android",
    "platformVersion": "10",
    "deviceName": "UYT5T18524015578",
    "appPackage": "com.tencent.mm",
    "appActivity": ".ui.LauncherUI",
    "noReset": True,
    "fullReset": False,
    'newCommandTimeout': 600,
    "chromedriverExecutable": chrome_driver_path,
    "recreateChromeDriverSessions": True,  # 该参数解决了 在切换多个webview的时候只拿到第一个webview 不需要再杀掉前面的进程
    'chromeOptions': {
        'androidProcess': 'com.tencent.mm:appbrand0'
    },
    "browserName": "",
    'skipDeviceInitialization': True,
    'skipUnlock	':  True,
    'sessionOverride':  True
}

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
driver.implicitly_wait(5)
driver.find_element_by_android_uiautomator('new UiSelector().text("发现")').click()

driver.find_element_by_android_uiautomator('new UiSelector().text("小程序")').click()

driver.find_element_by_android_uiautomator('new UiSelector().text("超级猩猩")').click()


driver.switch_to.context('WEBVIEW_com.tencent.mm:appbrand0')



print(driver.page_source)
home_key='//*[@class="NavigatorBar--nav-home"]'
driver.find_element_by_xpath(home_key).click()

# def get_devices_size():
#     size = driver.get_window_size()
#     return size
#
# def touch_tap(x, y, duration=100):
#     """
#
#     :param x:横坐标
#     :param y:纵坐标
#     :param duration:点击时间
#     :return:
#     """
#     screen_width =get_devices_size()['width']
#     screen_height = get_devices_size()['height']
#     a = (float(x) / screen_width) * screen_width
#     x1 = int(a)
#     b = (float(y) / screen_height) * screen_height
#     y1 = int(b)
#     driver.tap([(x1, y1), (x1, y1)], duration)


BottomTab(driver).click_store_tab()
BasePage(driver).switch_to_NATIVE_APP()
BasePage(driver).swipe_by_dorection("up")
BasePage(driver).switch_to_WEBVIEW_com()
print('1111111111111110',driver.page_source)
# driver.close_app()