# coding=utf-8
from common.basefunction import Base
from selenium import webdriver



class Jujiao(Base):
    # 调用base的聚焦方法
    def js_jujiao(self,ele):
        self.js_focus(ele)


if __name__ == "__main__":

    driver = webdriver.Firefox()
    driver.get("http://www.cnblogs.com/yoyoketang/p/")
    focus = Jujiao(driver)
    ele = ("xpath","//h3[text()='最新评论']")
    focus.js_jujiao(ele)
