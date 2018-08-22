# coding:utf-8
from selenium import webdriver
import time

def login():
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get("http://192.168.0.158:8082/Analytics/#!/login?returnTo=%2Flogin")
    driver.implicitly_wait(5)
    driver.find_element("id", "username").send_keys("admin")
    driver.find_element("id", "password").send_keys("root123")
    driver.find_element("id", "loginBtn").submit()
    time.sleep(5)
    admin = driver.find_elements("css selector", ".box-title.ng-binding")[0]
    print(admin.text)

