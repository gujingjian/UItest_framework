# coding=utf-8
import time
import unittest

from common.HTMLTestRunner import HTMLTestRunner

#获取时间戳
nowtime = time.strftime("%Y-%m-%d %H_%M_%S")
# 用例地址
test_dir = r"C:\Users\ylzx\PycharmProjects\AUTOui\testcase"
# discover加载用例
discover = unittest.defaultTestLoader.discover(start_dir=test_dir,pattern="login*.py",top_level_dir=None)
print(discover)

reportpath = r"C:\report%s.html"%nowtime # 报告文件夹
fp = open(reportpath,"wb") #二进制写入

runner = HTMLTestRunner(fp,verbosity=2,title=u'测试报告demo',description=u'用例执行情况：') # verbosity=2才会有中文的注释
runner.run(discover)

