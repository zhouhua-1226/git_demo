import os
import time
import unittest
from HTMLTestRunner import HTMLTestRunner

if __name__ == '__main__':
    # 测试套件，用于测试部分用例
    # suite = unittest.TestSuite()
    # suite.addTest(Login("test01_baili"))
    # unittest.main(defaultTest="suite")

    # 获取测试用例
    suite = unittest.TestSuite()
    testcases = unittest.defaultTestLoader.discover(os.getcwd(), "*.py")
    suite.addTests(testcases)

    # unittest.TextTestRunner(verbosity=2).run(suite)
    # unittest.main(defaultTest="suite")
    # print(os.getcwd())
    nowtime = time.strftime("%Y-%m-%d %H-%M-%S", time.localtime())
    name = open(os.getcwd()+"/"+nowtime+"_report.html", "wb")
    runner = HTMLTestRunner(stream=name, verbosity=2, title="测试报告", description="报告详情如下:")  # 生成html报告
    runner.run(suite)

