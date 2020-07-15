import time

from selenium.webdriver.common.by import By

from common.basepage import BasePage
from pages.member import MemberPage


class PotentialPage(BasePage):
    """潜客首页"""
    # _locator = (By.XPATH, '')

    # 潜客列表标签
    potentialList_locator = (By.XPATH, '//*[@class="page-title"]/li[1]')
    # 潜客设置标签
    potentialSetting_locator = (By.XPATH, '//*[@class="page-title"]/li[2]')
    # 查询输入框
    search_input_locator = (By.XPATH, '//*[@placeholder="请输姓名/手机号"]')
    # 查询按钮
    search_btn_locator = (By.XPATH, '//*[@class="el-input__icon el-icon-search"]')
    # 选择意向按钮
    intention_btn_locator = (By.XPATH, '//*[contains(text(),"选择意向")]/following-sibling::div')
    # 意向级别下拉选项，随机选择；[1]全部，[2]A级，[3]B级，[4]C级，[5]D级
    intention_selects_locator = (By.XPATH, '//*[contains(@x-placement,"bottom")]//li')
    # 潜客姓名
    potential_name_locator = (By.XPATH, '//*[contains(@class,"el-table__body-wrapper")]//tbody/tr[1]//div')
    # 查询暂无数据
    search_noData_locator = (By.XPATH, '//span[text()="暂无数据"]')


    """新增潜客页面"""
    addCustomer_btn_locator = (By.XPATH, '//div[@id="newDivers"]')
    # 姓名
    name_input_locator = (By.XPATH, '//input[@placeholder="请输入姓名"]')
    # 性别，按默认的即可，label[1]代表男性，label[2]代表女性
    sex_select_locator = (By.XPATH, '//div[@class="input-block"]/label[2]')
    # 手机号
    mobile_input_locator = (By.XPATH, '//input[@placeholder="请输入手机号"]')
    # 微信号
    wechat_input_locator = (By.XPATH, '//input[@placeholder="请输入微信号"]')
    # 意向级别
    newIntention_btn_locator = (By.XPATH, '//div[@class="el-select"]')
    # 选择意向级别，和intention_select_locator共用
    # 编辑时，选定一个固定的修改，然后验证
    intention_B_locator = (By.XPATH, '//*[contains(@x-placement,"start")]//li[2]')
    # 备注
    remarks_input_locator = (By.CSS_SELECTOR, 'textarea[placeholder*="备注"]')
    # 已是会员的手机号再次新增潜客的提示信息
    prompt_msg_locator = (By.XPATH, '//*[@class="el-message__content"]')
    # 确定按钮，button[1]代表取消按钮，button[2]代表确定按钮
    new_confirm_locator = (By.XPATH, '//div[@aria-label="新增潜客"]/div[3]/span/button[2]')
    # 取消按钮
    new_cancel_locator = (By.XPATH, '//div[@aria-label="新增潜客"]/div[3]/span/button[1]')

    """编辑页面"""
    # 编辑按钮，根据tr[1]的索引，选择对应列的数据，目前是第一列
    edit_btn_locator = (By.XPATH, '//*[contains(@class,"el-table__fixed-body")]//tbody/tr[1]//a[text()="编辑"]')
    # 编辑页面的元素和新增页面的元素一致，可以共用
    # tr[1]第一列编辑的姓名元素，姓名文本包含空格
    edit_name_locator = (By.XPATH, '//*[contains(@class,"el-table__fixed-body")]//tbody/tr[1]/td[1]/div')
    # tr[1]第一列编辑的意向级别元素，意向级别文本不包含空格
    edit_intention_locator = (By.XPATH, '//*[contains(@class,"el-table__fixed-body")]//tbody/tr[1]/td[4]/div')
    # 编辑确定按钮
    edit_confirm_locator = (By.XPATH, '//div[@aria-label="编辑潜客"]/div[3]/span/button[2]')

    """跟进页面"""
    # 跟进按钮
    followUp_btn_locator = (By.XPATH, '//*[contains(@class,"el-table__fixed-body")]//tbody/tr[1]//a[text()="跟进"]')
    # 跟进记录输入框
    record_input_locator = (By.XPATH, '//*[@class="record-text"]')
    # 确定按钮，button[1]代表取消按钮，button[2]代表确定按钮
    followUp_confirm_locator = (By.XPATH, '//div[@aria-label="潜客跟进"]/div[3]/span/button[2]')


    """详情页面"""
    # 列表第一条详情按钮
    detail_btn_locator = (By.XPATH, '//*[contains(@class,"el-table__fixed-body")]//tbody/tr[1]//a[text()="详情"]')
    # 详情页面关闭按钮
    close_btn_locator = (By.XPATH, '//*[text()="关闭页面"]')
    # 详情页面编辑按钮
    detail_edit_locator = (By.XPATH, '//*[text()="编辑"]')
    # 详情页面转为会员按钮
    detail_changeMember_locator = (By.XPATH, '//*[text()="转为会员"]')
    # 添加跟进按钮
    detail_followUp_locator = (By.XPATH, '//*[text()="添加跟进"]')
    # 详情页面的潜客姓名
    detail_name_locator = (By.XPATH, '//*[@class="user-info"]/li[1]/span')
    # 详情页面的意向级别
    detail_intention_locator = (By.XPATH, '//*[@class="user-info"]/li[4]/span[2]')
    # 最新的跟进记录
    followUp_msg_locator = (By.XPATH, '//*[@class="recording"]//li[1]//p')
    # _locator = (By.XPATH, '')

    """转为会员页面
    从潜客列表页，点击进入
    转变会员页面和新增会员的元素相同，无须重复定位直接引用，转变会员页面只有生日、会员来源、营销顾问、备注未填写
    """
    member_btn_locator = (By.XPATH, '//*[contains(@class,"el-table__fixed-body")]//tbody/tr[1]//a[text()="转为会员"]')

    """潜客设置页面"""
    # 即可点击上下按键，也可以直接输入
    # A类客户
    # 上下按键，span[1]代表decrease减少，span[2]代表increase增加
    A_btn_locator = (By.XPATH, '//*[text()="A类客户"]/following-sibling::div//span[1]')
    #  输入框
    A_input_locator = (By.XPATH, '//*[text()="A类客户"]/following-sibling::div//input')

    # B类客户
    # 上下按键，span[1]代表decrease减少，span[2]代表increase增加
    B_btn_locator = (By.XPATH, '//*[text()="B类客户"]/following-sibling::div//span[1]')
    #  输入框
    B_input_locator = (By.XPATH, '//*[text()="B类客户"]/following-sibling::div//input')

    # C类客户
    # 上下按键，span[1]代表decrease减少，span[2]代表increase增加
    C_btn_locator = (By.XPATH, '//*[text()="C类客户"]/following-sibling::div//span[1]')
    #  输入框
    C_input_locator = (By.XPATH, '//*[text()="C类客户"]/following-sibling::div//input')

    # D类客户
    # 上下按键，span[1]代表decrease减少，span[2]代表increase增加
    D_btn_locator = (By.XPATH, '//*[text()="D类客户"]/following-sibling::div//span[1]')
    #  输入框
    D_input_locator = (By.XPATH, '//*[text()="D类客户"]/following-sibling::div//input')

    # 超过
    # 上下按键，span[1]代表decrease减少，span[2]代表increase增加
    Over_btn_locator = (By.XPATH, '//*[text()="超过"]/following-sibling::div//span[1]')
    #  输入框
    Over_input_locator = (By.XPATH, '//*[text()="超过"]/following-sibling::div//input')
    # 保存按钮
    save_btn_locator = (By.XPATH, '//*[text()="保存"]')
    # 成功提示信息
    success_msg_locator = (By.XPATH,'//*[@class="el-message__content"]')

    """潜客列表功能"""
    def search_potential(self,mobile):
        """潜客列表查询功能"""
        search_input = self.visible_only_wait(self.search_input_locator)
        search_input.clear()
        search_input.send_keys(mobile)
        self.visible_only_wait(self.search_btn_locator).click()

    """新增潜客功能"""
    def click_newPotential(self):
        """点击新增潜客按钮"""
        self.visible_only_wait(self.addCustomer_btn_locator).click()

    def name_input(self,name):
        # 输入姓名
        name_input = self.visible_only_wait(self.name_input_locator)
        name_input.clear()
        name_input.send_keys(name)

    def mobile_input(self,mobile):
        # 输入手机号
        self.visible_only_wait(self.mobile_input_locator).send_keys(mobile)

    def rank_select(self):
        # 意向级别选择,选择一个固定的B
        self.visible_only_wait(self.newIntention_btn_locator).click()
        self.visible_only_wait(self.intention_B_locator).click()

    def newPotential(self,name,mobile,wechat="wx123456",remarks="备注"):
        """新增潜客功能"""
        # 点击新增潜客按钮
        self.click_newPotential()
        # 录入潜客信息
        self.name_input(name)
        self.mobile_input(mobile)
        self.visible_only_wait(self.wechat_input_locator).send_keys(wechat)
        # 点击意向级别按钮
        self.visible_only_wait(self.newIntention_btn_locator).click()
        # 随机选择意向级别
        intentions = self.visible_least_wait(self.intention_selects_locator)
        self.random_select_click(intentions)
        # 输入备注
        self.visible_only_wait(self.remarks_input_locator).send_keys(remarks)
        # 点击确认
        self.click_confirm()

    def get_prompt_msg(self):
        """获取已是会员手机号再次新增潜客的提示信息"""
        return self.presence_only_wait(self.prompt_msg_locator)

    def click_confirm(self):
        """点击新增潜客的确定按钮"""
        self.click_wait(self.new_cancel_locator).click()

    def click_cancel(self):
        """点击新增潜客的取消按钮，关闭弹窗"""
        self.click_wait(self.new_cancel_locator).click()

    def get_newPotential_msg(self,mobile):
        """验证新增潜客成功，返回潜客列表首页，根据手机号查询潜客信息,返回潜客姓名"""
        self.search_potential(mobile)
        return self.visible_only_wait(self.potential_name_locator)

    """编辑功能"""

    def edit(self,name):
        """与新增潜客元素共用，功能一样，自行挑选数据改动"""
        # 点击编辑按钮
        self.click_wait(self.edit_btn_locator).click()
        # 按需要选择修改,修改用户名
        self.name_input(name)
        # 修改意向级别,选择固定的B
        self.rank_select()
        # 点击确定按钮
        self.visible_only_wait(self.edit_confirm_locator).click()

    def get_editName_msg(self):
        """获取编辑后的潜客姓名"""
        return self.visible_only_wait(self.edit_name_locator)

    def get_editIntention_msg(self):
        """获取编辑后的意向级别"""
        return self.visible_only_wait(self.edit_intention_locator)

    """跟进功能"""
    def record_input(self,record="跟进记录"):
        # 录入跟进记录
        self.visible_only_wait(self.record_input_locator).send_keys(record)

    def clicK_followUp_confirm(self):
        # 点击确认按钮
        self.visible_only_wait(self.followUp_confirm_locator).click()

    def followUp(self):
        """跟进"""
        # 点击跟进按钮
        self.visible_only_wait(self.followUp_btn_locator).click()
        # 录入跟进记录
        self.record_input()
        # 点击确认按钮
        self.clicK_followUp_confirm()


    """详情页面"""

    def open_detail(self):
        """打开详情页面"""
        # 点击详情页面
        self.visible_only_wait(self.detail_btn_locator).click()

    def close_detail(self):
        # 关闭详情页面
        self.visible_only_wait(self.close_btn_locator).click()


    def detail_edit(self,name):
        """详情页面进行编辑,与新增潜客元素共用，功能一样，自行挑选数据改动"""
        # 点击编辑按钮
        self.visible_only_wait(self.detail_edit_locator).click()
        # 按需要选择修改,修改用户名
        self.name_input(name)
        # 修改意向级别,选择固定的B
        self.rank_select()
        # 点击确定按钮
        self.visible_only_wait(self.edit_confirm_locator).click()

    def get_detailName_msg(self):
        """获取编辑后的详情页面潜客姓名"""
        return self.visible_only_wait(self.detail_name_locator)

    def get_detailIntention_msg(self):
        """获取编辑后的详情页面意向级别"""
        return self.visible_only_wait(self.detail_intention_locator)

    def detail_followUp(self,record="详情页面的跟进记录"):
        """详情页面的跟进功能"""
        # 点击添加跟进按钮
        self.click_wait(self.detail_followUp_locator).click()
        # 录入跟进记录
        self.record_input()
        # 点击确认按钮
        self.clicK_followUp_confirm()

    def get_followUp_msg(self):
        # 获取最新的跟进记录
        return self.visible_only_wait(self.followUp_msg_locator)


    """潜客转为会员功能"""

    def change_member(self):
        """
        从潜客列表页，点击进入
        转变会员页面和新增会员的元素相同，无须重复定位直接引用，转变会员页面只有生日、会员来源、营销顾问、备注未填写
        """
        # 点击转为会员
        self.visible_only_wait(self.member_btn_locator).click()
        # 选择生日
        self.visible_only_wait(MemberPage.date_btn_locator).click()
        date = self.visible_least_wait(MemberPage.date_select_locator)
        self.random_select_click(date)
        # 选择会员来源
        self.presence_only_wait(MemberPage.members_resource_locator).click()
        self.visible_only_wait(MemberPage.resource_select_locator).click()
        # 选择营销顾问
        self.visible_only_wait(MemberPage.adviser_locator).click()
        self.visible_only_wait(MemberPage.adviser_select_locator).click()
        # 点击提交
        submit = self.visible_only_wait(MemberPage.submit_btn_locator).click()
        # 提交按钮滚动到可视范围，才能点击
        # submit.location_once_scrolled_into_view
        # submit.click()

        """潜客转为会员功能"""

    def search_changeMember_msg(self, mobile):
        """验证潜客转为会员后，在潜客列表页用手机号查询，就无法查到潜客信息"""
        search_input = self.visible_only_wait(self.search_input_locator)
        search_input.clear()
        search_input.send_keys(mobile)
        self.visible_only_wait(self.search_btn_locator).click()
        return self.visible_only_wait(self.search_noData_locator)

    def search_member_msg(self, mobile):
        """验证潜客转为会员后，在会员列表页用手机号查询，可以查到转为会员的信息"""
        input_member = self.visible_only_wait(MemberPage.input_member_locator)
        input_member.clear()
        input_member.send_keys(mobile)
        self.visible_only_wait(MemberPage.search_btn_locator).click()
        return self.visible_only_wait(MemberPage.member_name_locator)

    def potentialSetting(self):
        """潜客跟进天数设置"""
        # 点击潜客设置
        self.visible_only_wait(self.potentialSetting_locator).click()
        # 点击上下键操作跟进天数
        self.visible_only_wait(self.A_btn_locator).click()
        self.visible_only_wait(self.B_btn_locator).click()
        self.visible_only_wait(self.C_btn_locator).click()
        self.visible_only_wait(self.D_btn_locator).click()
        self.visible_only_wait(self.Over_btn_locator).click()
        self.visible_only_wait(self.save_btn_locator).click()

    def get_setting_msg(self):
        # 获取返回提示信息
        return self.visible_only_wait(self.success_msg_locator)



