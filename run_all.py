# coding: utf-8
import unittest
from common import HTMLTestRunner_cn
import time


# 用例地址
tc_dir = "D:\\test\\case"
# 测试套件收集用例
# discover方法加载多个用例集合
discover = unittest.defaultTestLoader.discover(start_dir=tc_dir,
                                               pattern="aws*.py",
                                               top_level_dir=None)

print(discover)

if __name__ == "__main__":
    # 生成报告的路径及时间
    report_path = "D:\\thiscomputer\\workspace\\aws_test\\report\\"+"result.html"
    # 打开报告并写入测试结果
    fp = open(report_path,"wb")
    runner = HTMLTestRunner_cn.HTMLTestRunner(stream=fp,
                                              title=u"大数据平台AWS测试报告",
                                              description=u"用例执行结果")

    # 运行测试用例
    runner.run(discover)
    # 关闭报告文件
    fp.close()


