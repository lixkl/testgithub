# coding=utf-8
from HTMLTestRunner import HTMLTestRunner
import os
import unittest
import time

def insertion_sort(data):
    '''
    for i in range(1, len(data)):
        position = i - 1
        cur = data[i]

        while position >= 0 and cur < data[position]:
            data[position + 1] = data[position]
            position = position - 1

        data[position + 1] = cur
    '''
dir = os.path.dirname(os.path.abspath('.'))  # 注意相对路径获取方
case_dir = dir + r'\testsuites' # c测试用例路径
suite= unittest.TestLoader().discover(case_dir,pattern="test*.py",top_level_dir=None) # 运行case_dir下的所有用例

if __name__ == '__main__':
    report_dir = dir + r'\test_report'
    now = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
    report_name = report_dir +'/'+now +'result.html'
    filepath = os.path.abspath(os.path.join(report_dir,report_name))
    runner = unittest.TextTestRunner()
    fp = open(filepath,'wb') # 定义测试报告存放路径
    runner = HTMLTestRunner(stream=fp,title='VOP测试报告',description='VOP测试报告') # 定义测试报告
    runner.run(suite)#执行测试用例
    fp.close()