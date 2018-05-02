# coding=utf-8

# 第七课，公共方法封装成类
# 在定义函数的基础上，再定义类，在函数内加个self，其他保持原样，最后在调用时进行实例化

from selenium import webdriver
import time
import unittest
from test.common.basefunction import Base


class Loginpage():
    # def __init__(self):
    #     self.driver = driver

    def login(self,driver,username,pwd):
        """登录函数"""
        driver.get("https://prem2.yaolaivip.com/")
        driver.set_window_size(400,600)
        time.sleep(2)
        driver.find_element_by_link_text("我的").click()
        driver.find_element_by_css_selector(".color-yellow").click()
        # 登录
        driver.find_element_by_css_selector(".login-input.input-phone").send_keys(username)
        driver.find_element_by_css_selector(".login-input.input-password").send_keys(pwd)
        driver.find_element_by_css_selector(".go-login").click()
        time.sleep(2)
        try:
            t = driver.find_element_by_xpath(".//*[@class='username']").text
            return t
        except:
            print("登录失败！！！，返回空字符")
            return ""

if __name__ == "__main__":
    loginpage = Loginpage() # 类的实例化
    driver = webdriver.Firefox()
    result = loginpage.login(driver, "18612498560", "123456")
    print(result)
    driver.quit()
