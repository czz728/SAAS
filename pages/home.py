from selenium.webdriver.common.by import By

from common.basepage import BasePage


class HomePage(BasePage):
    """首页导航"""
    #  (By.XPATH, '')
    # 概览导航
    overview_locator = (By.XPATH, '//*[@class="icon-shouye"]')
    overview_text_locator = (By.XPATH, '//i[@class="icon-shouye"]/following-sibling::span')
    # 预约导航
    appointment_locator = (By.XPATH, '//*[@class="icon-yuyueshezhi"]')
    # 会员导航
    member_locator = (By.XPATH, '//*[@class="icon-huiyuan"]')
    # 潜客导航
    potential_locator = (By.XPATH, '//*[@class="icon-biaoqian"]')
    # 商品导航
    commodity_locator = (By.XPATH, '//*[@class="icon-icon27401"]')
    # 采购导航
    purchase_locator = (By.XPATH, '//*[@class="icons-caiwu icfont"]')
    # 订单导航
    order_locator = (By.XPATH, '//*[@class="icon-porder"]')
    # 营销导航
    marketing_locator = (By.XPATH, '//*[@class="icon-yingxiao"]')
    # 统计导航
    statistics_locator = (By.XPATH, '//*[@class="icon-tongji9"]')
    # 分析导航
    analyze_locator = (By.XPATH, '//*[@class="icon-statistics1"]')
    # 设置导航
    setting_locator = (By.XPATH, '//*[@class="icon-shezhi"]')


    def overview(self):
        """点击概览"""
        self.visible_only_wait(self.overview_locator).click()

    def appointment(self):
        """点击预约"""
        self.visible_only_wait(self.appointment_locator).click()

    def member(self):
        """点击会员"""
        self.visible_only_wait(self.member_locator).click()

    def potential(self):
        """点击潜客"""
        self.visible_only_wait(self.potential_locator).click()

    def commodity(self):
        """点击商品"""
        self.visible_only_wait(self.commodity_locator).click()

    def purchase(self):
        """点击采购"""
        self.visible_only_wait(self.purchase_locator).click()

    def order(self):
        """点击订单"""
        self.visible_only_wait(self.order_locator).click()

    def marketing(self):
        """点击营销"""
        self.visible_only_wait(self.marketing_locator).click()

    def statistics(self):
        """点击统计"""
        self.visible_only_wait(self.statistics_locator).click()

    def analyze(self):
        """点击分析"""
        self.visible_only_wait(self.analyze_locator).click()

    def setting(self):
        """点击设置"""
        self.visible_only_wait(self.setting_locator).click()





