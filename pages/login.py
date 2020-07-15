from PIL import Image
from selenium.webdriver.common.by import By

from common.basepage import BasePage
from common.captcha import get_captcha
from common.config import myconf

from conf.constant import cons
from pages.home import HomePage


class LoginPage(BasePage):
    """登录功能"""
    # 登录页面元素
    mobile_locator = (By.XPATH, '//input[@placeholder="请输入登录账号/手机号码"]')
    pwd_locator = (By.XPATH, '//input[@placeholder="请输入密码"]')
    captcha_locator = (By.XPATH, '//input[@placeholder="请输入验证码"]')
    captcha_image_locator = (By.XPATH, '//canvas[@id="s-canvas"]')
    submit_locator = (By.XPATH, '//button[@class="submit-btn"]')
    captcha_error_locator = (By.XPATH, '//*[@id="app"]/div/div[1]/form/div[2]/ul/div[1]/span[2]')

    def get_url(self):
        """访问登录页面"""
        url = myconf.get('URL','url')
        self.driver.get(url)

    def locate_mobile_elem(self):
        """定位手机号元素"""
        return self.visible_only_wait(self.mobile_locator)

    def locate_pwd_elem(self):
        """定位密码元素"""
        return self.visible_only_wait(self.pwd_locator)

    def locate_captcha_elem(self):
        """定位验证码元素"""
        return self.visible_only_wait(self.captcha_locator)

    def locate_submit_elem(self):
        """定位登录按钮元素"""
        return self.click_wait(self.submit_locator)

    def  captcha_crop(self):
        """截图并根据图形验证码相对坐标再次分割，获取只有图形验证码的截图"""
        # 截图整个网页
        self.driver.save_screenshot(cons.CAPTCHA_PATH)
        # 定位图形验证码
        captcha_image_elem = self.visible_only_wait(self.captcha_image_locator)
        # 获取验证码图形坐标
        captcha_x = captcha_image_elem.location['x']
        captcha_y = captcha_image_elem.location['y']
        # 获取验证码宽高
        captcha_height = captcha_image_elem.size['height']
        captcha_width = captcha_image_elem.size['width']
        # 结合坐标和宽高
        captcha_xwidth = captcha_x + captcha_width
        captcha_yheight = captcha_y + captcha_height
        # 获取验证码的截图
        image_screenshot = Image.open(cons.CAPTCHA_PATH)
        image_captcha = image_screenshot.crop((captcha_x, captcha_y, captcha_xwidth, captcha_yheight))
        image_captcha.save(cons.CAPTCHA_PATH)


    def get_captcha_error(self):
        # 获取验证码错误信息
        return self.visible_only_wait(self.captcha_error_locator)

    def get_login_success(self):
        # 获取登录成功信息
        return self.visible_only_wait(HomePage.overview_text_locator)

    def login(self,mobile,pwd,frequency=3):

        """登录操作"""
        self.get_url()
        # 输入账号
        mobile_elem = self.locate_mobile_elem()
        mobile_elem.send_keys(mobile)
        # 输入密码
        pwd_elem = self.locate_pwd_elem()
        pwd_elem.send_keys(pwd)

        # 截图并获取验证码
        self.captcha_crop()
        captcha = get_captcha()
        # 输入验证码
        captcha_elem = self.locate_captcha_elem()
        captcha_elem.send_keys(captcha)
        # 点击登录按钮
        submit_elem = self.locate_submit_elem()
        submit_elem.click()

        if self.get_captcha_error().text == '验证码错误':
            login_time = 0
            while login_time < frequency:
                self.visible_only_wait(self.captcha_image_locator).click()
                self.captcha_crop()
                captcha = get_captcha()
                # 输入验证码
                captcha_elem = self.locate_captcha_elem()
                captcha_elem.clear()
                captcha_elem.send_keys(captcha)
                # 点击登录按钮
                submit_elem = self.locate_submit_elem()
                submit_elem.click()
                if self.get_login_success().text == "概览":
                    break
                login_time += 1
















