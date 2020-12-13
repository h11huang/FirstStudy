import pytest
from page.exit_login_page import Exit_login
from page.login_lianxi import Login


class TestExitLogin:
    @pytest.fixture()
    def login(self):
        Login().login_page()


    def test_exit(login):
        Exit_login().exit_login()

