import pytest
from selenium import webdriver
from selenium.webdriver import ChromeOptions

from common.config import myconf
from conf.constant import cons
from pages.login import LoginPage

def init_web():
    # 初始化浏览器
    # 在jenkins运行时，需要配置二进制路径
    chrome_options = ChromeOptions()
    # chrome_options.add_argument("--headless"),无头选项也可以不设置
    # chrome_options.binary_location = r"C:\Users\czz\AppData\Local\Google\Chrome\Application\chrome.exe"
    chrome_options.binary_location = myconf.get('EXE','binary')
    driver = webdriver.Chrome(executable_path=cons.DRIVER_PATH,options=chrome_options)

    # 设置隐式等待
    driver.implicitly_wait(cons.IMPLICIT_TIMEOUT)
    driver.maximize_window()
    return driver

@pytest.fixture(scope='session')
def login_web():
    """登录网站"""
    driver = init_web()
    LoginPage(driver).login(mobile=myconf.get('USER','username'),pwd=myconf.get('USER','pwd'))
    yield driver
    # driver.quit()



