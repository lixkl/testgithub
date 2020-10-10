# coding=utf-8
import time
import unittest
from pip._vendor.distlib.compat import raw_input
from framework.browser_engine import BrowserEngine
from pageobjects.homepage import HomePage
from pageobjects.VOP_QXFP import QXFP
from framework.logger import Logger
logger = Logger(logger="VOP_QXFP").getlog()


class VOP_QXFP_addstaff(unittest.TestCase):
    @classmethod
    def setUp(self):
        """
        测试固件的setUp()的代码，主要是测试的前提准备工作
        :return:
        """
        browse = BrowserEngine(self)
        self.driver = browse.open_browser(self)

    @classmethod
    def tearDown(self):
        try:
            qxpage = QXFP(self.driver)
            time.sleep(2)
            qxpage.delmod()
            logger.info('后置处理已删除测试组织')
            time.sleep(2)
        except Exception as e:
            logger.info('后置处理失败，删除失败')
            print(e)

        # 运行页面停留使用这个函数
        user_choice = raw_input('Please click ENTER button to close application')
        if not user_choice:
            print("ABORTED")
            self.driver.quit()

        self.driver.quit()

    def VOP_DL(self):
        """
        系统登录页面切换到VOP
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
        logger.info('前置处理-登录')

    def test_VOP_QXFP_ADDOrg(self):
        """
        VOP添加员工用例：搜索员工，添加员工，删除员工
        :return:
        """
        self.VOP_DL()
        homepage = HomePage(self.driver)
        qxpage = QXFP(self.driver)
        self.driver.implicitly_wait(5)
        qxpage.isElementExist()
        self.driver.implicitly_wait(1)
        qxpage.switch_to_QXFP()
        logger.info("切换到VOP权限分配页面")
        time.sleep(2)
        '''
        qxpage.add_organization("自动测试添加")
        logger.info("添加组织-自动测试添加")
        time.sleep(1)
        qxpage.select_otime_lastyear()
        logger.info("填写开始时间为上一年")
        time.sleep(1)
        qxpage.confirm()
        logger.info("已添加组织，截图并开始断言")
        time.sleep(2)
        homepage.get_windows_img()  # 调用基类截图方法
        '''


        try:
            keyword = "自动测试添加"
            qxpage.search(keyword)
            time.sleep(1)
            self.driver.implicitly_wait(2)
            # assert '' in homepage.get_page_title()  # 调用页面对象继承基类中的获取页面标题方法
            elem = self.driver.find_element_by_css_selector('div[title = "' + keyword + '"]')
            logger.info("断言-通过搜索判断是否查询到已添加的组织，有则通过")
            # self.assertEqual(str(elem.text), keyword)
            self.assertEqual(str(elem.text), '错误的')
            logger.info("搜索到添加的组织，用例通过")
            print('Test Pass.')
        except Exception as e:
            logger.info("无法搜索到添加的组织，用例失败")
            homepage.get_windows_img()
            print('Test Fail.', format(e))
            raise AssertionError


if __name__ == '__main__':
    unittest.main()

