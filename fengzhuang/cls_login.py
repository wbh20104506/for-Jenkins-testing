# coding:utf-8
from selenium import webdriver
import time

class Login():
    u'''封装登录类'''
    def __init__(self, driver):
        self.driver = driver
        self.driver.maximize_window()
        self.driver.get("http://192.168.0.158:8082/Analytics/#!/login?returnTo=%2Flogin")

    def user_name(self, username):
        u'''封装输入用户名'''
        self.username = self.driver.find_element("id", "username").send_keys(username)

    def user_password(self, psw):
        u'''封装输入密码'''
        self.psw = self.driver.find_element("id", "password").send_keys(psw)

    def remember_psw(self):
        u'''封装记住密码'''
        self.psw = self.driver.find_element("id", "rememberMe").click()

    def login_button(self):
        u'''封装点击登录按钮'''
        self.lg_btn = self.driver.find_element("id", "loginBtn").click()

    def login_Steps(self, username, psw):
        u'''封装登录步骤'''
        self.user_name(username)
        self.user_password(psw)
        self.remember_psw()
        self.login_button()

    def login_result(self):
        u'''获取登录结果'''
        try:
            admin = self.driver.find_element("css selector", ".box-title.container__title.ng-binding").text
            return admin
        except:
            print("登录失败，返回空字符")
            return ""

if __name__ == "__main__":
    driver = webdriver.Firefox()
    login_Page = Login(driver)
    login_Page.login_Steps("lz_eng", "Ghc2018!")
    time.sleep(3)
    login_Page.login_result()
    result = login_Page.login_result()
    print(result)
    driver.quit()
