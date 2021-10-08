


from Common.basepage import BasePage
from appium.webdriver.common.mobileby import MobileBy

class GroupClassDetailsPage(BasePage):


    #团课名称
    league_class_name= "//*[text()='BODY COMBAT燃脂搏击(初级课)2222']"

    # 教练名称
    coach_name= "//*[text()='黎又铭']"

    #教练简介
    coach_introduction='//*[contains(text(),"1222")]'

    #课程简介
    course_introduction='//*[contains(text(),"BODYCOMBAT有氧搏击，将中国武术、泰拳、西洋拳击、空手道、跆拳道等结合在一起，高效燃脂的同时提升体能和灵活性。动作节奏性非常强，让你的训练课就像一场运动party。")]'

    #课程标签
    course_label_1="//*[text()='燃脂']"

    course_label_2="//*[text()='搏击']"

    course_label_3="//*[text()='LesMills']"

    #训练效果
    training_effect='//*[contains(text(),"BODYCOMBAT是快节奏、中高强度、多重复次数的搏击主题有氧运动项目。持续1小时左右的有氧训练，不仅可以高效燃脂，还能促进新陈代谢，改善心肺功能。同时它的动作快速有力，反复训练能帮助提高动作的敏捷性。现代都市白领生活压力较大，搏击主题的有氧运动可以让你尽情释放压力。")]'

    #适合人群
    crowd_suits='//*[contains(text(),"BODYCOMBAT将搏击和有氧训练结合，动作和音乐经过顶级教练员、运动生理专家、编辑师精心研究，不仅安全有效，还易于掌握。无论是平时缺乏锻炼、身材娇小、体质瘦弱的白领女性，还是身体强壮的男性，都非常适合参与，从而达到燃脂瘦身，放松减压的目的。但是孕妇、高血压、动脉粥样硬化、心脏病患者均不宜参加，以免发生意外。")]'

    #FAQ
    F="//*[text()='Q: 女生适合BODYCOMBAT吗？']"
    AQ="//*[text()='A: 非常适合。BODYCOMBAT主要功效是减脂，而不是锻炼肌肉。看上去这么有男子气概的方式，同样非常适用于女性。如果能够长期坚持，再适当地配合器械组合，就会使身体的构成有所改变，肌肉会逐渐取代松松的赘肉，身体的线条会更加清晰。值得一提的是，女生打起拳来也很帅哦！']"

    #注意事项
    note='//*[contains(text(),"运动装备")]'

    #赠课好友
    free_class='//*[contains(text(),"赠课给好友")]'

    #约课
    appointment='//*[contains(text(),"立即约课")]'

    def get_league_class_name_text(self):
        """获取团课名称文本"""
        return self.get_text(loc=(MobileBy.XPATH,self.league_class_name),img_name="团课详情页")

    def get_coach_name_text(self):
        """获取教练名称文本"""
        return self.get_text(loc=(MobileBy.XPATH,self.coach_name),img_name="团课详情页")

    def get_coach_introduction_text(self):
        """获取教练简介文本"""
        return self.get_text(loc=(MobileBy.XPATH,self.coach_introduction),img_name="团课详情页")

    def get_course_introduction_text(self):
        """获取课程简介文本"""
        return self.get_text(loc=(MobileBy.XPATH, self.course_introduction), img_name="团课详情页")

    def get_course_label_1_text(self):
        """获取课程标签1文本"""
        return self.get_text(loc=(MobileBy.XPATH, self.course_label_1), img_name="团课详情页")

    def get_course_label_2_text(self):
        """获取课程标签2文本"""
        return self.get_text(loc=(MobileBy.XPATH, self.course_label_2), img_name="团课详情页")

    def get_course_label_3_text(self):
        """获取课程标签3文本"""
        return self.get_text(loc=(MobileBy.XPATH, self.course_label_3), img_name="团课详情页")

    def get_training_effect_text(self):
        """获取训练效果文本"""
        return self.get_text(loc=(MobileBy.XPATH, self.training_effect), img_name="团课详情页")

    def get_crowd_suits_text(self):
        """获取适合人群文本"""
        return self.get_text(loc=(MobileBy.XPATH, self.crowd_suits), img_name="团课详情页")

    def get_F_text(self):
        """获取F文本"""
        return self.get_text(loc=(MobileBy.XPATH, self.F), img_name="团课详情页")

    def get_AQ_text(self):
        """获取AQ文本"""
        return self.get_text(loc=(MobileBy.XPATH, self.AQ), img_name="团课详情页")



    def get_note_text(self):
        """获取注意事项文本"""
        return self.get_text(loc=(MobileBy.XPATH, self.note), img_name="团课详情页")

    def get_free_class_text(self):
        """获取赠课文本"""
        return self.get_text(loc=(MobileBy.XPATH, self.free_class), img_name="团课详情页")

    def get_appointment_text(self):
        """获取立即约课文本"""
        return self.get_text(loc=(MobileBy.XPATH, self.appointment), img_name="团课详情页")


    def click_free_class_text(self):
        """点击赠课"""
        self.get_click(loc=(MobileBy.XPATH, self.free_class), img_name="团课详情页")

    def click_appointment_text(self):
        """点击约课"""
        self.get_click(loc=(MobileBy.XPATH, self.appointment), img_name="团课详情页")


