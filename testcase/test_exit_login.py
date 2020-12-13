import pytest
from page.exit_login_page import Exit_login
from page.login_page import Login

class TestExitLogin:

    def login(self):
        Login().login_page()

    def test_exitlogin_quanding(self):
        self.login()
        Exit_login().exit_login()
        assert 1 == 1

    def test_exitlogin_quxiao(self):
        self.login()
        Exit_login().quxiao_exitlogin()
        assert 2 == 2

    def test_exitlogin_offwin(self):
        self.login()
        Exit_login().off_exitlogin()
        assert 3 == 3




