import sys,os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from TestCase.login import Login


def test_login_failed_by_wrong_user():
    # 步骤
    result = Login.login_check("nmb_python1111","lemonban")
    # 断言
    assert result == {"code": 1, "msg": "账号或密码不正确"}

def test_login_failed_by_wrong_passwd():
    # 步骤
    result = Login.login_check("nmb_python", "lemonban666")
    # 断言
    assert result == {"code": 1, "msg": "账号或密码不正确"}


def test_login_failed_by_no_user():
    # 步骤
    result = Login.login_check(None, "lemonban666")
    # 断言
    assert result == {"code": 1, "msg": "所有的参数不能为空"}

def test_login_failed_by_no_passwd():
    # 步骤
    result = Login.login_check("nmb_python", None)
    # 断言
    assert result == {"code": 1, "msg": "所有的参数不能为空"}