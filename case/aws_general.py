# coding:utf-8

import unittest

from page.aws_login_open_detail import *


class General_test(unittest.TestCase):
    '''不分报表总体测试'''

    @classmethod
    def setUpClass(cls):
        '''登录'''
        cls.driver = webdriver.Firefox()
        detail = Login_Open_Detail(cls.driver)
        detail.login_url()

    @classmethod
    def tearDownClass(cls):
         cls.driver.quit()

    def setUp(self):
        '''打开明细表'''
        self.P = Repeat_Process(self.driver)
        self.Base = BasePage(self.driver)

    def test_01(self):
        u'''测试删除收藏报表'''
        Favorite_Icon2 = ("xpath",".//*[@id='Aboard']/body/div[1]/div/div/div[1]/header/div[3]/div[1]/i")
        Report_Checkbox = ("css selector",".jstree-icon.jstree-checkbox")
        Delete_Btn = ("css selector",".btn.btn-danger.fav-bth.delete")
        OK_Cancel_Btn = ("css selector",".btn.btn-danger.ok-btn.ng-binding")
        self.P.delete_favorite(Favorite_Icon2,Report_Checkbox,Delete_Btn,OK_Cancel_Btn)
        time.sleep(3)
        Rpt_N_Y = ("css selector",".jstree-icon.jstree-checkbox")
        elements = self.Base.find_elements(Rpt_N_Y)
        self.assertEqual(1,len(elements))

if __name__ == "__main__":
    unittest.main()

