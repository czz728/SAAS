"""
    @Author : CZZ
    @Date : 2020/6/11 10:10
    @Describe : 自动化测试 
    @Project : merchant
    @Module : test_demo
"""
import allure
import pytest
from pages.home import HomePage
from pages.member import MemberPage
from resource.data.test_data import member_paying_data, member_resting_data



@pytest.mark.skip
@allure.feature("会员页面")
class TestMember():
    # @pytest.mark.skip
    @allure.story("服务开单")
    @allure.title("服务收款")
    @pytest.mark.parametrize('test_data',member_paying_data)
    def test_billing_serve_paying(self,login_web,test_data):
        """会员选择一个服务开单"""
        """step1:初始化页面"""
        # 登录网站
        driver = login_web
        # 打开首页
        self.home_page = HomePage(driver)
        # 点击会员
        self.home_page.member()
        # 初始化会员页面
        self.member_page = MemberPage(driver)
        """step2:准备数据"""
        # 查询开单的会员
        self.member_page.search_member(member_info=test_data['mobile'])
        """step3:操作步骤"""

        with allure.step("1、选择服务信息"):
            self.member_page.billing_serve()

        with allure.step("2、提交收款"):
            self.member_page.paying_submit()

        with allure.step("3、确认结算"):
            self.member_page.confirm_payment_submit()

        with allure.step("4、获取收款后订单状态"):
            actual = self.member_page.get_paySuccessOrder_msg()
        """step4:断言结果"""
        assert  test_data['expected']  in  actual.text

    # @pytest.mark.skip
    @allure.story("服务开单")
    @allure.title("服务挂单")
    @pytest.mark.parametrize('test_data',member_resting_data)
    def test_billing_serve_resting(self,login_web,test_data):
        """step1:初始化页面"""
        # 登录网站
        driver = login_web
        # 打开首页
        self.home_page = HomePage(driver)
        # 点击会员
        self.home_page.member()
        # 初始化会员页面
        self.member_page = MemberPage(driver)
        """step2:准备数据"""
        # 查询开单的会员
        self.member_page.search_member(member_info=test_data['mobile'])
        """step3:操作步骤"""

        with allure.step("1、选择服务信息"):
            self.member_page.billing_serve()

        with allure.step("2、提交挂单"):
            self.member_page.resting_order_submit()

        with allure.step("3、获取挂单的订单状态"):
            actual = self.member_page.get_restingOrder_msg()
        """step4:断言结果"""
        assert  test_data['expected'] in actual.text

    # @pytest.mark.skip
    @allure.story("产品开单")
    @allure.title("产品收款")
    @pytest.mark.parametrize('test_data',member_paying_data)
    def test_billing_product_paying(self,login_web,test_data):
        """step1:初始化页面"""
        # 登录网站
        driver = login_web
        # 打开首页
        self.home_page = HomePage(driver)
        # 点击会员
        self.home_page.member()
        # 初始化会员页面
        self.member_page = MemberPage(driver)
        """step2:准备数据"""
        # 查询开单的会员
        self.member_page.search_member(member_info=test_data['mobile'])
        """step3:操作步骤"""

        with allure.step("1、选择产品信息"):
            self.member_page.billing_product()

        with allure.step("2、提交收款"):
            self.member_page.paying_submit()

        with allure.step("3、确认结算"):
            self.member_page.confirm_payment_submit()

        with allure.step("4、获取收款后订单状态"):
            actual = self.member_page.get_paySuccessOrder_msg()
        """step4:断言结果"""
        assert  test_data['expected'] in actual.text

    # @pytest.mark.skip
    @allure.story("产品开单")
    @allure.title("产品挂单")
    @pytest.mark.parametrize('test_data',member_resting_data)
    def test_billing_product_resting(self,login_web,test_data):
        """step1:初始化页面"""
        # 登录网站
        driver = login_web
        # 打开首页
        self.home_page = HomePage(driver)
        # 点击会员
        self.home_page.member()
        # 初始化会员页面
        self.member_page = MemberPage(driver)
        """step2:准备数据"""
        self.member_page.search_member(member_info=test_data['mobile'])
        """step3:操作步骤"""

        with allure.step("1、选择产品信息"):
            self.member_page.billing_product()

        with allure.step("2、提交挂单"):
            self.member_page.resting_order_submit()

        with allure.step("3、获取挂单的订单状态"):
            actual = self.member_page.get_restingOrder_msg()
        """step4:断言结果"""
        assert  test_data['expected']  in actual.text





