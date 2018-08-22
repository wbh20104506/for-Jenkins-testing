# coding:utf-8

from selenium import webdriver
from selenium.webdriver.common.base import *
from fengzhuang.repeat_process import *
from fengzhuang.login_open_detail import *

import unittest
import time

class Test_Detail(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        '''登录'''
        cls.driver = webdriver.Firefox()
        detail = Login_Open_Detail(cls.driver)
        detail.Login()

    @classmethod
    def tearDownClass(cls):
         cls.driver.quit()

    def setUp(self):
        '''打开明细表'''
        detail = Login_Open_Detail(self.driver)
        detail.Open_Detail()
        self.P = Repeat_Process(self.driver)

    def test_01(self):
        '''测试能成功添加快速过滤器'''
        locator_Add_Filter = ("css selector", ".basic-filter__icon.iconfont.icon-dropdown")
        locator_Quick = ("xpath", ".//*[@id='collapse']/div/div[1]/ul/li[1]/a/uib-tab-heading")
        locator_Input_Text = ("xpath", ".//*[@id='collapse']/div/div[1]/div/div[1]/div/ul[2]/li[1]/div[2]/div/div/div/textarea")
        text = "2"
        Operation_List = ("xpath",".//*[@id='collapse']/div/div[1]/div/div[1]/div/ul[2]/li[1]/div[3]/div/div[1]")
        Operation = ("xpath",".//*[@id='collapse']/div/div[1]/div/div[1]/div/ul[2]/li[1]/div[3]/div/div[2]/div/div/div[2]/div")
        locator_Apply_Filter = ("id", "refresh-filter")
        self.P.Add_Quick_Filter(locator_Add_Filter, locator_Quick, locator_Input_Text,text,Operation_List,Operation, locator_Apply_Filter)
        locator_Result = ("xpath", ".//*[@id='table']/tbody/tr[7]/td[5]")
        result = self.P.Result(locator_Result)
        print(result)
        self.assertEqual("2", result)

    def test_02(self):
        '''测试能成功添加Basic过滤器'''
        locator_Add_Filter = ("css selector", ".basic-filter__icon.iconfont.icon-dropdown")
        locator_Basic = ("xpath",".//*[@id='collapse']/div/div[1]/ul/li[2]/a")
        locator_Add_Button = ("xpath",".//*[@id='collapse']/div/div[1]/div/div[2]/div/div/button")
        locator_Field_List = ("xpath",".//*[@id='collapse']/div/div[1]/div/div[2]/ul/li/div[1]/div[2]/div/div[1]")
        locator_Field = ("xpath",".//*[@id='collapse']/div/div[1]/div/div[2]/ul/li/div[1]/div[2]/div/div[2]/div/div/div[10]/div/span")
        locator_Operation_List = ("xpath",".//*[@id='collapse']/div/div[1]/div/div[2]/ul/li/div[2]/div/div[1]")
        locator_Operation =("xpath",".//*[@id='collapse']/div/div[1]/div/div[2]/ul/li/div[2]/div/div[2]/div/div/div[2]/div/span")
        locator_Field_Text =("xpath",".//*[@id='collapse']/div/div[1]/div/div[2]/ul/li/div[3]/div/div/div/textarea")
        text = "9"
        locator_Apply_Filter = ("id", "refresh-filter")
        self.P.Add_Basic_Filter(locator_Add_Filter,locator_Basic,locator_Add_Button,locator_Field_List,locator_Field,
                           locator_Operation_List,locator_Operation,locator_Field_Text,text,locator_Apply_Filter)
        locator_Result = ("xpath",".//*[@id='table']/tbody/tr[1]/td[14]")
        result = self.P.Result(locator_Result)
        print(result)
        self.assertEqual("9",result)

    def test_03(self):
        u'''测试收藏报表'''
        Favorite_Button = ("xpath",".//*[@id='inner-container']/div[2]/ng-switch/div/div/div/div[1]/div/div/div/button[1]")
        Report_Name = ("xpath",".//*[@id='Aboard']/body/div[1]/div/div/div[2]/form/div[1]/input")
        text = "my report"
        OK_Button = ("xpath",".//*[@id='Aboard']/body/div[1]/div/div/div[3]/button[2]")
        Favorite_Icon = ("xpath",".//*[@id='Aboard']/body/div[1]/div/div/div[1]/header/div[3]/div[1]/i")
        Report_Title = ("xpath",".//*[text()='my report']")
        self.P. Favorite(Favorite_Button,Report_Name,text,OK_Button,Favorite_Icon,Report_Title)
        locator_Result = ("css selector",".box-title.container__title.ng-binding.ng-scope")
        result = self.P.Result(locator_Result)
        print(result)
        self.assertEqual("my report",result)

    def test_04(self):
        u'''测试弹出报表'''
        Pop = ("xpath",".//*[@id='inner-container']/div[2]/ng-switch/div/div/div/div[1]/div/div/div/button[2]")
        self.P.Pop_Out(Pop)  # 弹出报表并获取句柄
        self.assertEqual(2,len(Pop))

if __name__ == "__main__":
    unittest.main()
