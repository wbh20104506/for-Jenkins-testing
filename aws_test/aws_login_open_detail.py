# coding:utf-8
import time

from aws_test.repeat_process import *


class Login_Open_Detail():

    def __init__(self,driver):
        self.P = Repeat_Process(driver)

    def login_url(self):
        '''登录'''
        url = "https://demo.jintelhealth.com/Analytics/#!/login"
        self.P.open_link(url) #  打开链接
        locator1 = ("id", "username")
        username = "lz_admin"
        locator2 = ("id", "password")
        psw = "Ghc2018!"
        locator3 = ("id", "loginBtn")
        self.P.login(locator1, username, locator2, psw, locator3)  # 输入用户名密码登录
        locator = ("css selector", ".box-title.container__title.ng-binding")
        print(self.P.result(locator))  # 获取登录结果

    def open_detail(self):
        '''打开明细表'''
        locator1 = ("id", "topInput")
        text = "Detail0808"
        locator2 = ("id", "myI")
        self.P.search_report(locator1, text, locator2)  # 搜索并打开报表
        time.sleep(3)

if __name__ == "__main__":
    driver = webdriver.Firefox()
    detail = Login_Open_Detail(driver)
    detail.login_url()
    detail.open_detail()