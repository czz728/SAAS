"""封装web页面基本操作"""
import os
import random
import time
import allure
from selenium.webdriver import Chrome, ActionChains
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from common.mylog import log
from conf.constant import cons




class BasePage:

    # 初始化浏览器
    def __init__(self, driver: Chrome):
        self.driver = driver

    """封装强制等待、显示等待两种元素定位等待方式"""

    def sleep_wait(self, locator, timeout=20, frequency=0.2):
        """
        场景：定位单个元素时
        强制等待
        locator:定位方式（By.XPATH）
        timeout:超时时间
        frequency:元素定位频率
        """
        used_time = 0  # 元素定位使用时间
        while used_time < timeout:
            try:
                elem = self.driver.find_element(*locator)
                # self.screen_shot()
                time.sleep(frequency)
                used_time += frequency
                return elem
            except NoSuchElementException as e:
                log.error(f'在用<<{locator[0]}>>方法定位<<{locator[1]}>>元素时失败==>>检查页面元素是否正确或换其他定位方式')
        # 不能在while循环里截图
        # self.screen_shot()
        #         raise e

    def presence_only_wait(self, locator, timeout=20, frequency=0.5):
        """
        场景：定位单个元素时
        显示等待-存在的元素定位
        locator:定位方式（By.XPATH）
        timeout:超时时间
        frequency:元素定位频率
        """
        try:
            wait = WebDriverWait(self.driver, timeout, poll_frequency=frequency)
            elem = wait.until(expected_conditions.presence_of_element_located(locator))
            # 将元素滚动到可见范围，放在公共方法会有冲突，定位失败
            # elem.location_once_scrolled_into_view
            # self.screen_shot()
            # log.debug('元素定位成功')
            return elem
        except  NoSuchElementException as e:
            log.error(f'在用<<{locator[0]}>>方法定位<<{locator[1]}>>元素时失败==>>检查页面元素是否正确或换其他定位方式')
            self.screen_shot()
            # raise e
        except TimeoutException as e:
            log.error(f'在用<<{locator[0]}>>方法定位<<{locator[1]}>>元素时失败==>>检查页面元素是否正确或换其他定位方式')
            self.screen_shot()
            # raise e

    def presence_least_wait(self, locator, timeout=20, frequency=0.5):
        """
        场景：定位多个元素时
        显示等待-存在的元素定位
        locator:定位方式（By.XPATH）
        timeout:超时时间
        frequency:元素定位频率
        """
        try:
            wait = WebDriverWait(self.driver, timeout, poll_frequency=frequency)
            elem = wait.until(expected_conditions.presence_of_all_elements_located(locator))
            # self.screen_shot()
            # log.debug('元素定位成功')
            return elem
        except  NoSuchElementException as e:
            log.error(f'在用<<{locator[0]}>>方法定位<<{locator[1]}>>元素时失败==>>检查页面元素是否正确或换其他定位方式')
            self.screen_shot()
            # raise e
        except TimeoutException as e:
            log.error(f'在用<<{locator[0]}>>方法定位<<{locator[1]}>>元素时失败==>>检查页面元素是否正确或换其他定位方式')
            self.screen_shot()
            # raise e

    def visible_only_wait(self, locator, timeout=20, frequency=1):
        """
        场景：定位单个元素时
        显示等待-可见的元素定位
        locator:定位方式（By.XPATH）
        timeout:超时时间
        frequency:元素定位频率
        """
        try:
            wait = WebDriverWait(self.driver, timeout, poll_frequency=frequency)
            elem = wait.until(expected_conditions.visibility_of_element_located(locator))
            # 将元素滚动到可见范围，放在公共方法会有冲突，定位失败
            # elem.location_once_scrolled_into_view
            # self.screen_shot()
            # log.info('元素定位成功')
            return elem
        except  NoSuchElementException as e:
            log.error(f'在用<<{locator[0]}>>方法定位<<{locator[1]}>>元素时失败==>>检查页面元素是否正确或换其他定位方式')
            self.screen_shot()
            # raise e
        except TimeoutException as e :
            log.error(f'在用<<{locator[0]}>>方法定位<<{locator[1]}>>元素时失败==>>检查页面元素是否正确或换其他定位方式')
            self.screen_shot()
            # raise e

    def visible_least_wait(self, locator, timeout=20, frequency=1):
        """
        场景：定位多个元素时
        显示等待-可见的元素定位
        locator:定位方式（By.XPATH）
        timeout:超时时间
        frequency:元素定位频率
        """
        try:
            wait = WebDriverWait(self.driver, timeout, poll_frequency=frequency)
            elem = wait.until(expected_conditions.visibility_of_all_elements_located(locator))
            # self.screen_shot()
            # log.debug('元素定位成功')
            return elem
        except  NoSuchElementException as e:
            log.error(f'在用<<{locator[0]}>>方法定位<<{locator[1]}>>元素时失败==>>检查页面元素是否正确或换其他定位方式')
            self.screen_shot()
            # raise e
        except TimeoutException as e :
            log.error(f'在用<<{locator[0]}>>方法定位<<{locator[1]}>>元素时失败==>>检查页面元素是否正确或换其他定位方式')
            self.screen_shot()
            # raise e

    def click_wait(self, locator, timeout=20, frequency=1):
        """
        场景：定位单个元素时
        显示等待-可点击元素定位
        locator:定位方式（By.XPATH）
        timeout:超时时间
        frequency:元素定位频率
        """
        try:
            wait = WebDriverWait(self.driver, timeout, poll_frequency=frequency)
            elem = wait.until(expected_conditions.element_to_be_clickable(locator))
            # 将元素滚动到可见范围
            # elem.location_once_scrolled_into_view
            # log.debug('元素定位成功')
            # self.screen_shot()
            return elem
        except  NoSuchElementException as e:
            log.error(f'在用<<{locator[0]}>>方法定位<<{locator[1]}>>元素时失败==>>检查页面元素是否正确或换其他定位方式')
            self.screen_shot()
            # raise e
        except TimeoutException as e:
            log.error(f'在用<<{locator[0]}>>方法定位<<{locator[1]}>>元素时失败==>>检查页面元素是否正确或换其他定位方式')
            self.screen_shot()
            # raise e

    def random_select_click(self,elements,number=1):
        """
        场景：多个元素选项时，随机选择一个
        :param elements: 定位成功的多个元素组成的列表
        :return: 返回随机选择的一个元素
        """
        select_number = 0
        while select_number<number:
            # 随机选择一个元素
            option = elements[random.randint(0,len(elements)-1)]
            # 将元素滚动到可见范围
            option.location_once_scrolled_into_view
            option.click()
            select_number += 1

    def screen_shot(self,testname=None):
        """截图"""
        # 根据执行日期生成目录
        date = time.localtime()
        date_name = '_'.join([str(date.tm_year),str(date.tm_mon),str(date.tm_mday)])
        date_dir = cons.SCREENSHOT_PATH +'\\' + date_name
        # 如果当前目录不存在就创建
        if not os.path.exists(date_dir):
            os.mkdir(date_dir)

        # 根据具体执行时间生成截图名称
        time_name = '_'.join([str(date.tm_hour),str(date.tm_min),str(date.tm_sec)])

        # screenshot_file = os.path.join(cons.SCREENSHOT_PATH, screenshot_name + '.png')
        if testname is None:
            screenshot_name = date_dir + '\\' + time_name +'.png'
            self.driver.save_screenshot(screenshot_name)
        else:
            screenshot_name = date_dir + '\\' + time_name +'_'+testname+ '.png'
            self.driver.save_screenshot(screenshot_name)

        # 结合allure测试报告，将截图粘贴在测试报告中展示
        with open(screenshot_name, mode='rb') as f:
            file = f.read()
        allure.attach(file, testname, allure.attachment_type.PNG)
        log.info(f"页面截图文件保存在：{screenshot_name}")

    def mouseOver(self,driver,hover_elem,click_elem):
        """鼠标悬停后点击操作

        """
        # 初始化动作链条对象
        action = ActionChains(driver)
        # 将鼠标悬停在对应的元素上

        action.move_to_element(hover_elem).perform()
        # 点击悬停后出现的可点击对象
        action.click(click_elem).perform()



