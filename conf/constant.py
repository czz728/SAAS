import os

"""
该模块不能导入common.config这个读取配置文件的模块，一导入就会报错ImportError: cannot import name，
很可能是递归导入问题，在一个py中调用另一个文件夹中的py中的方法时，由于两个py文件之间相互调用，即递归导入，导致报错
"""

class Constant(object):
    """常量Constant"""
    # 项目路径
    BASE_PATH = os.path.dirname(os.path.dirname(__file__))
    # 测试用例数据路径
    DATA_PATH = os.path.join(BASE_PATH, 'resource/data')
    # 图形验证码路径
    CAPTCHA_PATH = os.path.join(BASE_PATH, 'resource/captcha') +'/captcha.png'
    # 测试用例路径
    CASE_PATH = os.path.join(BASE_PATH, 'testcases')
    # 配置文件路径
    CONF_PATH = os.path.join(BASE_PATH, 'conf')
    # 测试报告路径
    REPORT_PATH = os.path.join(BASE_PATH, 'reports')
    # allure_report路径
    ALLURE_REPORT_PATH = os.path.join(BASE_PATH, 'reports/allure_report')
    # allure_results路径
    ALLURE_RESULTS_PATH = os.path.join(BASE_PATH, 'reports/allure_results')
    # 测试日志路径
    LOG_PATH = os.path.join(BASE_PATH,'logs')
    # 驱动存放路径
    DRIVER_PATH = os.path.join(BASE_PATH,'resource/driver') +"/chromedriver_83.exe"
    # 如果没有测试报告文件夹，自动创建
    if not os.path.exists(REPORT_PATH):
        os.mkdir(REPORT_PATH)

    SCREENSHOT_PATH = os.path.join(BASE_PATH, 'screenshot')
    # 截图存放路径，如果没有，自动创建文件夹
    if not os.path.exists(SCREENSHOT_PATH):
        os.mkdir(SCREENSHOT_PATH)

    #
    # 隐式等待超时时间
    IMPLICIT_TIMEOUT = 20
    # 常用登录用户
    # username = myconf.get('USER','username')
    # pwd = myconf.get('USER','pwd')

# 创建一个常量对象
cons= Constant()






