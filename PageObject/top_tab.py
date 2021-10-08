from Common.basepage import BasePage
from appium.webdriver.common.mobileby import MobileBy

class TopTab(BasePage):

    #返回键
    return_key='//*[@class="NavigatorBar--nav-back"]'

    #主页键
    home_key='//*[@class="NavigatorBar--nav-home"]'


    def click_return_key(self):
        """点击返回键"""
        self.driver.switch_to.context("NATIVE_APP")

        self.get_click(loc=(MobileBy.XPATH,self.return_key),img_name="顶部按钮")


    def click_home_key(self):
        """点击home键"""
        self.get_click(loc=(MobileBy.XPATH,self.home_key),img_name="顶部按钮")
        self.switch_to_NATIVE_APP()  # 需先切换原生
        self.switch_to_WEBVIEW_com()  # 后切换回webview

