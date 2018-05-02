from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class Base():

    def __init__(self, driver):
        self.driver = driver
        self.timeout = 30
        self.poll = 0.5

     # 查找元素方法
    def findElement(self, para):
        element = WebDriverWait(self.driver, self.timeout, self.poll).until(EC.presence_of_element_located(para))
        return element

        # 通过lambda参数也可查找元素
        # element = WebDriverWait(self.driver, self.timeout, self.poll).until(lambda x: x.find_element(*para))
        # return element

    # sendkeys方法
    def sendKeys(self, para, text):
        ele = self.findElement(para)
        ele.send_keys(text)

    # click方法
    def click(self, para):
        ele = self.findElement(para)
        ele.click()

    # clear方法
    def clear(self, loctor):
            ele = self.findElement(loctor)
            ele.clear()

    # 鼠标悬停方法
    def moveToElement(self, loctor):
        ele = self.findElement(loctor)
        ActionChains(driver).move_to_element(ele).perform()

    # 判断文本存在方法
    def is_text_in_element(self,locator,text):
        '''判断text包含在元素里面的时候统一返回bool'''
        try:
             result = WebDriverWait(self.driver, self.timeout, self.poll).until(EC.text_to_be_present_in_element(locator,text))
             return result
        except:
            return False

    # 判断value存在方法
    def is_value_in_element(self,locator,text):
        '''判断value值，统一返回bool
        1.找不到元素返回False
        2.value为空返回False
        3.text不在元素的value值里返回False
        '''
        try:
             result = WebDriverWait(self.driver, self.timeout, self.poll).until(EC.text_to_be_present_in_element_value(locator,text))
             return result
        except:
            return False

    # 查找元素存在方法
    def is_element_exists(self, locator):
        try:
            self.findElement(locator)
            return True
        except:
            return False

    # 滚动到底部方法
    def js_scroll_end(self):
        js_heig = "window.scrollTo(0, document.body.scrollHeight)"
        self.driver.execute_script(js_heig)

    # 聚焦元素方法
    def js_focus(self, loctor):
        targe = self.findElement(loctor)
        self.driver.execute_script("arguments[0].scrollIntoView();", targe)

    # 回到顶部方法
    def js_scroll_top(self):
        js = "window.scrollTo(0, 0)"
        self.driver.execute_script(js)


if __name__ == "__main__":

    # driver = webdriver.Firefox()
    # base = Base(driver)
    # driver.get("http://prem2.yaolaivip.com/")
    # driver.set_window_size(400,600)
    # addr1 = ("link text","我的")
    # base.click(addr1)
    # addr2 = ("css selector",".color-yellow")
    # base.click(addr2)
    # loc1 = ("css selector",".login-input.input-phone")
    # loc2 = ("css selector",".login-input.input-password")
    # loc3 = ("css selector",".go-login")
    # base.sendKeys(loc1, "18612498560")
    # base.sendKeys(loc2, "123456")
    # base.click(loc3)
    # t = ("xpath",".//*[@class='username']")
    # result = base.is_text_in_element(t , "18612498560")
    # print(result)
    # driver.quit()

   # 聚焦元素
    driver = webdriver.Firefox()
    base = Base(driver)
    driver.get("http://www.cnblogs.com/yoyoketang/p/")
    ele = ("xpath","//h3[text()='最新评论']")
    base.js_focus(ele)
