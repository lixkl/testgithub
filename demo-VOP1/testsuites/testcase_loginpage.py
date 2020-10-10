# coding=utf-8
import time
import unittest

from framework.browser_engine import BrowserEngine
from pageobjects.homepage import HomePage
from framework.logger import Logger

logger = Logger(logger="VOP_DLYM").getlog()


class VOP_DLYM(unittest.TestCase):

    def setUp(self):
        """
        测试固件的setUp()的代码，主要是测试的前提准备工作
        :return:
        """
        browse = BrowserEngine(self)
        self.driver = browse.open_browser(self)

    def tearDown(self):
            self.driver.quit()
    def test_VOP_DL(self):  #用例注意test开头
        """
        登陆系统并切换到VOP
        :return:
        """
        homepage = HomePage(self.driver)
        list = BrowserEngine.readjson(self)
        user = list['username']
        pwd = list['passwd']
        homepage.input_username(user)
        homepage.input_password(pwd)

        homepage.click_login()
        time.sleep(2)
        homepage.get_windows_img()
        logger.info('loginpage已截图')

        try:
            elem = self.driver.find_element_by_id('timeInfo')
            #assert '' in homepage.get_page_title()  # 调用页面对象继承基类中的获取页面标题方法
            assert (user) in self.driver.page_source
            #self.assertEqual(str(elem.text), '李嘉华')
            print('Test Pass.')
        except Exception as e:
            print('Test Fail.', format(e))
            homepage.get_windows_img()
            raise AssertionError
