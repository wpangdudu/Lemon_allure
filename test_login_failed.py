"""
======================
Author: 柠檬班-小简
Time: 2020/10/21 20:38
Project: py33-接口自动化
Company: 湖南零檬信息技术有限公司
======================
"""

from login import login_check


def test_login_failed_by_wrong_user():
    # 步骤
    result = login_check("nmb_python1111","lemonban")
    # 断言
    assert result == {"code": 1, "msg": "账号或密码不正确"}

def test_login_failed_by_wrong_passwd():
    # 步骤
    result = login_check("nmb_python", "lemonban666")
    # 断言
    assert result == {"code": 1, "msg": "账号或密码不正确"}


def test_login_failed_by_no_user():
    # 步骤
    result = login_check(None, "lemonban666")
    # 断言
    assert result == {"code": 1, "msg": "所有的参数不能为空"}

def test_login_failed_by_no_passwd():
    # 步骤
    result = login_check("nmb_python", None)
    # 断言
    assert result == {"code": 1, "msg": "所有的参数不能为空"}