import time

from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait
from Common.logger import LogHandler
from Common.dir_path import log_path, screenshot_path
import os
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver import Remote


class BasePage():
    """
    包含pageobjects里面常用的到selenium底层方法
    实现日志记录/失败截图
    """

    def __init__(self, driver: Remote):
        self.driver = driver

    # 封装截图功能
    def screenshot(self, img_name):
        """
        :param img_name: 页面名称_页面行为
        :return:
        """
        # 获取当前时间
        current_time = time.strftime('%Y-%m-%d_%H-%M-%S')

        # 将截图路径与页面名称与当前时间拼接在一起
        file_path = os.path.join(screenshot_path, f'{img_name}_{current_time}.png')
        self.driver.save_screenshot(filename=file_path)
        LogHandler(file=log_path).info(f"当前截图为{file_path}")

    # 封装隐性等待 等待元素可见
    def wait_ele_visible(self, loc, img_name, timeout=20, poll_fre=0.5):
        LogHandler(file=log_path).info(f'在{img_name}页面等待{loc}元素')
        try:
            WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll_fre).until(
                EC.visibility_of_element_located(loc))
        except:
            self.screenshot(img_name=img_name)
            LogHandler(file=log_path).exception(f'在{img_name}页面等待{loc}元素可见失败')
            raise

    # 封装隐性等待 等待元素点击
    def wait_ele_clickable(self, loc, img_name, timeout=20, poll_fre=0.5):
        LogHandler(file=log_path).info(f'在{img_name}页面等待{loc}元素')
        try:
            WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll_fre).until \
                (EC.element_to_be_clickable(loc))
        except:
            self.screenshot(img_name=img_name)
            LogHandler(file=log_path).exception(f'在{img_name}页面等待{loc}元素失败')
            raise

    # 查找单个元素
    def get_ele(self, loc, img_name, ):
        LogHandler(file=log_path).info(f'在{img_name}页面查找{loc}元素')
        try:
            ele = self.driver.find_element(*loc)
        except:
            self.screenshot(img_name=img_name)
            LogHandler(file=log_path).exception(f'在{img_name}页面查找{loc}元素失败')
            raise
        else:
            return ele

    # 查找多个元素
    def get_eles(self, loc, img_name):
        LogHandler(file=log_path).info(f'在{img_name}页面查找{loc}元素')
        try:
            eles = self.driver.find_elements(*loc)
        except:
            self.screenshot(img_name=img_name)
            LogHandler(file=log_path).exception(f'在{img_name}页面查找到个{loc}元素失败')
            raise
        else:
            return eles

    # 点击
    def get_click(self, loc, img_name, timeout=20, poll_fre=0.5):
        LogHandler(file=log_path).info(f'在{img_name}页面点击{loc}元素')
        self.wait_ele_visible(loc=loc, img_name=img_name, timeout=timeout, poll_fre=poll_fre)
        ele = self.get_ele(loc=loc, img_name=img_name)
        try:
            ele.click()
        except:
            self.screenshot(img_name=img_name)
            LogHandler(file=log_path).exception(f'在{img_name}页面查点击失败')
            raise

    # 输入
    def get_send_keys(self, loc, img_name, timeout=20, poll_fre=0.5, value=None):
        LogHandler(file=log_path).info(f'在{img_name}页面{loc}元素输入{value}文本值')
        self.wait_ele_visible(loc=loc, img_name=img_name, timeout=timeout, poll_fre=poll_fre)
        ele = self.get_ele(loc=loc, img_name=img_name)
        try:
            ele.send_keys(value)
        except:
            self.screenshot(img_name=img_name)
            LogHandler(file=log_path).exception(f'在{img_name}页面{loc}元素输入{value}失败')
            raise

    # 获单个取文本值
    def get_text(self, loc, img_name, timeout=20, poll_fre=0.5, ):
        LogHandler(file=log_path).info(f'在{img_name}页面获取{loc}元素文本值')
        self.wait_ele_visible(loc=loc, img_name=img_name, timeout=timeout, poll_fre=poll_fre)
        ele = self.get_ele(loc=loc, img_name=img_name)
        try:
            text = ele.text
        except:
            self.screenshot(img_name=img_name)
            LogHandler(file=log_path).exception(f'在{img_name}页面获取{loc}元素文本值失败')
            raise
        else:
            return text

    # 获多个取文本值
    def get_multiple_text(self, loc, img_name, timeout=20, poll_fre=0.5, ):
        LogHandler(file=log_path).info(f'在{img_name}页面获取{loc}元素文本值')
        self.wait_ele_visible(loc=loc, img_name=img_name, timeout=timeout, poll_fre=poll_fre)
        eles = self.get_eles(loc=loc, img_name=img_name)
        try:
            if len(eles) == 1:
                return eles[0].text
            elif len(eles) > 1:
                list_text = []
                for ele in eles:
                    list_text.append(ele.text)
                return list_text
        except:
            self.screenshot(img_name=img_name)
            LogHandler(file=log_path).exception(f'在{img_name}页面获取{loc}元素文本值失败')
            raise
        # else:
        #     return text

    # 获取属性
    def get_attribute(self, loc, img_name, timeout=20, poll_fre=0.5, attr_name=None):
        LogHandler(file=log_path).info(f'在{img_name}页面获取{loc}属性')
        self.wait_ele_visible(loc=loc, img_name=img_name, timeout=timeout, poll_fre=poll_fre)
        ele = self.get_ele(loc=loc, img_name=img_name)
        try:
            value = ele.get_attribute(attr_name)
        except:
            self.screenshot(img_name=img_name)
            LogHandler(file=log_path).exception(f'在{img_name}页面获取{loc}的属性失败')
            raise
        else:
            return value

    # 切换到新的窗口
    # iframe切图 --触发进入iframe 找到iframe switch_to.ifranme
    def switch_to_iframe(self, loc, img_name):
        # 等待 切换
        try:
            WebDriverWait(self.driver, 20).until(EC.frame_to_be_available_and_switch_to_it(loc))
        except:
            LogHandler(log_path).exception(f'在{img_name}页面切入ifranme表单失败')
            self.screenshot(f'在{img_name}页面切换表单失败')
            raise

    # 获取设备大小
    def get_devices_size(self):
        size = self.driver.get_window_size()
        return size

    # 滑屏操作-上下左右
    def swipe_by_dorection(self, direction:str):
        """
        通过方向整屏滑动
        :param direction: up down left right 向哪个方向滑动
        :return:
        """
        width = self.get_devices_size()['width']
        height = self.get_devices_size()['height']
        if direction.lower() == 'up':
            x1 = width * 0.5
            y1 = height * 0.9
            y2 = height * 0.25
            self.driver.swipe(x1, y1, x1, y2)
        elif direction.lower()  == 'down':
            x1 = width * 0.5
            y1 = height * 0.25
            y2 = height * 0.9
            self.driver.swipe(x1, y1, x1, y2,duration=5000)
        elif direction.lower() == 'left':
            x1 = width * 0.8
            x2 = width * 0.2
            y1 = height * 0.5
            self.driver.swipe(x1, y1, x2, y1)
        elif direction.lower() == 'right':
            x1 = width * 0.2
            x2 = height * 0.8
            y1 = height * 0.5
            self.driver.swipe(x1, y1, x2, y1)

    def switch_to_NATIVE_APP(self):
        """切换回原生"""
        self.driver.switch_to.context("NATIVE_APP")

    def switch_to_WEBVIEW_com(self):
        """切换回webview"""
        self.driver.switch_to.context('WEBVIEW_com.tencent.mm:appbrand0')

    # 通过坐标点击
    def touch_tap(self, x, y, duration=100):
        """

        :param x:横坐标
        :param y:纵坐标
        :param duration:点击时间
        :return:
        """
        screen_width = self.get_devices_size()['width']
        screen_height = self.get_devices_size()['height']
        a = (float(x) / screen_width) * screen_width
        x1 = int(a)
        b = (float(y) / screen_height) * screen_height
        y1 = int(b)
        self.switch_to_NATIVE_APP()  # 需先切换原生 才可做点击
        self.driver.tap([(x1, y1), (x1, y1)], duration)
        self.switch_to_WEBVIEW_com()  # 点击完成后切换回webview

    def get_toast_msg(self, text, img_name):
        loc = (MobileBy.XPATH, f'//*[contains(@text(),"{text}")]')
        LogHandler(file=log_path).info(f'获取toast提示信息，toast元素为{loc}')
        return self.get_text(loc, img_name, 10, 0.01)

    # 列表滑动-找文本/找元素/向上/向下
    # toast获取
    # 混合应用 获取所有 然后切换一下
    # 进入小程序页面
