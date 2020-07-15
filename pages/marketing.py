from selenium.webdriver.common.by import By
from common.basepage import BasePage


class MarketingPage(BasePage):


    """营销页面"""
    # (By.XPATH, '')
    # 发券中心
    send_ticket_center_locator = (By.XPATH, '//*[@class="m-name" and text()="发券中心"]/../..')
    immediateUse_locator = (By.XPATH, '//*[text()="发券中心"]/../following-sibling::div/button[1]')
    _locator = (By.XPATH, '')
    _locator = (By.XPATH, '')


    def send_ticket_center(self):
        return self.visible_only_wait(self.send_ticket_center_locator)

    def immediateUse(self):
        return self.presence_only_wait(self.immediateUse_locator)



    def click_tt(self):
        self.driver.execute_script("arguments[0].click();", self.immediateUse())

