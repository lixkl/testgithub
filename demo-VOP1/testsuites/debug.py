# coding=utf-8
import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
from pip._vendor.distlib.compat import raw_input
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import json
import os
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import execjs


class VOP_QXFP():
    dir = os.path.dirname(os.path.abspath('.'))  # 注意相对路径获取方法
    chrome_driver_path = dir + '/tools/chromedriver.exe'
    ie_driver_path = dir + '/tools/IEDriverServer.exe'

    def VOP_DL(self):
        driver = webdriver.Chrome(self.chrome_driver_path)
        #driver.get('http://10.100.248.27:8081/vinda_dis/com.rst.cloud.base.framework.view.MainFrame1.d')
        driver.get('http://10.10.117.2:8081/vinda_dis/com.rst.cloud.base.framework.view.MainFrame1.d')
        driver.maximize_window()
        driver.find_element_by_id('username_').send_keys('141163')
        driver.find_element_by_id('password_').send_keys('111111')
        driver.find_element_by_xpath("// button[contains(text(), '登')]").click()

        # fi = driver.find_element_by_xpath("// span[contains(text(), '首页')]")
        try:
            driver.find_element_by_xpath("// span[contains(text(), '首页')]")
            mainpage = True
        except:
            mainpage = False
        if mainpage:
            print(mainpage)
            driver.find_element_by_xpath('//*[@class="tab tab-closeable tab-selected"]/span[1]/span[3]').click()

        xpath_VOPexpand = '//label[contains(text(), "VOP系统")]/../label[1]'
        driver.find_element_by_xpath(xpath_VOPexpand).click()
        time.sleep(2)
        driver.find_element_by_xpath('//label[contains(text(), "权限分配")]').click()
        time.sleep(2)
        if2 = driver.find_element_by_xpath('//*[@id="d_tabControlWorkarea"]/div[2]/div[1]/iframe')
        print(if2.text)
        driver.switch_to.frame(if2)
        time.sleep(2)
        '''
        driver.find_element_by_id("d_btnAddOrganize").click()
        if2 = driver.find_element_by_xpath('//*[@id="d_btnAddOrganize"]/span[1]')
        time.sleep(3)

        driver.find_element_by_id("d_textOName").send_keys('自动测试模块')
        #driver.find_element_by_class_name("d-icon d-trigger-icon-date").click()
        driver.find_element_by_css_selector("[class='d-icon d-trigger-icon-date']").click()
        time.sleep(1)
        #driver.find_element_by_id("d__uid_239").click()
        #driver.find_element_by_class_name("d-icon.pre-year-button").click()
        driver.find_element_by_css_selector("[class = 'd-icon pre-year-button']").click()
        time.sleep(1)
        driver.find_element_by_css_selector("[class = 'd-button d-button-highlight']").click()

        #driver.find_element_by_id("d__uid_238").click()
        time.sleep(1)
        driver.find_element_by_id("d_btnSaveOrganize").click()
        driver.find_element_by_id("d_btnSaveOrganize").send_keys(Keys.ENTER)
        #time.sleep(1)  # 给予一定的睡眠时间防止没有弹出警告框
        WebDriverWait(driver,20).until(EC.alert_is_present()) 
        alert = driver.switch_to.alert  # 切到弹出框
        print(alert.text)
        alert.accept()  # 确定 取消为 alert.dismiss()
        '''
        driver.find_element_by_id("d_textOrganize").send_keys('自动测试模块')
        driver.find_element_by_id("d_btnQuery").click()
        time.sleep(1)
        a = driver.find_element_by_css_selector('div[title = "自动测试模块"]')
        print(a.text)
        time.sleep(1)
        #driver.find_element_by_css_selector('.d-checkbox d-checkbox-default d-checkbox-icononly d-checkbox-unchecked').click()
        try:
            #driver.find_element_by_xpath('//*[@title="自动测试添加"]/../../td[1]/div[1]')
            #driver.find_element_by_css_selector('div[title = "自动测试模块"]')
            driver.find_element_by_xpath('//span[@class="d-checkbox d-checkbox-default d-checkbox-icononly d-checkbox-unchecked"]').click()
            #driver.find_element_by_class_name('d-checkbox.d-checkbox-default.d-checkbox-icononly.d-checkbox-unchecked')
            page = True
        except:
            page = False
        if mainpage:
            print(page)

        time.sleep(1)
        '''
        driver.find_element_by_xpath('//*[@title = "自动测试模块"]/../../td[1]/div[1]').click()
        time.sleep(1)
        driver.find_element_by_id("d_btnDelOrganize").click()
        time.sleep(2)
        alert = driver.switch_to.alert  # 切到弹出框
        print(alert.text)
        alert.accept()  # 确定 取消为 alert.dismiss()
        time.sleep(1)
        alert = driver.switch_to.alert  # 切到弹出框
        print(alert.text)
        alert.dismiss()  # 确定 取消为 alert.dismiss()
        '''
        user_choice = raw_input('Please click ENTER button to close application')
        if not user_choice:
            print("ABORTED")
            driver.quit()

        #scrip_code = 'document.querySelector("#d_btnAddOrganize > span.button-left > span.d-icon").click()'
        #driver.execute_script(scrip_code)


if __name__ == '__main__':
    a = VOP_QXFP()
    a.VOP_DL()