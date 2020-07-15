import allure
import pytest

from pages.home import HomePage
from pages.overview import OverviewPage
from resource.data.test_data import overview_data

@pytest.mark.skip
@allure.feature("概览页面")
class TestOverview():

    # @pytest.mark.skip
    @allure.story("快捷入口")
    @allure.title("快速开单")
    def test_quickOrder(self,login_web):
        """step1:初始化页面"""
        # 登录网站
        driver = login_web
        # 打开首页
        self.home_page = HomePage(driver)
        # 点击概览
        self.home_page.overview()
        # 初始化概览页面
        self.overview_page = OverviewPage(driver)
        """step2:准备数据"""
        """step3:操作步骤"""
        # 点击快速开单，打开开单页面
        self.overview_page.quickOrder()
        # 获取开单页面的标题
        actual = self.overview_page.get_quickOrder_msg()
        """step4:断言结果"""
        # 断言实际结果与预期结果
        # assert actual.text == test_data["quickOrder"]

    # @pytest.mark.skip
    @allure.story("快捷入口")
    @allure.title("新增预约")
    def test_newBooking(self,login_web):
        """step1:初始化页面"""
        # 登录网站
        driver = login_web
        # 打开首页
        self.home_page = HomePage(driver)
        # 点击概览
        self.home_page.overview()
        # 初始化概览页面
        self.overview_page = OverviewPage(driver)
        """step2:准备数据"""
        """step3:操作步骤"""
        # 点击新增预约，弹出新增预约弹窗
        self.overview_page.newBooking()
        # 获取新增预约弹窗的标题
        actual = self.overview_page.get_newBooking_msg()
        """step4:断言结果"""
        # 断言实际结果与预期结果
        # assert actual.text == test_data["newBooking"]
        # 点击取消，关闭弹窗
        self.overview_page.newBooking_cancel_click()

    # @pytest.mark.skip
    @allure.story("快捷入口")
    @allure.title("新增会员")
    def test_newMembers(self,login_web):
        """step1:初始化页面"""
        # 登录网站
        driver = login_web
        # 打开首页
        self.home_page = HomePage(driver)
        # 点击概览
        self.home_page.overview()
        # 初始化概览页面
        self.overview_page = OverviewPage(driver)
        """step2:准备数据"""
        """step3:操作步骤"""
        # 点击新增会员，打开新增会员页面
        self.overview_page.newMembers()
        # 获取新增会员页面的标题
        actual = self.overview_page.get_newMembers_msg()
        """step4:断言结果"""
        # 断言实际结果与预期结果
        # assert actual.text == test_data["newMembers"]

    # @pytest.mark.skip
    @allure.story("快捷入口")
    @allure.title("新增潜客")
    def test_newPotentialCustomer(self,login_web):
        """step1:初始化页面"""
        # 登录网站
        driver = login_web
        # 打开首页
        self.home_page = HomePage(driver)
        # 点击概览
        self.home_page.overview()
        # 初始化概览页面
        self.overview_page = OverviewPage(driver)
        """step2:准备数据"""
        """step3:操作步骤"""
        # 点击新增潜客，弹出新增潜客弹窗
        self.overview_page.newPotentialCustomer()
        # 获取新增潜客弹窗的标题
        actual = self.overview_page.get_newPotentialCustomer_msg()
        """step4:断言结果"""
        # 断言实际结果与预期结果
        # assert actual.text == test_data["newPotentialCustomer"]
        # 点击取消，关闭弹窗
        self.overview_page.newPotentialCustomer_cancel_click()

    # @pytest.mark.skip
    @allure.story("待办事项")
    @allure.title("预约单-待付款")
    def test_listPaying(self,login_web):
        """step1:初始化页面"""
        # 登录网站
        driver = login_web
        # 打开首页
        self.home_page = HomePage(driver)
        # 点击概览
        self.home_page.overview()
        # 初始化概览页面
        self.overview_page = OverviewPage(driver)
        """step2:准备数据"""

        # 获取预约单-待付款任务数

        """step3:操作步骤"""
        with allure.step("kk"):
            pass
        # 1、点击预约单-待付款，打开预约列表页面
        self.overview_page.listPaying()
        # 2、获取预约列表页面-待付款的预约数
        actual = self.overview_page.get_listPaying_msg()
        """step4:断言结果"""
        # assert actual.text == test_data["listPaying"]

    # @pytest.mark.skip
    @allure.story("待办事项")
    @allure.title("预约单-待服务")
    @pytest.mark.parametrize("test_data",overview_data)
    def test_listServer(self,login_web,test_data):
        """step1:初始化页面"""
        # 登录网站
        driver = login_web
        # 打开首页
        self.home_page = HomePage(driver)
        # 点击概览
        self.home_page.overview()
        # 初始化概览页面
        self.overview_page = OverviewPage(driver)
        """step2:准备数据"""
        """step3:操作步骤"""
        # 点击预约单-待服务，打开预约列表页面
        self.overview_page.listServer()
        # 获取预约列表页面的标题
        actual = self.overview_page.get_listServer_msg()
        """step4:断言结果"""
        # 断言实际结果与预期结果
        assert actual.text == test_data["listPaying"]

    # @pytest.mark.skip
    @allure.story("待办事项")
    @allure.title("预约单-待分配")
    @pytest.mark.parametrize("test_data",overview_data)
    def test_listAllot(self,login_web,test_data):
        """step1:初始化页面"""
        # 登录网站
        driver = login_web
        # 打开首页
        self.home_page = HomePage(driver)
        # 点击概览
        self.home_page.overview()
        # 初始化概览页面
        self.overview_page = OverviewPage(driver)
        """step2:准备数据"""
        """step3:操作步骤"""
        # 点击预约单-待分配，打开预约列表页面
        self.overview_page.listAllot()
        # 获取预约列表页面的标题
        actual = self.overview_page.get_listAllot_msg()
        """step4:断言结果"""
        # 断言实际结果与预期结果
        assert actual.text == test_data["listPaying"]

    # @pytest.mark.skip
    @allure.story("待办事项")
    @allure.title("新增潜客")
    @pytest.mark.parametrize("test_data",overview_data)
    def test_orderPaying(self,login_web,test_data):
        """step1:初始化页面"""
        # 登录网站
        driver = login_web
        # 打开首页
        self.home_page = HomePage(driver)
        # 点击概览
        self.home_page.overview()
        # 初始化概览页面
        self.overview_page = OverviewPage(driver)
        """step2:准备数据"""
        """step3:操作步骤"""
        # 点击新增预约，弹出新增预约弹窗
        self.overview_page.orderPaying()
        # 获取新增预约弹窗的标题
        actual = self.overview_page.get_orderPaying_msg()
        """step4:断言结果"""
        # 断言实际结果与预期结果
        assert actual.text == test_data["orderPaying"]

    # @pytest.mark.skip
    @allure.story("待办事项")
    @allure.title("新增潜客")
    @pytest.mark.parametrize("test_data",overview_data)
    def test_potentialCustomer(self,login_web,test_data):
        """step1:初始化页面"""
        # 登录网站
        driver = login_web
        # 打开首页
        self.home_page = HomePage(driver)
        # 点击概览
        self.home_page.overview()
        # 初始化概览页面
        self.overview_page = OverviewPage(driver)
        """step2:准备数据"""
        """step3:操作步骤"""
        # 点击新增预约，弹出新增预约弹窗
        self.overview_page.potentialCustomer()
        # 获取新增预约弹窗的标题
        actual = self.overview_page.get_potentialCustomer_msg()
        """step4:断言结果"""
        # 断言实际结果与预期结果
        assert actual.text == test_data["potentialCustomer"]

