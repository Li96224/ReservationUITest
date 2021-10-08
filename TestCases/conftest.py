


import pytest
from Common.wx_init import DriverClient


@pytest.fixture()
def get_home_page():
    """
    打开app 确认已登录 切入课表页
    :return:实例driver
    """
    driver=DriverClient().get_driver()
    yield driver
    driver.quit()



if __name__ == '__main__':
    pass