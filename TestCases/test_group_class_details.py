


import pytest

from Common.request_handler import create_schedule
from PageObject.recommended_schedule_page import RecommendedSchedulePage
from PageObject.top_tab import TopTab
from PageObject.home_page import HomePage
from PageObject.group_class_details_page import GroupClassDetailsPage
import allure
@allure.title("课程详情页-课程信息")
@pytest.mark.usefixtures('get_home_page')
class TestGroupClassDetails():
    def test_group_class_details(self,get_home_page):
        create_schedule(class_id=5020, coach_id=[3216262], box_id=2375, tenant_id=26257, isTrue=True,
                        now=True)
        TopTab(get_home_page).click_home_key()

        HomePage(get_home_page).click_class_name()
        HomePage(get_home_page).switch_to_NATIVE_APP()
        HomePage(get_home_page).switch_to_WEBVIEW_com()
        assert(GroupClassDetailsPage(get_home_page).get_league_class_name_text()=='BODY COMBAT燃脂搏击(初级课)2222' )
        assert(GroupClassDetailsPage(get_home_page).get_coach_name_text()=='黎又铭' )
        RecommendedSchedulePage(get_home_page).swipe_by_dorection('up')

        # assert(GroupClassDetailsPage(get_home_page).get_coach_introduction_text() is True )
        # assert(GroupClassDetailsPage(get_home_page).get_course_introduction_text()=='BODYCOMBAT有氧搏击，将中国武术、泰拳、西洋拳击、空手道、跆拳道等结合在一起，高效燃脂的同时提升体能和灵活性。动作节奏性非常强，让你的训练课就像一场运动party。' )
        assert(GroupClassDetailsPage(get_home_page).get_course_label_1_text()=='燃脂' )
        assert(GroupClassDetailsPage(get_home_page).get_course_label_2_text()=='搏击' )
        assert(GroupClassDetailsPage(get_home_page).get_course_label_3_text()=='LesMills' )
        assert(GroupClassDetailsPage(get_home_page).get_training_effect_text()=='BODYCOMBAT是快节奏、中高强度、多重复次数的搏击主题有氧运动项目。持续1小时左右的有氧训练，不仅可以高效燃脂，还能促进新陈代谢，改善心肺功能。同时它的动作快速有力，反复训练能帮助提高动作的敏捷性。现代都市白领生活压力较大，搏击主题的有氧运动可以让你尽情释放压力。' )
        RecommendedSchedulePage(get_home_page).swipe_by_dorection('up')

        assert(GroupClassDetailsPage(get_home_page).get_crowd_suits_text()=='BODYCOMBAT将搏击和有氧训练结合，动作和音乐经过顶级教练员、运动生理专家、编辑师精心研究，不仅安全有效，还易于掌握。无论是平时缺乏锻炼、身材娇小、体质瘦弱的白领女性，还是身体强壮的男性，都非常适合参与，从而达到燃脂瘦身，放松减压的目的。但是孕妇、高血压、动脉粥样硬化、心脏病患者均不宜参加，以免发生意外。' )
        assert(GroupClassDetailsPage(get_home_page).get_F_text()=='Q: 女生适合BODYCOMBAT吗？' )
        assert(GroupClassDetailsPage(get_home_page).get_AQ_text()=='A: 非常适合。BODYCOMBAT主要功效是减脂，而不是锻炼肌肉。看上去这么有男子气概的方式，同样非常适用于女性。如果能够长期坚持，再适当地配合器械组合，就会使身体的构成有所改变，肌肉会逐渐取代松松的赘肉，身体的线条会更加清晰。值得一提的是，女生打起拳来也很帅哦！' )
        # assert(GroupClassDetailsPage(get_home_page).get_note_text() is True )
        assert(GroupClassDetailsPage(get_home_page).get_appointment_text()=="赠课给好友" )

