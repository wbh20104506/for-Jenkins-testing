# coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.base import *
import time

class Repeat_Process():
    u'''封装前端UI中的重复步骤'''

    def __init__(self,driver):
        self.driver = driver
        self.Base = BasePage(self.driver)

    def open_link(self,url):
        u'''打开链接'''
        self.Base.open(url)

    def login(self, locator1, username, locator2, psw, locator3):
        u'''封装登录步骤'''
        self.Base.send_keys(locator1, username, is_clear=True)
        self.Base.send_keys(locator2, psw, is_clear=True)
        self.Base.click(locator3)

    def result(self,locator):
        u'''获取元素文本结果'''
        try:
            result = self.Base.get_text(locator)
            return result
        except:
            print("失败，返回空字符")
            return ""

    def search_report(self, locator1, text, locator2):
        u'''封装搜索报表步骤'''
        self.Base.send_keys(locator1, text, is_clear=True)
        self.Base.click(locator2)

    def add_quick_filter(self, locator_Add_Filter, locator_Quick, locator_Input_Text,text,Operation_List,Operation, locator_Apply_Filter):
        u'''封装添加Quick Filter步骤'''
        self.Base.click(locator_Add_Filter)
        self.Base.click(locator_Quick)
        self.Base.send_keys(locator_Input_Text, text, is_clear=True)
        self.Base.click(Operation_List)
        self.Base.move_to_element(Operation)
        self.Base.click(locator_Apply_Filter)

    def add_basic_filter(self,locator_Add_Filter,locator_Basic,locator_Add_Button,locator_Field_List,locator_Field,
                         locator_Operation_List,locator_Operation,locator_Field_Text,text,locator_Apply_Filter):
        u'''封装添加Basic Filter步骤'''
        self.Base.click(locator_Add_Filter)
        self.Base.click(locator_Basic)
        self.Base.click(locator_Add_Button)
        self.Base.click(locator_Field_List)
        self.Base.move_to_element(locator_Field)
        self.Base.click(locator_Operation_List)
        self.Base.move_to_element(locator_Operation)
        self.Base.send_keys(locator_Field_Text,text,is_clear=True)
        self.Base.click(locator_Apply_Filter)

    def favorite(self,Favorite_Button,Report_Name,text,OK_Cancel_Button,Favorite_Icon,Report_Title):
        u'''封装收藏报表步骤'''
        self.Base.click(Favorite_Button)
        self.Base.send_keys(Report_Name,text,is_clear=True)
        self.Base.click(OK_Cancel_Button)
        self.Base.click(Favorite_Icon)
        self.Base.click(Report_Title)

    def delete_favorite(self,Favorite_Icon,Report_Checkbox,Delete_Btn,OK_Cancel_Btn):
        u'''封装删除收藏报表'''
        self.Base.click(Favorite_Icon)
        checkboxes = self.Base.find_elements(Report_Checkbox)
        checkboxes[1].click()
        self.Base.click(Delete_Btn)
        self.Base.click(OK_Cancel_Btn)

    def pop_out(self,Pop):
        u'''封装弹出报表并获取句柄'''
        self.Base.click(Pop)
        handles = self.Base.get_handles()
        print(handles)

    def exp_rpt(self,Expt_Icon,Rpt_Title,text,File_Type,Rpt_Type,Expt_Cancel_Btn):
        u'''封装导出报表'''
        self.Base.click(Expt_Icon)
        self.Base.send_keys(Rpt_Title,text,is_clear=True)
        self.Base.click(File_Type)
        self.Base.click(Rpt_Type)
        self.Base.click(Expt_Cancel_Btn)

if __name__ == "__main__":
    driver = webdriver.Firefox()
    P = Repeat_Process(driver)
    Base = BasePage(driver)
    url = "https://demo.jintelhealth.com/Analytics/#!/login"
    P.open_link(url) #  打开链接
    locator1 = ("id", "username")
    username = "lz_admin"
    locator2 = ("id", "password")
    psw = "Ghc2018!"
    locator3 = ("id", "loginBtn")
    P.login(locator1, username, locator2, psw, locator3)  # 输入用户名密码登录
    locator = ("css selector", ".box-title.container__title.ng-binding")
    print(P.result(locator))  # 获取登录结果
    locator1 = ("id", "topInput")
    text = "Detail0808"
    locator2 = ("id", "myI")
    P.search_report(locator1, text, locator2)  # 搜索并打开报表
    time.sleep(3)
    Expt_Icon = ("xpath",".//*[@id='inner-container']/div[2]/ng-switch/div/div/div/div[1]/div/div/div/button[3]")
    Rpt_Title =("xpath",".//*[@id='Aboard']/body/div[1]/div/div/div/div[2]/div[1]/input")
    text = ("my export")
    File_Type = ("xpath",".//*[@id='Aboard']/body/div[1]/div/div/div/div[2]/div[2]/div/div/div[1]")
    Rpt_Type = ("xpath",".//*[@id='Aboard']/body/div[1]/div/div/div/div[2]/div[2]/div/div/div[2]/div/div/div[2]/div")
    Expt_Cancel_Btn = ("xpath",".//*[@id='Aboard']/body/div[1]/div/div/div/div[3]/button[2]")
    P.exp_rpt(Expt_Icon,Rpt_Title,text,File_Type,Rpt_Type,Expt_Cancel_Btn)






