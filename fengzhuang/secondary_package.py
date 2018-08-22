# coding:utf-8
from selenium import webdriver
from selenium.common.exceptions import *  # 导入所有异常类
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class Lzhang():
    u'''基于原生的selenium框架做了二次封装'''
    def __init__(self):
        u'''启动浏览器参数化，默认启动Firefox'''
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()

    def get(self, url):
        u'''使用get打开url'''
        self.driver.get(url)

    def find_element(self, location, timeout=10):
        u'''定位元素单数封装'''
        element = WebDriverWait(self.driver, timeout, 1).until(EC.presence_of_element_located(location))
        return element

    def find_elements(self, locations, timeout=10):
        u'''定位元素复数封装'''
        elements = WebDriverWait(self.driver, timeout, 1).until(EC.presence_of_all_elements_located(locations))
        return elements

    def click(self, locator):
        u'''点击操作封装'''
        element = self.find_element(locator)
        element.click()

    def send_keys(self, locator, text):
        u'''封装发送文本，清空后输入'''
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

if __name__ == "__main__":
    a = Lzhang()  # 启动firefox
    a.get("http://192.168.0.158:8081/Analytics/#!/login?returnTo=%2Flogin")  # 打开链接
    user_location = ("id", "username")  # 用户名元素
    a.send_keys(user_location, "admin")  # 输入用户名
    psw_location = ("id", "password")  # 密码元素
    a.send_keys(psw_location, "root123")  # 输入密码
    login_button = ("id", "loginBtn")  # 登录按钮元素
    a.click(login_button)  # 点击登录按钮
    report_location = ("css selector", ".box-title.ng-binding")  # 报表总名称元素
    report_name = a.find_element(report_location, 10)  # 定位报表总名称
    print(report_name.text)  # 打印报表总名称
    report_locations = ("css selector", ".box-title.ng-binding")  # 多个报表元素
    report_names = a.find_elements(report_locations, 10)  # 定位多个报表
    print(report_names[1].text)  # 打印第二个报表名称
