import pytest

from PageObject.recommended_schedule_page import RecommendedSchedulePage
import allure


@allure.title("推荐课表页-推荐课程信息")
@pytest.mark.usefixtures('get_home_page')
class TestClassScheduleCard:
    def test_class_schedule_card(self, get_home_page):
        assert ('CXWORX腰腹核心' == RecommendedSchedulePage(get_home_page).get_recommended_course_name_text())
        assert ('高效燃脂' == RecommendedSchedulePage(get_home_page).get_training_effect_1_text())
        RecommendedSchedulePage(get_home_page).swipe_by_dorection('up')
        assert ('普拉提' == RecommendedSchedulePage(get_home_page).get_Selected_courses_Category_1_text())

        assert ('雕刻线条' == RecommendedSchedulePage(get_home_page).get_training_effect_2_text())
        assert ('RPM 燃脂骑行' == RecommendedSchedulePage(get_home_page).get_Selected_courses_Category_2_text())
        RecommendedSchedulePage(get_home_page).swipe_by_dorection('up')

        assert ('拉伸放松' == RecommendedSchedulePage(get_home_page).get_training_effect_3_text())
        assert ('Deep Rowing 深燃划船' == RecommendedSchedulePage(get_home_page).get_Selected_courses_Category_3_text())
