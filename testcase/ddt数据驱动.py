#conding=utf-8
import time
import unittest
from selenium import webdriver
from page.loginpage import LoginPage
import ddt

testdata = [
    {"username":"18612498560","pwd":"123456","res":"18612498560"},
    {"username":"15810662774","pwd":"123123","res":"15810662774"}
]
@ddt.ddt
class TestLogin(unittest.TestCase):
    u'''测试登录功能'''
    #开始
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.loginpage = LoginPage(cls.driver)
        t = time.strftime("%Y-%m-%d %H_%M_%S")
        print("用例开始执行"+t)

    #结束
    @classmethod
    def tearDownClass(cls):
        t = time.strftime("%Y-%m-%d-%H_%M_%S")
        print("用例执行完成"+t)
        cls.driver.quit()

    # 登录
    def login_case(self,username,pwd):
        self.loginpage.login(username,pwd)
        res = self.loginpage.login_result()
        print(res)
        return res

    # 前置条件
    def setUp(self):
        pass

    # 后置条件，退出登录
    def tearDown(self):
        self.loginpage.logout()

    # 正常登录
    @ddt.data(*testdata)
    def test_01(self,parameter):
        # 读取testdata数据
        result = self.login_case(parameter["username"],parameter["pwd"])
        self.assertEqual(result,parameter["res"])

    # 密码错误
    # def test_02(self):
    #     u'''密码错误：账号18612498560，密码111111 '''
    #     self.driver.find_element_by_css_selector(".login-input.input-phone").send_keys("18612498560")
    #     self.driver.find_element_by_css_selector(".login-input.input-password").send_keys("111111")
    #     self.driver.find_element_by_css_selector(".go-login").click()
    #     time.sleep(2)
    #     self.assertTrue( self.driver.title == "登录")
    #
    #  # 用户不存在
    # def test_03(self):
    #     u'''用户不存在'''
    #     self.driver.find_element_by_css_selector(".login-input.input-phone").send_keys("13912345678")
    #     self.driver.find_element_by_css_selector(".login-input.input-password").send_keys("111111")
    #     self.driver.find_element_by_css_selector(".go-login").click()
    #     time.sleep(2)
    #     self.assertTrue( self.driver.title == "登录")


if __name__ == '__main__':
    unittest.main()
