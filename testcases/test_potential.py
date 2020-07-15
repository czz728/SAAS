import allure
import pytest
from common.parameter import random_mobile, randomname
from pages.home import HomePage
from pages.member import MemberPage
from pages.potential import PotentialPage
from resource.data.test_data import potential_data


@pytest.mark.skip
@allure.feature("潜客页面")
class TestPotential():

    @pytest.mark.skip
    @allure.story("潜客列表")
    @allure.title("已注册会员重复新增潜客")
    @pytest.mark.parametrize("test_data",potential_data)
    def test_repeatToadd(self,login_web,test_data):
        """已注册会员的手机号重复新增潜客，弹出提示信息"""
        """step1:初始化页面"""
        # 登录网站
        driver = login_web
        # 打开首页
        self.home_page = HomePage(driver)
        # 点击潜客
        self.home_page.potential()
        # 初始化潜客页面
        self.potential_page = PotentialPage(driver)
        """step2:准备数据"""
        # 随机生成姓名和手机号进行录入

        """step3:操作步骤"""
        with allure.step(" 1、点击新增潜客，打开新增潜客页面"):
            self.potential_page.click_newPotential()
        with allure.step("2、输入已注册会员的手机号，点击确定"):
            self.potential_page.mobile_input(test_data["mobile"])
            self.potential_page.click_confirm()
        with allure.step("3、获取提示信息"):
            actual = self.potential_page.get_prompt_msg()
            self.potential_page.click_cancel()
        """step4:断言结果"""
        # 断言提示信息是否正确
        assert  test_data["expected"] in actual.text


    @pytest.mark.skip
    @allure.story("潜客列表")
    @allure.title("新增潜客")
    def test_newPotential(self,login_web):
        """新增潜客后，在潜客列表验证是否新增一条潜客数据"""
        """step1:初始化页面"""
        # 登录网站
        driver = login_web
        # 打开首页
        self.home_page = HomePage(driver)
        # 点击潜客
        self.home_page.potential()
        # 初始化潜客页面
        self.potential_page = PotentialPage(driver)
        """step2:准备数据"""
        # 随机生成姓名和手机号进行录入
        name = randomname.create_name()
        mobile = random_mobile()
        """step3:操作步骤"""
        with allure.step(" 1、点击新增潜客，打开新增潜客页面，并录入潜客信息"):
            self.potential_page.newPotential(name,mobile)
        with allure.step("2、根据录入成功的潜客手机号，获取潜客姓名"):
            actual = self.potential_page.get_newPotential_msg(mobile)
        """step4:断言结果"""
        # 断言录入的潜客姓名是否是手机号查询的姓名
        assert  name in actual.text


    # @pytest.mark.skip
    @allure.story("潜客列表")
    @allure.title("潜客编辑")
    def test_edit(self,login_web):
        """编辑潜客信息，并在列表验证是否修改成功"""
        """step1:初始化页面"""
        # 登录网站
        driver = login_web
        # 打开首页
        self.home_page = HomePage(driver)
        # 点击潜客
        self.home_page.potential()
        # 初始化潜客页面
        self.potential_page = PotentialPage(driver)
        """step2:准备数据"""
        # 准备要修改的潜客姓名
        name = randomname.create_name()
        """step3:操作步骤"""
        with allure.step(" 1、点击编辑，打开潜客编辑页面，对潜客姓名和意向级别修改"):
            self.potential_page.edit(name)
        with allure.step("2、根据录入成功的潜客手机号，获取潜客姓名"):
            actual = self.potential_page.get_newPotential_msg()
        """step4:断言结果"""
        # 断言录入的潜客姓名是否是手机号查询的姓名
        assert  name in actual.text


    # @pytest.mark.skip
    @allure.story("潜客列表")
    @allure.title("潜客转为会员")
    def test_changeMember(self,login_web):
        """潜客转为会员后，分别验证潜客列表已查询不到和在会员列表能查询到"""
        """step1:初始化页面"""
        # 登录网站
        driver = login_web
        # 打开首页
        self.home_page = HomePage(driver)
        # 点击潜客
        self.home_page.potential()
        # 初始化潜客页面
        self.potential_page = PotentialPage(driver)
        # 初始化会员页面
        self.member_page = MemberPage(driver)

        """step2:准备数据"""
        # 随机生成姓名和手机号进行录入
        name = randomname.create_name()
        mobile = random_mobile()
        """step3:操作步骤"""

        with allure.step("1、点击新增潜客，打开新增潜客页面，并录入潜客信息"):
            self.potential_page.newPotential(name, mobile)
        with allure.step("2、查询到新潜客"):
            self.potential_page.search_potential(mobile)
        with allure.step("3、进行编辑"):
            self.potential_page.edit()
        with allure.step("4、进行跟进"):
            self.potential_page.followUp()
        with allure.step("5、转为会员"):
            self.potential_page.change_member()
        """step4:断言结果"""
        # 1、潜客转为会员，潜客列表就无法查询到
        actual1 = self.potential_page.search_changeMember_msg(mobile)
        assert "暂无数据" in actual1.text
        # 2、潜客转为会员，在会员列表能查询
        self.home_page.member()
        # time.sleep(2)
        actual2 = self.potential_page.search_member_msg(mobile)
        # 断言用手机查询刚转的会员姓名
        assert name in actual2.text


    @pytest.mark.skip
    @allure.story("潜客设置")
    @allure.title("设置潜客参数")
    def test_potentialSetting(self, login_web):
        """各种级别潜客跟进天数设置"""
        """step1:初始化页面"""
        # 登录网站
        driver = login_web
        # 打开首页
        self.home_page = HomePage(driver)
        # 点击潜客
        self.home_page.potential()
        # 初始化潜客页面
        self.potential_page = PotentialPage(driver)

        """step2:准备数据"""

        """step3:操作步骤"""

        with allure.step("1、点击潜客设置，打开潜客设置页面，修改跟进天数"):
            self.potential_page.potentialSetting()
        with allure.step("2、获取修改保存后的提示信息"):
            actual = self.potential_page.get_setting_msg()

        """step4:断言结果"""
        # 断言录入的潜客姓名是否是手机号查询的姓名
        assert "保存成功" == actual.text

