from Common.basepage import BasePage
from appium.webdriver.common.mobileby import MobileBy


class RecommendedSchedulePage(BasePage):
    # 推荐课程名称
    recommended_course_name = '//*[text()="CXWORX腰腹核心"]'

    # 训练效果1
    training_effect_1 = '//*[text()="高效燃脂"]'

    # 训练效果2
    training_effect_2 = '//*[text()="雕刻线条"]'

    # 训练效果3
    training_effect_3 = '//*[text()="拉伸放松"]'

    # 训练效果1-课程1
    selected_courses_Category_1 = '//*[text()="普拉提"]'

    #训练效果2-课程2
    selected_courses_Category_2='//*[text()="RPM 燃脂骑行"]'

    #训练效果3-课程3
    selected_courses_Category_3='//*[text()="Deep Rowing 深燃划船"]'


    def get_recommended_course_name_text(self):
        """获取推荐课程文本"""
        return self.get_text(loc=(MobileBy.XPATH, self.recommended_course_name), img_name='推荐课表页')

    def get_training_effect_1_text(self):
        """获取训练效果1文本"""
        return self.get_text(loc=(MobileBy.XPATH,self.training_effect_1),img_name='推荐课表页')

    def get_training_effect_2_text(self):
        """获取训练效果2文本"""
        return self.get_text(loc=(MobileBy.XPATH, self.training_effect_2), img_name='推荐课表页')

    def get_training_effect_3_text(self):
        """获取训练效果3文本"""
        return self.get_text(loc=(MobileBy.XPATH, self.training_effect_3), img_name='推荐课表页')


    def get_Selected_courses_Category_1_text(self):
        """训练效果1-课程1文本"""
        return self.get_text(loc=(MobileBy.XPATH, self.selected_courses_Category_1), img_name='推荐课表页')

    def get_Selected_courses_Category_2_text(self):
        """训练效果2-课程1文本"""
        return self.get_text(loc=(MobileBy.XPATH, self.selected_courses_Category_2), img_name='推荐课表页')

    def get_Selected_courses_Category_3_text(self):
        """训练效果3-课程1文本"""
        return self.get_text(loc=(MobileBy.XPATH, self.selected_courses_Category_3), img_name='推荐课表页')


