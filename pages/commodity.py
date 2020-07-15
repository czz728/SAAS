from selenium.webdriver.common.by import By


class CommodityPage():
    """预约页面"""
    #  _locator = (By.XPATH, '')

    """服务页面"""
    # 服务标签
    serveLabel_locator = (By.XPATH, '//*[@class="page-title"]/li[2]')
    # 新增按钮，卡项、产品页面共用
    newAdd_btn_locator = (By.XPATH, '//div[@class="headquarters_Label"]/span[1]')
    # 编辑按钮，随机选择一个，卡项、产品页面共用
    edit_btn_locator = (By.XPATH, '//*[@class="el-table__fixed-right"]//a[text()="编辑"]')
    # 下架按钮，随机选择一个，卡项、产品页面共用
    unshelve_btn_locator = (By.XPATH, '//*[@class="el-table__fixed-right"]//a[text()="下架"]')
    # 上架按钮，随机选择一个，卡项、产品页面共用
    putaway_btn_locator = (By.XPATH, '//*[@class="el-table__fixed-right"]//a[text()="上架"]')
    # 下架取消按钮，卡项、产品页面共用
    cancel_unshelve_locator = (By.XPATH, '//*[@aria-label="提示"]//div[@class="el-message-box__btns"]/button[1]')
    # 下架确定按钮，卡项、产品页面共用
    confirm_unshelve_locator = (By.XPATH, '//*[@aria-label="提示"]//div[@class="el-message-box__btns"]/button[2]')
    """新增服务页面"""
    # 服务名称输入框
    serveName_input_locator = (By.XPATH, ' //*[@placeholder="请输入20字以内的服务名称"]')
    # 服务分类下拉框
    serveCategory_locator = (By.XPATH, '//div[@class="el-input el-input--suffix"]')
    # 服务分类选项，随机选择一个
    serveCategory_options_locator = (By.XPATH, '//*[@x-placement="bottom-start"]//li')
    # 服务标签下拉框
    serveLabel_select_locator = (By.XPATH, '//div[@class="el-input el-input--medium el-input--suffix"]')
    # 服务标签，随机选择一个
    serveLabel_options_locator = (By.XPATH, '//*[@x-placement="top-start"]//li')
    # 上传图片
    upload_locator = (By.XPATH, '//*[@class="uploadBtn"]')
    # 售价输入框
    price_input_locator = (By.XPATH, '//*[contains(text(),"售价")]/following-sibling::input')
    # 划线价输入框
    linePrice_input_locator = (By.XPATH, '//*[contains(text(),"划线价")]/following-sibling::input')
    # 服务时长
    # 时长减少按钮
    duration_decrease_locator = (By.XPATH, '//*[@class="barCode"]//span[@class="el-input-number__decrease"]')
    # 时长增加按钮
    duration_increase_locator = (By.XPATH, '//*[@class="barCode"]//span[@class="el-input-number__increase"]')
    # 网店展示单选框
    # 展示选项
    onlineStore_show_locator = (By.XPATH, '//*[@class="el-radio__label" and text()="展示"]')
    # 不展示选项
    onlineStore_noshow_locator = (By.XPATH, '//*[@class="el-radio__label" and text()="不展示"]')
    # 上下架单选框
    # 上架选项
    putaway_locator = (By.XPATH, '//*[@class="el-radio__label" and text()="上架"]')
    # 不上架选项
    noPutaway_locator = (By.XPATH, '//*[@class="el-radio__label" and text()="不上架"]')
    # 排序
    # 排序增加按钮
    sort_increase_locator = (By.XPATH, '//*[contains(text(),"排序")]/..//span[@class="el-input-number__increase"]')
    # 适用门店单选框-默认全部门店
    # 全部门店选项
    allStore_option_locator = (By.XPATH, '//*[@class="el-radio__label" and text()="全部门店"]')
    # 自定义选项，后续有需要再扩展
    userDefined_option_locator = (By.XPATH, '//*[@class="el-radio__label" and text()="自定义"]')
    # 服务详情输入框
    detail_input_locator = (By.XPATH, '//*[@class="ql-editor ql-blank"]')
    # 提交服务按钮
    submit_btn_locator = (By.XPATH, '//*[contains(@class,"submit-btn")]/span[1]')
    # 取消按钮
    cancel_btn_locator = (By.XPATH, '//*[contains(@class,"submit-btn")]/span[2]')

    """管理服务分类弹窗页面"""
    # 管理服务分类按钮
    mananyServe_category_locator = (By.XPATH, '//div[@class="headquarters_Label"]/span[2]')
    # 新增分类按钮
    newCategory_btn_locator = (By.XPATH, '//*[text()="新增分类"]')
    # 分类名称输入框
    categoryName_input_locator = (By.XPATH, '//*[text()="添加分类"]/following-sibling::div/input')
    # 确定按钮
    confirm_Category_locator = (By.XPATH, '//*[@x-placement="right"]//*[@class="el-button el-button--primary el-button--mini"]')
    # 取消按钮
    cancel_Category_locator = (By.XPATH, '//*[@x-placement="right"]//*[@class="el-button el-button--default el-button--mini"]')
    # 编辑按钮
    edit_Category_locator = (By.XPATH, '')
    # 删除按钮
    del_Category_locator = (By.XPATH, '')
    """管理服务标签弹窗页面"""
    # 管理服务标签按钮
    mananyServe_label_locator = (By.XPATH, '//div[@class="headquarters_Label"]/span[3]')
    # 新增标签按钮
    newLabel_btn_locator = (By.XPATH, '//*[text()="新增标签"]')
    # 标签名称输入框
    labelName_input_locator = (By.XPATH, '//*[text()="添加标签"]/following-sibling::div/input')
    # 确定按钮
    confirm_label_locator = (By.XPATH, '//*[@x-placement="right"]//*[@class="el-button el-button--primary el-button--mini"]')
    # 取消按钮
    cancel_label_locator = (By.XPATH, '//*[@x-placement="right"]//*[@class="el-button el-button--default el-button--mini"]')

    # 门店服务标签
    storeServe_locator = (By.XPATH, '//div[@class="el-tabs__item is-top"]/span[text()="门店服务"]')
    # 查看按钮，随机选择一个
    check_serve_locator = (By.XPATH, '//*[@class="el-table__fixed-right"]//a[text()="查看"]')


    """卡项页面"""
    # 卡项标签
    cardOption_locator = (By.XPATH, '//*[@class="page-title"]/li[2]')

    """新增卡项页面"""
    # 单选卡项类别，随机选择一个
    _locator = (By.XPATH, '//*[contains(text(),"卡项类别")]/following-sibling::div//span[@class="el-radio__label"]')

    """次卡"""
    # 卡项名称输入框
    _locator = (By.XPATH, '//*[@placeholder="请输入20字以内的卡项名称"]')
    # 适用门店单选框，默认全部门店，元素定位和新增服务页面的共用
    # 添加服务按钮
    _locator = (By.XPATH, '//*[@class="addbtn"]')
    """添加服务弹窗"""
    # 服务勾选框，随机一个
    _locator = (By.XPATH, '//*[@class="server-table"]/li//span[@class="el-checkbox__input"]')
    # 确定按钮
    _locator = (By.XPATH, '//*[@aria-label="次卡管理服务"]//button[@class="el-button el-button--primary"]')
    # 选择有效期
    _locator = (By.XPATH, '//*[@class="el-radio__label" and text()="永久有效"]')
    # 单选卡片样式
    _locator = (By.XPATH, '//*[@class="el-radio__label" and text()="默认样式"]')
    # 备注输入框
    _locator = (By.XPATH, '//textarea[@class="reamrk"]')
    # 售价输入框，元素定位和新增服务页面的共用
    # 划线价输入框，元素定位和新增服务页面的共用
    # 网店展示单选框，元素定位和新增服务页面的共用
    # 上下架单选框，元素定位和新增服务页面的共用
    # 排序增加按钮，元素定位和新增服务页面的共用
    # 提交卡项按钮，元素定位和新增服务页面的共用

    """折扣卡"""
    # 卡项名称输入框
    _locator = (By.XPATH, '//*[@placeholder="请输入20字以内的卡项名称"]')
    # 适用门店单选框，默认全部门店，元素定位和新增服务页面的共用
    # 添加服务按钮，元素定位和次卡的共用
    """添加服务弹窗"""
    # 服务勾选框，随机选择一个，元素定位和次卡的共用
    # 确定按钮
    _locator = (By.XPATH, '//*[@aria-label="折扣卡管理服务"]//button[@class="el-button el-button--primary"]')
    # 选择有效期，元素定位和次卡的共用
    # 单选卡片样式，元素定位和次卡的共用
    # 备注输入框，元素定位和次卡的共用
    # 售价输入框，元素定位和新增服务页面的共用
    # 划线价输入框，元素定位和新增服务页面的共用
    # 网店展示单选框，元素定位和新增服务页面的共用
    # 上下架单选框，元素定位和新增服务页面的共用
    # 排序增加按钮，元素定位和新增服务页面的共用
    # 提交卡项按钮，元素定位和新增服务页面的共用

    """充值卡"""
    # 卡项名称输入框，元素定位和次卡的共用
    # 适用门店单选框，默认全部门店，元素定位和新增服务页面的共用
    # 选择有效期，元素定位和次卡的共用
    # 单选卡片样式，元素定位和次卡的共用
    # 备注输入框，元素定位和次卡的共用
    # 充值金额输入框
    _locator = (By.XPATH, '//*[contains(text(),"充值金额")]/following-sibling::input')
    # 赠送金额输入框
    _locator = (By.XPATH, '//*[contains(text(),"赠送金额")]/following-sibling::input')
    # 划线价输入框，元素定位和新增服务页面的共用
    # 网店展示单选框，元素定位和新增服务页面的共用
    # 上下架单选框，元素定位和新增服务页面的共用
    # 排序增加按钮，元素定位和新增服务页面的共用
    # 提交卡项按钮，元素定位和新增服务页面的共用

    """套卡"""
    # 卡项名称输入框，元素定位和次卡的共用
    # 适用门店单选框，默认全部门店，元素定位和新增服务页面的共用
    # 添加服务按钮
    _locator = (By.XPATH, '//*[@class="addbtn" and text()="添加服务"]')
    """添加服务弹窗"""
    # 服务勾选框，随机一个，元素定位和次卡的共用
    # 确定按钮
    _locator = (By.XPATH, '//*[@aria-label="套卡管理服务"]//button[@class="el-button el-button--primary"]')

    # 添加产品按钮
    _locator = (By.XPATH, '//*[@class="addbtn" and text()="添加产品"]')
    """添加产品弹窗"""
    # 添加按钮
    _locator = (By.XPATH, '//*[text()="添加"]')
    # 商品规格多选，必须全选，用for循环遍历
    _locator = (By.XPATH, '//*[@x-placement="bottom"]//li')
    # 商品规格确定按钮
    _locator = (By.XPATH, '//*[@x-placement="top"]//button[@class="el-button el-button--primary el-button--mini"]')
    # 确定按钮
    _locator = (By.XPATH, '//*[@aria-label="套卡管理产品"]//button[@class="el-button el-button--primary"]')

    # 选择有效期，元素定位和次卡的共用
    # 单选卡片样式，元素定位和次卡的共用
    # 备注输入框，元素定位和次卡的共用
    # 售价输入框，元素定位和新增服务页面的共用
    # 划线价输入框，元素定位和新增服务页面的共用
    # 网店展示单选框，元素定位和新增服务页面的共用
    # 上下架单选框，元素定位和新增服务页面的共用
    # 排序增加按钮，元素定位和新增服务页面的共用
    # 套卡详情输入框
    _locator = (By.XPATH, '//div[@class="ql-editor ql-blank"]')
    # 提交卡项按钮，元素定位和新增服务页面的共用

    """时限卡"""
    # 卡项名称输入框，元素定位和次卡的共用
    # 适用门店单选框，默认全部门店，元素定位和新增服务页面的共用
    # 添加服务按钮，元素定位和次卡的共用
    _locator = (By.XPATH, '//*[@class="addbtn"]')
    """添加服务弹窗"""
    # 服务勾选框，随机一个，元素定位和次卡的共用
    # 确定按钮
    _locator = (By.XPATH, '//*[contains(@aria-label,"时限卡")]//button[@class="el-button el-button--primary"]')
    # 选择有效期，选择月卡、年卡
    _locator = (By.XPATH, '//*[@class="el-radio__label" and text()="年卡"]')
    # 单选卡片样式，元素定位和次卡的共用
    # 备注输入框，元素定位和次卡的共用
    # 售价输入框，元素定位和新增服务页面的共用
    # 划线价输入框，元素定位和新增服务页面的共用
    # 网店展示单选框，元素定位和新增服务页面的共用
    # 上下架单选框，元素定位和新增服务页面的共用
    # 排序增加按钮，元素定位和新增服务页面的共用
    # 提交卡项按钮，元素定位和新增服务页面的共用



    """产品页面"""
    # 产品标签
    product_locator = (By.XPATH, '//*[@class="page-title"]/li[3]')
    # 新增类型，自有产品
    _locator = (By.XPATH, '//*[@class="el-radio__label" and text()="自有产品"]')
    # 产品名称
    _locator = (By.XPATH, '//*[@placeholder="请输入20字以内的产品名称"]')
    # 产品分类按钮
    _locator = (By.XPATH, '//*[contains(text(),"产品分类")]/following-sibling::div//input')
    # 产品分类下拉选项，随机选择一个
    _locator = (By.XPATH, '//*[@x-placement="bottom-start"]//li')

    # 产品标签按钮
    _locator = (By.XPATH, '//*[contains(text(),"产品标签")]/following-sibling::div//input')
    # 产品标签下拉选项，随机选择一个
    _locator = (By.XPATH, '//*[@x-placement="top-start"]//li')

    # 网店展示单选框，元素定位和新增服务页面的共用
    # 排序增加按钮，元素定位和新增服务页面的共用
    # 适用门店单选框，默认全部门店，元素定位和新增服务页面的共用
    # 添加规格类型按钮
    _locator = (By.XPATH, '//*[@class="el-button el-button--primary"]/span[text()="添加规格类型"]')
    # 规格名称
    _locator = (By.XPATH, '//*[@placeholder="请输规格名称"]')
    # 添加规则项按钮
    _locator = (By.XPATH, '//*[@class="rule el-popover__reference"]')
    # 添加规则项按钮
    _locator = (By.XPATH, '//*[@placeholder="请输入规格项名称"]')
    # 确定按钮
    _locator = (By.XPATH, '//*[text()="添加规格项"]/../following-sibling::div//span[text()="确定"]')

    # 售价输入框
    _locator = (By.XPATH, '//*[@placeholder="售价"]')
    # 成本输入框
    _locator = (By.XPATH, '//*[@placeholder="成本"]')
    # 库存设定按钮
    _locator = (By.XPATH, '//a[text()="设定"]')
    # 库存输入框，定位到多个门店
    _locator = (By.XPATH, '//input[@placeholder="库存"]')
    # 库存确定按钮
    _locator = (By.XPATH, '//*[@aria-label="设定库存"]//button[@class="el-button el-button--primary"]')

    # 产品详情输入框,元素定位和新增服务页面的服务详情输入框共用
    # 提交产品按钮，元素定位和新增服务页面的共用