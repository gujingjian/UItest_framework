#conding=utf-8

#第六课，把login单独写成方法，测试用例内调用该方法，用例在testcase.py内

import time
from selenium import webdriver


def login(driver,username="18612498560",pwd="123456"):
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
    driver = webdriver.Firefox()
    result = login(driver, "18612498560", "123456")
    print(result)
    driver.quit()
