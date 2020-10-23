"""
======================
Author: 柠檬班-小简
Time: 2020/6/10 21:31
Project: py30
Company: 湖南零檬信息技术有限公司
======================
"""


# 功能逻辑
def login_check(username, password):
    """ 登录校验的函数
    :param username: 账号
    :param password: 密码
    :return: dict type
    正确的用户名密码是：nmb_python/lemonban
    并要求：用户名和密码都不能为None。
    """
    if username is not None and password is not None:
        if username == 'nmb_python' and password == 'lemonban':
            return {"code": 0, "msg": "登录成功"}
        else:
            return {"code": 1, "msg": "账号或密码不正确"}
    else:
        return {"code": 1, "msg": "所有的参数不能为空"}


"""
 cases = [
        {"title":"登陆成功","user": "nmb_python", "passwd": "lemonban", "check": {"code": 0, "msg": "登录成功"}},
        {"title":"登陆失败-密码错误","user": "nmb_python", "passwd": "lemonban11", "check": {"code": 1, "msg": "账号或密码不正确"}},
        {"title":"登陆失败-用户名错误","user": "python30", "passwd": "lemonban", "check": {"code": 1, "msg": "账号或密码不正确"}},
        {"title":"登陆失败-用户名为None","user": None, "passwd": "lemonban", "check": {"code": 1, "msg": "所有的参数不能为空"}},
        {"title":"登陆失败-密码为None","user": "nmb_python", "passwd": None, "check": {"code": 1, "msg": "所有的参数不能为空"}},
        {"title":"登陆失败-用户名和密码为None","user": None, "passwd": None, "check": {"code": 1, "msg": "所有的参数不能为空"}}
    ]
"""