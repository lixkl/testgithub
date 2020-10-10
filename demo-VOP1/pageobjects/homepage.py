# coding=utf-8
from framework.base_page import BasePage
from framework.browser_engine import BrowserEngine


class HomePage(BasePage,BrowserEngine):
    login_user = "id=>username_"
    login_password = "id=>password_"
    login_button = "xpath=>// button[contains(text(), '登')]"
    menu1 = "xpath=>//label[contains(text(),'VOP')]"  # VOP菜单


    def input_username(self,text):
        self.type(self.login_user,text)

    def input_password(self,text):
        self.type(self.login_password,text)

    def click_login(self):
        self.click(self.login_button)

    def switch_to_QXFP(self):
        self.click(self.menu1)
        self.click(self.expand)
        self.click(self.menu2)