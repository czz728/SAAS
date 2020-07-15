from selenium.webdriver.common.by import By

from common.basepage import BasePage


class OverviewPage(BasePage):
    """概览页面"""
    """快捷入口-页面元素"""
    #  _locator = (By.XPATH, '')
    # 快速开单
    quickOrder_locator = (By.XPATH, '//*[@class="quickUl clearfix"]/li[1]')
    quickOrder_msg_locator = (By.XPATH, '//span[text()="收银台"]')
    # 新增预约
    newBooking_locator = (By.XPATH, '//*[@class="quickUl clearfix"]/li[2]')
    newBooking_msg_locator = (By.XPATH, '//span[@class="el-dialog__title" and text()="新增预约"]')
    newBooking_cancel_locator = (By.XPATH, '//*[@aria-label="新增预约"]/div[3]/span/button[1]')

    # 新增会员
    newMembers_locator = (By.XPATH, '//*[@class="quickUl clearfix"]/li[3]')
    newMembers_msg_locator = (By.XPATH, '//span[text()="新增会员"]')
    # 新增潜客
    newPotentialCustomer_locator = (By.XPATH, '//*[@class="quickUl clearfix"]/li[4]')
    newPotentialCustomer_msg_locator = (By.XPATH, '//span[@class="el-dialog__title" and text()="新增潜客"]')
    newPotentialCustomer_cancel_locator = (By.XPATH, '//*[@aria-label="新增潜客"]/div[3]/span/button[1]')
    """待办事项-页面元素"""
    # 预约单-待付款
    listPaying_locator = (By.XPATH, '//*[@class="matterUl clearfix"]/li[1]')
    listPaying_msg_locator = (By.XPATH, '//span[@class="el-pagination__total"]')
    listPaying_count_locator = (By.XPATH, '//*[@class="matterUl clearfix"]/li[1]/p/span[text()]')
    # 预约单-待服务
    listServer_locator = (By.XPATH, '//*[@class="matterUl clearfix"]/li[2]')
    listServer_msg_locator = (By.XPATH, '//span[@class="el-pagination__total"]')
    listServer_count_locator = (By.XPATH, '//*[@class="matterUl clearfix"]/li[2]/p/span[text()]')

    # 预约单-待分配
    listAllot_locator = (By.XPATH, '//*[@class="matterUl clearfix"]/li[3]')
    listAllot_msg_locator = (By.XPATH, '//span[@class="el-pagination__total"]')
    listAllot_count_locator = (By.XPATH, '//*[@class="matterUl clearfix"]/li[3]/p/span[text()]')

    # 开单订单-待付款
    orderPaying_locator = (By.XPATH, '//*[@class="matterUl clearfix"]/li[4]')
    orderPaying_msg_locator = (By.XPATH, '//span[@class="el-pagination__total"]')
    orderPaying_count_locator = (By.XPATH, '//*[@class="matterUl clearfix"]/li[4]/p/span[text()]')

    # 潜客跟进-待跟进
    potentialCustomer_locator = (By.XPATH, '//*[@class="matterUl clearfix"]/li[5]')
    potentialCustomer_msg_locator = (By.XPATH, '//li[text()="潜客列表"]')

    """消息推送-页面元素"""
    # 最新功能
    # latestFeatures_
    # 美业资讯
    """快捷入口-功能"""
    # 点击快速开单，打开开单页面
    def quickOrder(self):
        self.visible_only_wait(self.quickOrder_locator).click()
    def get_quickOrder_msg(self):
        return self.visible_only_wait(self.quickOrder_msg_locator)

    # 点击新增预约，弹出新增预约弹窗
    def newBooking(self):
        self.visible_only_wait(self.newBooking_locator).click()
    def get_newBooking_msg(self):
        return self.visible_only_wait(self.newBooking_msg_locator)
    def newBooking_cancel_click(self):
        self.visible_only_wait(self.newBooking_cancel_locator).click()

    # 点击新增会员，打开新增会员页面
    def newMembers(self):
        self.visible_only_wait(self.newMembers_locator).click()
    def get_newMembers_msg(self):
        return self.visible_only_wait(self.newMembers_msg_locator)

    # 点击新增潜客，弹出新增潜客弹窗
    def newPotentialCustomer(self):
        self.visible_only_wait(self.newPotentialCustomer_locator).click()
    def get_newPotentialCustomer_msg(self):
        return self.visible_only_wait(self.newPotentialCustomer_msg_locator)
    def newPotentialCustomer_cancel_click(self):
        self.visible_only_wait(self.newPotentialCustomer_cancel_locator).click()
    """待办事项-功能"""

    # 获取概览页面预约单-待付款的任务数
    def get_listPaying_count(self):
        # 获取预约单-待付款包含任务数的字符串
        listPaying_text = self.visible_only_wait(self.listPaying_count_locator).text
        # 将字符串分隔，单独返回任务数
        listPaying_list = listPaying_text.split("个")
        return listPaying_list[0]
    # 点击预约单-待付款，打开预约列表页面
    def listPaying(self):
        self.visible_only_wait(self.listPaying_locator).click()
    # 获取预约列表页面-待付款的任务数
    def get_listPaying_msg(self):

        return self.visible_only_wait(self.listPaying_msg_locator)

    # 点击预约单-待服务，打开预约列表页面
    def listServer(self):
        self.visible_only_wait(self.listServer_locator).click()
    def get_listServer_msg(self):
        return self.visible_only_wait(self.listServer_msg_locator)

    # 点击预约单-待分配，打开预约列表页面
    def listAllot(self):
        self.visible_only_wait(self.listAllot_locator).click()
    def get_listAllot_msg(self):
        return self.visible_only_wait(self.listAllot_msg_locator)

    # 点击开单订单-待付款，打开订单列表页面
    def orderPaying(self):
        self.visible_only_wait(self.orderPaying_locator).click()
    def get_orderPaying_msg(self):
        return self.visible_only_wait(self.orderPaying_msg_locator)

    # 点击潜客跟进-待跟进，打开潜客列表页面
    def potentialCustomer(self):
        self.visible_only_wait(self.potentialCustomer_locator).click()
    def get_potentialCustomer_msg(self):
        return self.visible_only_wait(self.potentialCustomer_msg_locator)

