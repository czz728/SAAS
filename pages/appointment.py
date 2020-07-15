import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from common.basepage import BasePage


class AppointmentPage(BasePage):
    """预约页面"""
    #  _locator = (By.XPATH, '')
    """预约大屏"""
    """新增预约页面"""
    # 新增预约按钮
    newAppointment_button_locator = (By.XPATH,'//*[@id="newAppointments"]')
    # 客人手机号
    guestMobile_input_locator = (By.XPATH,'//*[contains(text(),"到店人手机号")]/following-sibling::input')
    # 客人姓名
    guestName_input__locator = (By.XPATH, '//*[contains(text(),"到店人姓名")]/following-sibling::input')
    # 预约门店
    appointmentShop_locator = (By.XPATH, '//*[contains(text(),"预约门店")]/following-sibling::div')
    # 选中门店，可随机选择一个
    shop_selects_locator = (By.XPATH, '//*[@x-placement="bottom-start"]//li[contains(@class,"el-select-dropdown__item")]')
    # 到店日期
    arrival_date_locator = (By.XPATH, '//*[@aria-label="新增预约"]//input[@placeholder="选择日期"]')
    # 选择具体日期，随机选择一个
    arrivalDate_selects_locator = (By.XPATH, '//div[@x-placement="bottom-start"]//*[@class="el-date-table"]//td[contains(@class,"available")]')
    # 到店时间
    arrival_time_locator = (By.XPATH, '//*[@placeholder="选择时间"]')
    # 选择具体时间，随机选择一个
    arrivalTime_selects_locator = (By.XPATH,'//*[@class="time-select-item"]')
    # 服务项目
    services_locator = (By.XPATH, '//*[contains(text(),"服务项目")]/following-sibling::div')
    # 选择具体服务,随机选择一个
    services_selects_locator = (By.XPATH, '//*[@x-placement="bottom-start"]//li')
    # 服务技师
    technician_locator = (By.XPATH, '//*[contains(text(),"服务技师:")]/following-sibling::input')
    # 选择具体技师,随机选择一个
    technician_selects_locator = (By.XPATH, '//label[@class="el-checkbox"]/span[2]')
    # 备注
    remarks_input_locator = (By.XPATH, '//*[contains(text(),"备注")]/following-sibling::textarea')
    # 确定按钮
    appointment_submit_locator = (By.XPATH, '//*[@class="dialog-footer"]/button[4]')


    """锁定时间页面"""
    # _locator = (By.XPATH, '')
    # 锁定时间按钮
    lockTime_button_locator = (By.XPATH, '//*[@class="lock-time"]')
    # 锁定日期
    lockDate_locator = (By.XPATH, '//*[@aria-label="锁定时间"]//input[@placeholder="选择日期"]')
    # 选择具体日期，随机选择一个
    lockDate_selects_locator = (By.XPATH, '//div[@x-placement="bottom-start"]//*[@class="el-date-table"]//td[contains(@class,"available")]')
    # 锁定员工
    lockStaff_locator = (By.XPATH, '//*[contains(text(),"锁定员工")]/following-sibling::div')
    # 选择具体员工，随机选择一个
    lockStaff_select_locator = (By.XPATH, '//*[@x-placement="bottom-start"]//li')
    # 锁定时间
    lockStart_locator = (By.XPATH, '//*[@class="locked-dialog"]/p/span[contains(text(),"锁定时间")]/following-sibling::div[1]')
    lockStart_select_locator = (By.XPATH, '//div[@class="el-scrollbar__view"]/div[@class="time-select-item"][1]')
    lockEnd_locator = (By.XPATH, '//*[@class="locked-dialog"]/p/span[contains(text(),"锁定时间")]/following-sibling::div[2]')
    lockEnd_select_locator = (By.XPATH, '//div[@x-placement="bottom-start"]/div/div/div/div[@class="time-select-item"][1]')
    # 确定按钮
    lockTime_Submit_locator = (By.XPATH, '//div[@class="el-dialog__body"]/following-sibling::div/span/button[2]')

    """预约列表"""
    reservationList_locator = (By.XPATH, '//li[@class="router-link-active"]')
    cancelReservation_button_locator = (By.XPATH, '//div[@class="el-table__fixed-body-wrapper"]/table/tbody/tr[1]/td[9]/div[1]/div[1]/span[1]')
    alter_button_locator = (By.XPATH, '//div[@class="el-table__fixed-body-wrapper"]/table/tbody/tr[1]/td[9]/div[1]/div[1]/span[2]')
    billing_button_locator = (By.XPATH, '//div[@class="el-table__fixed-body-wrapper"]/table/tbody/tr[1]/td[9]/div[1]/div[1]/span[3]')
    veiw_button_locator = (By.XPATH, '//div[@class="el-table__fixed-body-wrapper"]/table/tbody/tr[1]/td[9]/div[1]/div[2]/span[1]')





    def newAppointment(self):
        """新增预约"""
        # 点击预约首页的新增预约按钮
        self.presence_only_wait(self.newAppointment_button_locator).click()
        # 输入到店人手机号
        self.visible_only_wait(self.guestMobile_input_locator).send_keys('13298211677')
        # 输入到店人姓名
        self.visible_only_wait(self.guestName_input__locator).send_keys('小明')
        # 预约门店  使用默认选择的
        # self.visible_only_wait(self.shop_select_locator).click()
        # self.presence_wait(self.checked_shop_locator).click()
        # 选择到店时间
        self.visible_only_wait(self.arrival_time_locator).click()
        # 到店时间是根据当前时间变动的，固定到20:00并滚动到再点击
        elem = self.visible_only_wait(self.arrivalTime_selects_locator)
        elem.location_once_scrolled_into_view
        elem.click()
        # 选择服务项目
        self.visible_only_wait(self.services_locator).click()
        self.visible_only_wait(self.services_select_locator).click()
        # 选择服务技师
        self.visible_only_wait(self.technician_locator).click()
        self.visible_only_wait(self.technician_select_locator).click()
        # 输入备注
        self.visible_only_wait(self.remarks_input_locator).send_keys('备注')
        # 点击确定
        self.visible_only_wait(self.appointment_submit_locator).click()


    def lockTime(self):
        """锁定时间"""
        # 点击锁定时间按钮
        self.visible_only_wait(self.lockTime_button_locator).click()
        # 选择锁定员工
        self.visible_only_wait(self.lockStaff_locator).click()
        self.visible_only_wait(self.lockStaff_select_locator).click()
        # 选择锁定时间
        # 开始时间
        self.visible_only_wait(self.lockStart_locator).click()
        start = self.visible_only_wait(self.lockStart_select_locator)
        start.location_once_scrolled_into_view
        start.click()
        # 结束时间
        # 是根据开始时间自动计算结束时间，需要加强制等待
        time.sleep(2)
        self.visible_only_wait(self.lockEnd_locator).click()
        end = self.visible_only_wait(self.lockEnd_select_locator)
        end.location_once_scrolled_into_view
        end.click()
        # 点击确定
        self.visible_only_wait(self.lockTime_Submit_locator).click()







