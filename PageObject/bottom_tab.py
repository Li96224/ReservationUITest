from Common.basepage import BasePage
from appium.webdriver.common.mobileby import MobileBy


class BottomTab(BasePage):
    # 门店
    store_tab = (112, 1835)
    # 课表
    timetable_tab = (411, 1844)
    # 预约
    appointment_tab = (695, 1839)
    # 超星卡
    membership_card_tab = (932, 1857)

    def click_store_tab(self):
        """点击门店"""
        self.driver.switch_to.context("NATIVE_APP")

        self.touch_tap(*self.store_tab)

    def click_timetable_tab(self):
        """点击课表"""
        self.touch_tap(*self.timetable_tab)

    def click_appointment_tab(self):
        """点击预约"""
        self.touch_tap(*self.appointment_tab)

    def click_membership_card_tab(self):
        """点击超星卡"""
        self.touch_tap(*self.membership_card_tab)
