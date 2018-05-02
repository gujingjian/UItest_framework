#conding=utf-8

#第四课，写个基本的用例，并导出报告，报告文件在report.py内
from selenium import webdriver
import time
import unittest


class TestLogin(unittest.TestCase):
    u'''测试登录功能'''
    #开始
    @classmethod
    def setUpClass(cls):
        t = time.strftime("%Y-%m-%d %H_%M_%S")
        print("用例开始执行"+t)

    #结束
    @classmethod
    def tearDownClass(cls):
        t = time.strftime("%Y-%m-%d-%H_%M_%S")
        print("用例执行完成"+t)
        #print(t)

    # 前置条件，打开登录页
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("https://prem2.yaolaivip.com/")
        self.driver.set_window_size(400,600)
        time.sleep(2)
        self.driver.find_element_by_link_text("我的").click()
        self.driver.find_element_by_css_selector(".color-yellow").click()

    # 正常登录
    def test_01(base):
        u'''正常登录:账号18612498560，密码123456 '''
        base.findElement(".login-input.input-phone").send_keys("18612498560")
        base.findElement(".login-input.input-password").send_keys("123456")
        base.findElement(".go-login").click()
        time.sleep(2)
        t = base.findElement(".//*[@class='username']").text
        base.assertTrue(t == "18612498560")
    # # 密码错误
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

    # 后置条件，退出登录
    def setDown(self):
        self.driver.find_element_by_css_selector(".userPic").click()
        time.sleep(2)
        self.driver.find_element_by_css_selector("#app>div>div.bg-white.m-t>div>a:nth-child(3)").click()
        time.sleep(2)
        self.driver.find_element_by_css_selector(".btn.btn-block.accountSafe-btn").click()

    # 关闭浏览器
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
