

import pytest
from PageObject.home_page import HomePage
import allure
import time
from PageObject.top_tab import TopTab


@allure.title("课表页")
@pytest.mark.usefixtures('get_home_page')
class TestClassScheduleCard:
    def test_class_schedule_card(self,get_home_page):
        TopTab(get_home_page).click_home_key()
        assert('团课'==HomePage(get_home_page).get_group_class_text())






