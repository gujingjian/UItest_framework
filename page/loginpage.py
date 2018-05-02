# coding=utf-8
from selenium import webdriver
import time
from common.basefunction import Base



class LoginPage(Base):
    a = ("link text","我的")
    b = ("css selector",".color-yellow")
    user_loc = ("css selector",".login-input.input-phone")  # 输入账号
    pwd_loc = ("css selector",".login-input.input-password")  # 输入密码
    sub_loc = ("css selector",".go-login")    # 点登录
    member = ("css selector",".userImg") #进入会员设置页
    zhanghao_loc = ("css selector",".username") # 获取username

    # 打开登录页
    def open_login_page(self):
        self.driver.get("https://prem2.yaolaivip.com/")
        self.driver.set_window_size(400,600)
        self.findElement(self.a).click()
        self.findElement(self.b).click()

    # 输入用户名
    def input_username(self,username):
        self.sendKeys(self.user_loc,username)

    # 输入密码
    def input_pwd(self,pwd):
        self.sendKeys(self.pwd_loc,pwd)

    # 点击登录按钮
    def login_button(self):
        self.click(self.sub_loc)

    # 获取登录结果
    def login_result(self):
        self.click(self.member)
        time.sleep(2)
        try:
            t = self.findElement(self.zhanghao_loc).text
            return t
        except:
            print("登录失败！！！，返回空字符")
            return ""

    # 登录流程
    def login(self,username,pwd):
        self.open_login_page()
        self.input_username(username)
        self.input_pwd(pwd)
        self.login_button()



    user_page = ("xpath",".//*[text()='账号安全']") # 定位账号安全
    logout_page = ("xpath",".//*[text()='退出登录']") # 定位退出登录

    # 定位账号安全并点击
    def userpage(self):
        self.click(self.user_page)
    # 退出
    def logoutpage(self):
        self.click(self.logout_page)

    # 退出流程
    def logout(self):
        self.userpage()
        self.logoutpage()

if __name__ == "__main__":

    driver = webdriver.Firefox()
    loginpage = LoginPage(driver) # 类的实例化
    loginpage.login("18612498560","123456")

