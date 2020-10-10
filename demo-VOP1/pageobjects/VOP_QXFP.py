# coding=utf-8
from framework.base_page import BasePage
from framework.browser_engine import BrowserEngine
import time
from framework.logger import Logger
logger = Logger(logger="QXFP").getlog()



class QXFP(BasePage,BrowserEngine):
    menu1 = "xpath=>//label[contains(text(),'VOP')]"  # VOP菜单
    expand = '''xpath=>//label[contains(text(), "VOP系统")]/../label[1]'''# 下拉按钮xpath
    menu2 = "xpath=>//label[contains(text(), '权限分配')]" # 权限分配菜单
    tab_QXFP = "xpath=>// span[contains(text(), '权限分配')]" # 权限分配菜单
    if1 = 'xpath=>//*[@id="d_tabControlWorkarea"]/div[2]/div[1]/iframe'   # 切入iframe
    #if1 = "selector_selector=>#d__uid_334 > iframe"
    addicon = "id=>d_btnAddOrganize" # 新增按钮 第一个是新增组织，第二个是新增员工
    oname = "id=>d_textOName" #组织名称
    starttime = "selector_selector=>[class='d-icon d-trigger-icon-date']" # 开始时间输入框
    lastyear = "selector_selector=>[class = 'd-icon pre-year-button']" # 日历控件的上一年按钮a
    timeconf = "selector_selector=>[class = 'd-button d-button-highlight']" # 日历控件的确定按钮
    # endtime = "id=>d_textOrganizessstr" # 结束时间
    conf = "id=>d_btnSaveOrganize" # 确认按钮
    searchbox ='id=>d_textOrganize' # 搜索框
    searchbutton = "id=>d_btnQuery" # 查询按钮
    # listfr = 'selector_selector=>div[title = "自动测试模块"]' # 断言元素

    # listfr = 'elector_selector=>div[title = "%s"]'

    selectmod = 'xpath=>//*[@title="自动测试添加"]/../../td[1]/div[1]' # 根据title找勾选框，需要设置关键字为动态
    # selectmod = 'selector_selector=>[class = 'd-checkbox d-checkbox-default d-checkbox-icononly d-checkbox-unchecked']'
    # selectmod = 'selector_selector=>//*[@title = "'+keyword+'"]/../../td[1]/div[1]'
    deletebutton = "id=>d_btnDelOrganize" # 删除按钮
    closebutton = 'xpath=>//*[@class="tab tab-closeable tab-selected"]/span[1]/span[3]' # 关闭首页按钮
    mainpage = "// span[contains(text(), '首页')]"
    staffadd = "id=>d_btnAddEmpl"
    serchstaff = "id=>d_textHint"
    staffchoice = "selector_selector=>[class='d-button d-button-default d-focused d-button-focused']"
    staffconf = "id=>d_btnSaveEmpl"



    def switch_to_QXFP(self):
        self.click(self.menu1)
        self.click(self.expand)
        time.sleep(2)
        self.click(self.menu2)
        time.sleep(1)


    def add_organization(self,text):
        time.sleep(1)
        self.switch_iframe(self.if1)
        time.sleep(2)
        self.click(self.addicon)
        time.sleep(1)
        self.type(self.oname,text)


    def select_otime_lastyear(self):
        self.click(self.starttime)
        time.sleep(1)
        self.click(self.lastyear)
        time.sleep(1)
        self.click(self.timeconf)

    '''
    def select_otime_lastyear(self,time):
        self.click(self.endtime)
        self.type(self.endtime,time)
    '''

    def confirm(self):
        self.click(self.conf)
        time.sleep(1)
        alert = self.driver.switch_to.alert  # 切到弹出框
        print(alert.text)
        alert.accept()  # 确定 取消为 alert.dismiss()


    def search(self,keyword):
        time.sleep(1)
        self.type(self.searchbox,keyword)
        time.sleep(1)
        self.click(self.searchbutton)
        logger.info('权限分配搜索关键字%s'%keyword)


    def delmod(self):
        self.click(self.selectmod)
        time.sleep(1)
        self.click(self.deletebutton)
        alert = self.driver.switch_to.alert  # 切到弹出框
        print(alert.text)
        alert.accept()  # 确定
        time.sleep(1)
        alert = self.driver.switch_to.alert  # 切到弹出框
        print(alert.text)
        alert.dismiss()  # 取消

    def closemainpage(self):
        self.click(self.closebutton)

    def isElementExist(self):
        try:
            self.driver.find_element_by_xpath("// span[contains(text(), '首页')]")
            mainpage = True
        except:
            mainpage = False
        if mainpage:
            print(mainpage)
            self.click(self.closebutton)

    def addstaffname (self,keyword):
        self.click(self.serchstaff)
        time.sleep(1)
        self.type(self.searchbox,keyword)
        self.click(self.staffchoice)
        self.click(self.staffconf)
