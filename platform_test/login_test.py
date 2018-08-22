# coding:utf-8
from selenium import webdriver
from fengzhuang.cls_login import Login
import unittest

class Platform(unittest.TestCase):
    u'''登录大数据平台'''
    def setUp(self):
        self.dr = webdriver.Firefox()

    def test01(self):
        login_Page = Login(self.dr)
        login_Page.login_Steps("admin", "root123")
        login_Page.login_result()
        result = login_Page.login_result()
        self.assertEqual("仪表盘统计表", result)

    def tearDown(self):
        self.dr.quit()

if __name__ == "__main__":
    unittest.main()
