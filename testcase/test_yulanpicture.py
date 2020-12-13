import pytest
from page.login_page import Login
from page.yulan_picture_page import Yulan_tupian


class Test_yulanpicture:

    @pytest.fixture()
    def qianzhihouzhi(self):
        Login().login_page()
        print("打开图片文件夹")
        yield
        print("关闭浏览器")

    def test_yulanpic(self,qianzhihouzhi):
        Yulan_tupian().yulan_picture()
        assert 1 == 1

    def test_pic_xiayiye(self,qianzhihouzhi):
        Yulan_tupian().yulan_picture()
        Yulan_tupian().dianji_xiayiye()
        assert 2 == 2
