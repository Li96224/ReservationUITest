import pytest

from Common.request_handler import create_schedule
from PageObject.home_page import HomePage
import allure

from PageObject.top_tab import TopTab


@allure.title("课表页-课程信息")
@pytest.mark.usefixtures('get_home_page')
class TestClassScheduleCard:
    def test_class_schedule_card(self, get_home_page):
        TopTab(get_home_page).click_home_key()

        create_schedule(class_id=5020, coach_id=[3216262], box_id=2375, tenant_id=26257, isTrue=True,
                        now=True)
        assert ('团课' == HomePage(get_home_page).get_group_class_text())
        assert ('深圳' == HomePage(get_home_page).get_city_text())
        assert ('CAMP' == HomePage(get_home_page).get_camp_text())
        assert ('私教' == HomePage(get_home_page).get_Personal_Trainers_text())
        assert ('test_教室名称全能店' == HomePage(get_home_page).get_collection_store_text())
        assert ('BODY COMBAT燃脂搏击(初级课)2222' == HomePage(get_home_page).get_collection_store_curriculum_name_text())
        assert ('燃脂 • 搏击 • LesMills' == HomePage(get_home_page).get_collection_store_curriculum_label_text())
