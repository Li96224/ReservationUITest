from Common.basepage import BasePage
from appium.webdriver.common.mobileby import MobileBy


class HomePage(BasePage):
    # 团课
    group_class = '//*[@class="NavbarPageList--selected-item NavbarPageList--selected-item-active"]'

    # 私教
    Personal_Trainers = '//*[@class="NavbarPageList--selected-item NavbarPageList--selected-item-red"][1]'

    # camp
    camp = '//*[@id="stickyCourseNav"]/wx-view[1]/wx-view/wx-course-selected-navbar/wx-view/wx-view[1]/wx-view[3]'

    # 第一个日期
    first_date = '//*[@data-wpy-evt="1413-0" and @class="NavbarWeek--week"][1]'
    # 第二个日期
    second_date = '//*[@class="NavbarWeek--week NavbarWeek--week-active"]'
    # 第三个日期
    third_date = '//*[@data-wpy-evt="1413-0" and @class="NavbarWeek--week"][2]'
    # 第四个日期
    fourth_date = '//*[@data-wpy-evt="1413-0" and @class="NavbarWeek--week"][3]'
    # 第五个日期
    fifth_date = '//*[@data-wpy-evt="1413-0" and @class="NavbarWeek--week"][4]'
    # 第六个日期
    sixth_date = '//*[@data-wpy-evt="1413-0" and @class="NavbarWeek--week"][5]'

    # 课程名称
    class_name = "//*[text()='BODY COMBAT燃脂搏击(初级课)2222']"

    # 课程预约按钮
    appointment = '//*[@id="class"]/wx-class-list/wx-sticky-wrapper/wx-swiper/div/div[1]/div/wx-swiper-item[2]/wx-class-day/wx-class-box[2]/wx-view/wx-view/wx-class-entry[1]/wx-view/wx-view[2]'

    # 城市
    city = '//*[@class="SelectCity--select-city" ]'

    # 收藏门店
    collection_store = "//*[contains(text(),'test_教室名称全能店')][1]"

    # 收藏门店的首节排课 课程名称
    collection_store_curriculum_name = "//*[text()='BODY COMBAT燃脂搏击(初级课)2222']"

    # 藏门店的首节排课 课程标签
    collection_store_curriculum_label = "//*[text()='燃脂 • 搏击 • LesMills']"

    def get_group_class_text(self):
        """ 获取团课文本"""
        return self.get_text(loc=(MobileBy.XPATH, self.group_class), img_name='课表页')

    def get_Personal_Trainers_text(self):
        """获取私教文本"""
        return self.get_text(loc=(MobileBy.XPATH, self.Personal_Trainers), img_name='课表页')

    def get_collection_store_text(self):
        """获取收藏门店文本"""
        return self.get_text(loc=(MobileBy.XPATH, self.collection_store), img_name='课表页')

    def get_camp_text(self):
        """获取camp文本"""
        return self.get_text(loc=(MobileBy.XPATH, self.camp), img_name='课表页')

    def get_collection_store_curriculum_name_text(self):
        """获取团课名称"""
        return self.get_text(loc=(MobileBy.XPATH, self.collection_store_curriculum_name), img_name='课表页')

    def get_collection_store_curriculum_label_text(self):
        """获取团课标签"""
        return self.get_text(loc=(MobileBy.XPATH, self.collection_store_curriculum_label), img_name='课表页')

    def click_first_date(self):
        """点击第一个日期"""
        self.get_click(loc=(MobileBy.XPATH, self.first_date), img_name='课表页')

    def click_second_date(self):
        """点击第二个日期"""
        self.get_click(loc=(MobileBy.XPATH, self.second_date), img_name='课表页')

    def click_third_date(self):
        """点击第三个日期"""
        self.get_click(loc=(MobileBy.XPATH, self.third_date), img_name='课表页')

    def click_fourth_date(self):
        """点击第四个日期"""
        self.get_click(loc=(MobileBy.XPATH, self.fourth_date), img_name='课表页')

    def click_fifth_date(self):
        """点击第五个日期"""
        self.get_click(loc=(MobileBy.XPATH, self.first_date), img_name='课表页')

    def click_sixth_date(self):
        """点击第五个日期"""
        self.get_click(loc=(MobileBy.XPATH, self.sixth_date), img_name='课表页')

    def click_class_name(self):
        """点击课程名称"""
        self.get_click(loc=(MobileBy.XPATH, self.class_name), img_name='课表页')

    def click_appointment(self):
        """点击预约"""
        self.get_click(loc=(MobileBy.XPATH, self.appointment), img_name='课表页')

    def get_city_text(self):
        """获取城市文本"""
        return self.get_text(loc=(MobileBy.XPATH, self.city), img_name='课表页')
