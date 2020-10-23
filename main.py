"""
======================
Author: 柠檬班-小简
Time: 2020/10/21 20:49
Project: py33-接口自动化
Company: 湖南零檬信息技术有限公司
======================
"""
import os

import pytest

if __name__ == '__main__':
    # pytest.main()  # 执行pytest命令，去收集用例，然后执行用例。当前文件所在的目录为rootdir
    pytest.main(["--alluredir=allure_testresult_files"])

    os.system('allure generate report/report_data -o report/html --clean')
    os.system('allure serve allure_testresult_files')