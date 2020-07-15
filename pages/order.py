from selenium.webdriver.common.by import By
from common.basepage import BasePage


class OrderPage(BasePage):

    """订单首页"""
    #  _locator = (By.XPATH, '')
    # 全部订单标签
    _locator = (By.XPATH, '//*[@class="page-title"]/li[contains(text(),"全部订单")]')
    # 待付款标签
    _locator = (By.XPATH, '//*[@class="page-title"]/li[contains(text(),"待付款")]')
    # 待发货标签
    _locator = (By.XPATH, '//*[@class="page-title"]/li[contains(text(),"待发货")]')
    # 已发货标签
    _locator = (By.XPATH, '//*[@class="page-title"]/li[contains(text(),"已发货")]')
    # 已完成标签
    _locator = (By.XPATH, '//*[@class="page-title"]/li[contains(text(),"已完成")]')
    # 已取消标签
    _locator = (By.XPATH, '//*[@class="page-title"]/li[contains(text(),"已取消")]')
    # 已撤销标签
    _locator = (By.XPATH, '//*[@class="page-title"]/li[contains(text(),"已撤销")]')
    # 查询订单输入框
    _locator = (By.XPATH, '//*[@placeholder="输入订单编号/顾客手机号"]')
    # 查询按钮
    _locator = (By.XPATH, '//*[@class="el-input__icon el-icon-search"]')
    # 选择门店按钮
    _locator = (By.XPATH, '//*[@placeholder="选择门店"]')
    # 门店下拉选项
    _locator = (By.XPATH, '//*[contains(@x-placement,"bottom")]//li')
    # 下单时间按钮
    _locator = (By.XPATH, '//*[@placeholder="选择下单时间"]')
    # 下单时间下拉选项
    _locator = (By.XPATH, '//*[contains(@x-placement,"bottom")]//li')
    # 支付方式按钮
    _locator = (By.XPATH, '//*[@placeholder="选择支付方式"]')
    # 支付方式下拉选项
    _locator = (By.XPATH, '//*[contains(@x-placement,"bottom")]//li')
    # 订单来源按钮
    _locator = (By.XPATH, '//*[@placeholder="选择订单来源"]')
    # 订单来源下拉选项
    _locator = (By.XPATH, '//*[contains(@x-placement,"bottom")]//li')
    # 付款按钮
    _locator = (By.XPATH, '')
    # 取消订单按钮
    _locator = (By.XPATH, '')
    # 查看订单
    _locator = (By.XPATH, '')

    _locator = (By.XPATH, '')
    _locator = (By.XPATH, '')
    _locator = (By.XPATH, '')
    _locator = (By.XPATH, '')
    _locator = (By.XPATH, '')


