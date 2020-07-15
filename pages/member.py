from selenium.webdriver.common.by import By
from common.basepage import BasePage


class MemberPage(BasePage):

    """会员首页"""
    #  _locator = (By.XPATH, '')

    """会员列表页面"""
    # 会员列表标签
    member_list_locator = (By.XPATH, '//*[@class="page-title"]/li[text()="会员列表"]')
    # 门店选项
    select_shop_locator = (By.XPATH, '//div[contains(@class,"el-input--small")]/input[@placeholder="请选择"]')
    # 选中门店,根据门店名字，可以变更门店
    checked_shop_locator = (By.XPATH, '//span[text()="火少门店"]')
    # 会员输入框
    input_member_locator = (By.XPATH, '//*[@placeholder="请输入会员姓名／手机号"]')
    # 列表会员姓名，帮助潜客转为会员验证的
    member_name_locator = (By.XPATH, '//*[@class="name"]')
    # 查询按钮
    search_btn_locator = (By.XPATH, '//*[@class="el-input__icon el-icon-search"]')
    # 开单按钮，根据会员编号，可以变更会员
    billing_btn_locator = (By.XPATH, '//td[text()="1000466"]/following-sibling::td[6]/a[text()="开单"]')
    # 随机选择会员操作
    # billing_btn_locator = (By.XPATH, '//tr[@class="no-table"]/following-sibling::tr//a[text()="开单"]')
    # 详情按钮，根据会员编号，可以变更会员
    detail_btn_locator = (By.XPATH, '//td[text()="1000466"]/following-sibling::td[6]/a[text()="详情"]')
    # 随机选择会员操作
    # detail_btn_locator = (By.XPATH, '//tr[@class="no-table"]/following-sibling::tr//a[text()="详情"]')
    # 编辑按钮，根据会员编号，可以变更会员
    edit_btn_locator = (By.XPATH, '//td[text()="1000466"]/following-sibling::td[6]/a[text()="编辑"]')
    # 随机选择会员操作
    # edit_btn_locator = (By.XPATH, '//tr[@class="no-table"]/following-sibling::tr//a[text()="编辑"]')
    # 预约按钮，根据会员编号，可以变更会员
    appointment_btn_locator = (By.XPATH, '//td[text()="1000466"]/following-sibling::td[6]/a[text()="预约"]')
    # 随机选择会员操作
    # appointment_btn_locator = (By.XPATH, '//tr[@class="no-table"]/following-sibling::tr//a[text()="预约"]')

    """会员导入页面"""
    # 会员导入标签
    member_import_locator = (By.XPATH, '//*[@class="page-title"]/li[text()="会员导入"]')
    # 下载导入模板按钮
    download_template_locator = (By.XPATH, '//*[@class="download-btn"]')
    # 文件上传按钮
    upload_file_locator = (By.XPATH, '//*[@class="el-upload-dragger"]')
    # 提交按钮
    submit_uploadFile_locator = (By.XPATH, '//*[@class="submit-btn"]')
    # 提交后的提示信息
    prompt_msg_locator = (By.XPATH, '//*[@class="upload-inners"]/p[1]')
    # 确定按钮
    confirm_locator = (By.XPATH, '//*[@class="el-button el-button--primary"]')

    """会员导出页面"""
    # 会员导出标签
    member_export_locator = (By.XPATH, '//*[@class="page-title"]/li[text()="会员导出"]')
    # 选择门店按钮
    select_exportShop_locator = (By.XPATH, '//*[@class="el-input__inner"]')
    # 下拉选择门店，随机选择一个
    checked_exportShop_locator = (By.XPATH, '//*[@x-placement="bottom-start"]//li')
    # 导出会员，导出后没有提示信息无法断言是否导出成功
    export_btn_locator = (By.XPATH, '//*[@class="Tpbut"]/span')

    """新增会员页面"""
    # 新增会员按钮
    newMembers_btn_locator = (By.XPATH, '//li[@id="newMembers"]')
    # 姓名输入框
    name_input_locator = (By.XPATH, '//input[@placeholder="请输入姓名"]')
    # 手机输入框
    mobile_input_locator = (By.XPATH, '//input[@placeholder="请输入手机号"]')
    # 生日
    date_btn_locator = (By.XPATH, '//input[@placeholder="选择日期"]')
    # 生日选择，随机选择一个
    date_select_locator = (By.XPATH, '//table[@class="el-date-table"]/tbody//td')
    # 微信输入框
    wechat_input_locator = (By.XPATH, '//input[@placeholder="请输入微信号"]')
    #  会员来源下拉选择
    members_resource_locator = (By.XPATH, '//*[contains(text(),"会员来源")]/following-sibling::div')
    # 下拉框使用公共框架，暂时无法实现随机选择
    resource_select_locator = (By.XPATH, '//li[contains(@class,"el-select-dropdown__item")]/span[text()="主动进店"]')
    # 所属门店下拉选择
    department_shop_locator = (By.XPATH, '//*[contains(text(),"所属门店")]/following-sibling::div')
    # 下拉框使用公共框架，暂时无法实现随机选择
    shop_select_locator = (By.XPATH, '//li[contains(@class,"el-select-dropdown__item")]/span[text()="火少门店"]')
    # 营销顾问下拉选择
    adviser_locator = (By.XPATH, '//*[contains(text(),"营销顾问")]/following-sibling::div')
    # 下拉框使用公共框架，暂时无法实现随机选择
    adviser_select_locator = (By.XPATH, '//li[contains(@class,"el-select-dropdown__item")]/span[text()="大娟"]')
    # 提交按钮
    submit_btn_locator = (By.XPATH, '//*[text()="提交"]')

    """开单-服务页面"""
    # 服务标签
    serveLabel_locator = (By.XPATH, '//*[@id="tab-1"]/span')
    # 服务选项，有多项可随机选择
    serve_selects_locator = (By.XPATH, '//*[@id="pane-1"]/div/dl/dd')
    """开单-产品页面"""
    # 产品标签
    productLabel_locator = (By.XPATH, '//*[@id="tab-2"]/span')
    # 产品选项，有多项可随机选择
    product_selects_locator = (By.XPATH, '//*[@id="pane-2"]/div/dl/dd')
    # 产品时间
    product_time_locator = (By.XPATH, '//*[@class="product-footerlist clearfix"]/li[contains(text(),"10：00")]')
    # 产品地点
    product_place_locator = (By.XPATH, '//*[@class="product-footerlist clearfix"]/li[contains(text(),"河西走廊")]')
    # 产品确认按钮
    product_submit_locator = (By.XPATH,'//*[@class="el-button el-button--primary el-button--mini"]')
    """消费清单公共页面"""
    # 改价
    alter_price_locator = (By.XPATH, '//dd[@class="conslistLi_dl_mod"]')
    # 降价折扣
    decrease_price_locator = (By.XPATH, '//span[@class="el-input-number__decrease"]')
    # 权益选择按钮
    select_equity_locator = (By.XPATH, '//span[@class="el-popover__reference"]')
    # 选择权益，随机选择
    equity_selects_locator = (By.XPATH, '//dd[contains(@class,"equityK")]')
    # 不使用会员权益
    noEquity_select_locator = (By.XPATH, '//dd[@class="equityK_1"]')
    # 使用会员权益
    useEquity_select_locator = (By.XPATH, '//dd[@class="equityK_2"]')
    # 使用会员卡-次卡,有多个时可随机选择
    clubCard_time_locator = (By.XPATH, '//dd[@class="equityK_3"]')
    # 使用会员卡-充值卡,有多个时可随机选择
    clubCard_recharge_locator = (By.XPATH, '//dd[@class="equityK_4"]')
    # 服务技师按钮
    service_technician_locator = (By.XPATH, '//span[@class="technician el-popover__reference"]')
    # 选择服务技师,有多个时可随机选择
    technician_checkbox_locator   = (By.XPATH, '//label[@class="el-checkbox checkboxText"]/span[@class="el-checkbox__label"]')
    # 选择点客,选择技师后才能激活选择
    customer_checkbox_locator = (By.XPATH, '//label[@class="el-checkbox textCk"]/span[@class="el-checkbox__label"]')
    # 营销顾问按钮
    marketing_adviser_locator = (By.XPATH, '//span[@class="adviser el-popover__reference"]')
    # 选择营销顾问，有多个时可随机选择
    adviser_checkbox_locator = (By.XPATH, '//*[@class="choosingTech_list clearfix"]//div[@class="el-scrollbar__view"]/li')
    # 优惠券
    coupon_locator = (By.XPATH, '//b[@class="el-popover__reference"]')
    # 选择不使用优惠券
    noCoupon_select_locator = (By.XPATH, '//li[@class="Coupon1"]')
    # 优惠券,有多个时可随机选择，可能选到不使用优惠券
    coupon_select_locator = (By.XPATH, '//ul[@class="Choose_c_list"]/li')
    # 整单优惠
    discounts_locator = (By.XPATH, '//input[@placeholder="请选择整单优惠"]')
    # 下拉框使用公共框架，暂时无法实现随机选择
    discounts_select_locator = (By.XPATH, '//span[text()="折上折"]')
    # 收款按钮
    paying_locator = (By.XPATH, '//span[@class="b"]')
    # 挂单按钮
    resting_order_locator = (By.XPATH, '//span[@class="h"]')

    """开卡页面"""

    # 开卡按钮
    activateCardLabel_locator = (By.XPATH, '//li[text()="开卡"]')
    # 充值卡选项
    rechargeCard_locator = (By.XPATH, '//li[text()="充值卡"]')
    # 次卡选项
    countCard_locator = (By.XPATH, '//li[text()="次卡"]')
    # 折扣卡选项
    discountCard_locator = (By.XPATH, '//li[text()="折扣卡"]')
    # 套卡选项
    SetCard_locator = (By.XPATH, '//li[text()="套卡"]')
    # 时限卡选项
    timeLimitCard_locator = (By.XPATH, '//li[text()="时限卡"]')
    # 每种卡项下的页面，有多个卡，可以随机选择
    cardItem_locator = (By.XPATH, '//dl[@class="order_lis1 clearfix"]/dd')

    """充值页面"""
    # 充值标签
    rechargeLabel_locator = (By.XPATH, '//li[text()="充值"]')
    # 充值卡选项，可随机选择一个
    refillCard_locator = (By.XPATH, '//dl[@class="order_lis2 clearfix"]/dd')

    """结算页面"""
    # 结算方式
    # 在线支付标签
    online_payment_locator = (By.XPATH, '//*[text()="在线支付"]')
    # 扫码收款选项
    sweepCode_collection_locator = (By.XPATH, '//*[text()="扫码收款"]')
    # 生成收款码选项
    generate_paymentCode_locator = (By.XPATH, '//*[text()="生成收款码"]')

    # 线下记账标签
    offline_account_locator = (By.XPATH, '//*[text()="线下记账"]')
    # 微信
    weixin_locator = (By.XPATH, '//p[@class="weixin active"]')
    # 支付宝
    zhifubao_locator = (By.XPATH, '//p[@class="zhifubao"]')
    # 现金
    xianjin_locator = (By.XPATH, '//p[@class="xianjin"]')
    # 刷卡
    shuaka_locator = (By.XPATH, '//p[@class="shuaka"]')
    # 确认结算
    confirm_payment_locator = (By.XPATH, '//div[@class="tab-content"]/div[4]')
    # 返回重新下单
    return_locator = (By.XPATH, '//div[@class="fahnui"]')
    # 付款成功查看订单
    paySuccess_checkOrder_locator = (By.XPATH, '//a[@class="btns" and text()="查看订单"]')
    # 付款成功订单状态
    paySuccess_orderStatus_locator = (By.XPATH,'//span[@class="icon-wancheng"]/following-sibling::*')
    # 挂单成功信息
    restingSuccess_locator = (By.XPATH, '//p[@class="p_text"]')
    # 挂单查看订单
    resting_checkOrder_locator = (By.XPATH, '//button[@class="el-button el-button--small"]/span[text()="查看订单"]')
    # 挂单订单状态
    resting_orderStatus_locator = (By.XPATH,'//div[@class="status wait"]/span/span[contains(text(),"待付款")]')
    #


    def newmembers(self):
        pass

    def search_member(self,member_info=None):
        """查询会员"""
        # 下拉选择门店
        self.visible_only_wait(self.select_shop_locator).click()
        self.presence_only_wait(self.checked_shop_locator).click()
        # 输入会员手机号或姓名
        member_elem = self.visible_only_wait(self.input_member_locator)
        member_elem.clear()
        member_elem.send_keys(member_info)
        # 点击查询
        self.visible_only_wait(self.search_btn_locator).click()

    """服务功能"""
    def click_serveLabel(self):
        """点击服务标签"""
        self.visible_only_wait(self.serveLabel_locator).click()

    def select_serve(self,number=1):
        """选择服务
        默认选择一个，可自行添加
        """
        # 定到到多个服务
        serves = self.visible_least_wait(self.serve_selects_locator)
        # 随机选择
        self.random_select_click(serves,number=1)

    def alter_price(self):
        """改价"""
        # 点击改价
        self.visible_only_wait(self.alter_price_locator).click()
        # 点击折扣按钮
        self.visible_only_wait(self.decrease_price_locator).click()

    def select_equity(self):
        """选择权益"""
        # 点击请选择按钮
        self.visible_only_wait(self.select_equity_locator).click()
        # 随机选择一个权益
        equities = self.visible_least_wait(self.equity_selects_locator)
        self.random_select_click(equities)

    def select_technician(self):
        """选择服务技师"""
        # 点击服务技师按钮,有多个服务时，遍历点击选择
        technicians = self.visible_only_wait(self.service_technician_locator)
        



    def click_productLabel(self):
        """点击服务标签"""
        self.visible_only_wait(self.productLabel_locator).click()

    def click_rechargeLabel(self):
        """点击服务标签"""
        self.visible_only_wait(self.rechargeLabel_locator).click()


    def select_serve(self):
        pass

    def billing_serve(self):
        """进行开单-服务"""
        # 点击开单
        self.visible_only_wait(self.billing_btn_locator).click()
        # 多个服务，随机选择
        serves = self.visible_least_wait(self.serve_selects_locator)
        # 想实现多选服务，可以用for循环
        self.random_select_click(serves)
        # 改价
        self.visible_only_wait(self.alter_price_locator).click()
        self.visible_only_wait(self.decrease_price_locator).click()

        # 选择权益
        self.visible_only_wait(self.select_equity_locator).click()
        # 选择不使用会员权益
        self.visible_only_wait(self.noEquity_select_locator).click()
        # 选择使用会员权益
        # self.visible_only_wait(self.useEquity_select_locator).click()
        # 使用会员卡-次卡,有多个时可随机选择
        # clubCard_times = self.visible_least_wait(self.clubCard_time_locator)
        # self.random_select(clubCard_times).click()
        # 使用会员卡-充值卡,有多个时可随机选择
        # clubCard_recharges = self.visible_least_wait(self.clubCard_recharge_locator)
        # self.random_select(clubCard_recharges).click()

        # 选择服务技师
        self.visible_only_wait(self.service_technician_locator).click()
        technicians = self.visible_least_wait(self.technician_checkbox_locator)
        self.random_select_click(technicians)
        # 选择技师后，才能点击点客
        self.visible_only_wait(self.customer_checkbox_locator).click()

        # 选择营销顾问
        self.click_wait(self.marketing_adviser_locator).click()
        advisers = self.visible_least_wait(self.adviser_checkbox_locator)
        self.random_select_click(advisers)

        # 选择优惠券
        self.visible_only_wait(self.coupon_locator).click()
        # 选择不使用优惠券
        self.visible_only_wait(self.noCoupon_select_locator).click()
        # 优惠券, 有多个时可随机选择，可能选到不使用优惠券
        coupons = self.visible_least_wait(self.coupon_select_locator)
        self.random_select_click(coupons)

        # 选择整单优惠 >>>下拉框使用公共框架，暂时无法实现随机选择
        self.visible_only_wait(self.discounts_locator).click()
        self.presence_only_wait(self.discounts_select_locator).click()

    def billing_product(self):
        """开单-产品"""
        # 点击开单
        self.visible_only_wait(self.billing_btn_locator).click()
        # 点击产品
        self.visible_only_wait(self.productLabel_locator).click()
        # 选择产品，有多项可随机选择
        products = self.visible_least_wait(self.product_selects_locator)
        self.random_select_click(products)

        # 选择产品信息
        self.visible_only_wait(self.product_time_locator).click()
        self.visible_only_wait(self.product_place_locator).click()
        self.visible_only_wait(self.product_submit_locator).click()
        # 改价
        self.visible_only_wait(self.alter_price_locator).click()
        self.visible_only_wait(self.decrease_price_locator).click()
        # 选择权益
        self.visible_only_wait(self.select_equity_locator).click()
        self.visible_only_wait(self.noEquity_select_locator).click()
        # 选择优惠券
        self.visible_only_wait(self.coupon_locator).click()
        self.visible_only_wait(self.noCoupon_select_locator).click()
        # 选择整单优惠
        self.visible_only_wait(self.discounts_locator).click()
        self.visible_only_wait(self.discounts_select_locator).click()


    def activateCard_recharge(self):
        pass
    def activateCard_count(self):
        pass
    def activateCard_discount(self):
        pass
    def activateCard_Set(self):
        pass
    def activateCard_timeLimit(self):
        pass




    def paying_submit(self):
        self.visible_only_wait(self.paying_locator).click()

    def resting_order_submit(self):
        self.click_wait(self.resting_order_locator).click()


    def confirm_payment_submit(self,payment='weixin'):
        # 线下记账
        if payment == 'weixin':
            self.click_wait(self.weixin_locator).click()
        elif payment == 'zhifubao':
            self.click_wait(self.zhifubao_locator).click()
        elif payment == 'xianjin':
            self.click_wait(self.xianjin_locator).click()
        elif payment == 'shuaka':
            self.click_wait(self.shuaka_locator).click()
        else:
            print("暂不支持该支付方式")

        self.click_wait(self.confirm_payment_locator).click()

    def order_again(self):
        self.click_wait(self.return_locator).click()

    def get_paySuccessOrder_msg(self):
        self.click_wait(self.paySuccess_checkOrder_locator).click()
        return self.visible_only_wait(self.paySuccess_orderStatus_locator)


    def get_restingOrder_msg(self):
        self.click_wait(self.resting_checkOrder_locator).click()
        return self.visible_only_wait(self.resting_orderStatus_locator)

















