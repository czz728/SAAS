import time
import allure
import pytest
from pages.appointment import AppointmentPage
from pages.home import HomePage

@pytest.mark.skip
@allure.feature("预约页面")
class TestAppointment():

    @pytest.mark.skip
    @allure.story("预约大屏")
    @allure.title("新增预约")
    def test_newAppointment(self,login_web):
        """step1:初始化页面"""
        # 登录网站
        driver = login_web
        # 打开首页
        self.home_page = HomePage(driver)
        # 点击预约
        self.home_page.appointment()
        # 初始化预约页面
        self.appointment_page = AppointmentPage(driver)
        """step2:准备数据"""

        """step3:操作步骤"""

        """step4:断言结果"""

    @pytest.mark.skip
    @allure.story("预约大屏")
    @allure.title("锁定时间")
    def test_lockingTime(self, login_web):
        """step1:初始化页面"""
        # 登录网站
        driver = login_web
        # 打开首页
        self.home_page = HomePage(driver)
        # 点击预约
        self.home_page.appointment()
        # 初始化预约页面
        self.appointment_page = AppointmentPage(driver)
        """step2:准备数据"""
        self.appointment_page.lockTime()
        """step3:操作步骤"""

        """step4:断言结果"""

    @pytest.mark.skip
    @allure.story("预约列表")
    @allure.title("设置潜客参数")
    def test_newAppointment(self, login_web):
        """step1:初始化页面"""
        # 登录网站
        driver = login_web
        # 打开首页
        self.home_page = HomePage(driver)
        # 点击预约
        self.home_page.appointment()
        # 初始化预约页面
        self.appointment_page = AppointmentPage(driver)
        """step2:准备数据"""
        self.appointment_page.lockTime()
        """step3:操作步骤"""

        """step4:断言结果"""
