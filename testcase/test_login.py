import pytest
from page.login_page import Login

class TestLogin:

    login_succeed_data = [("18392314049","1234560"),("17345678956","4561237")]
    login_failure_data = [("18352654852",""),("","123456")]

    @pytest.fixture()   #fixture():括号里可以填写参数来指定前置后置级别，
                        # 'function'为用例级（不填也为function级）、'module'
                        #为模块级、'class'级
    def login_qianzhihouzhi01(self):
        print("开始登录")
        yield
        print("退出浏览器")

    # @pytest.fixture()
    # def login_qianzhihouzhi02(self):
    #     print("开始登录")
    #     yield
    #     print("刷新页面")

    @pytest.mark.parametrize('username,password',login_succeed_data)
    def test_login_succeed(self,login_qianzhihouzhi01,username,password):
        Login().login_page(username,password)
        assert 1 == 1

    @pytest.mark.parametrize('username,password',login_failure_data)
    def test_login_failure(self,login_qianzhihouzhi01,username,password):
        Login().login_page(username,password)
        assert 2 == 2
