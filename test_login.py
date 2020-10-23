"""
======================
Author: 柠檬班-小简
Time: 2020/10/21 20:18
Project: py33-接口自动化
Company: 湖南零檬信息技术有限公司
======================
"""
"""
1、用例文件名：test_*.py    或者   *_test.py
2、用例：类里面的方法/函数    
   一个函数就是一个测试用例，函数名称有要求：test_开头
   函数名：用例名称
   函数体：用例步骤、断言(期望结果与实际结果比对)、测试数据
   断言：assert 表达式(结果为True表示用例通过，结果为False表示用例失败)

3、前置/后置-fixture
"""



# import allure

from login import login_check
# @allure.title("登陆成功场景")
def test_login_success():

    # 步骤
    result = login_check("nmb_python","lemonban")
    print(result)
    # 断言
    assert result == {"code": 0, "msg": "登录成功11"}




