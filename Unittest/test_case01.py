import requests
import unittest
import os
import sys
base_path = os.getcwd()
sys.path.append(base_path)
from base.base_request import request
url = 'http://web.juhe.cn:8080/constellation/getAll'
data = {

}
host1 = '测试'


class TestCase01(unittest.TestCase):
    def setUp(self):
        print('case开始执行')

    def tearDown(self):
        print('case结束执行')

    @classmethod
    def setUpClass(cls):
        print('case 类方法开始执行')

    @classmethod
    def tearDownClass(cls):
        print('case 类方法执行结束')

    def test_04(self):
        print('case04')


    def test_01(self):
        res = request.run_main(url=url, data=data, method='get')
        print(res)
        print('第一个已经执行')
        self.assertEqual(res['resultcode'], '101', msg='key错误的')

    def test_02(self):
        print('case02')

    def test_03(self):
        print('case03')



# if __name__ == '__main__':
#     # unittest.main()
#
#     # 在pycharm中是按照case的顺序执行的
#     # 只有运行py文件的时候是按照添加顺序
#
#     suite = unittest.BaseTestSuite
#     tests = [TestCase01('test_02'), TestCase01('test_01')]
#     suite.addTests(tests)
#     runner = unittest.TestRunner()
#     runner.run(suite)

