import os
import shutil
from conf.constant import cons
import pytest


# 执行之前，清空测试报告生成目录allure_results
shutil.rmtree(cons.ALLURE_RESULTS_PATH)
# 执行测试用例，并将allure生成的测试报告文件输出到allure_results目录
pytest.main(["-vsq", "--alluredir", "./reports/allure_results"])
# 将allure生成的测试报告文件加工成真正的测试报告输出到allure_report目录
os.system(r"allure generate --clean reports/allure_results  -o reports/allure_report")


"""
-s：输出所有测试用例的print信息
-m：执行自定义标记的相关用例，例："-m='login'"
"""







