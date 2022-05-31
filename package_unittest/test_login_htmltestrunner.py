#测试报告
#试用htmlrunner模块生成测试报告
from practice.iiter3_add_user import login
from loguru import logger
import unittest
import sys
from package_unittest.HTMLTestRunner import  HTMLTestRunner
class TestLogin(unittest.TestCase):

    def test_login_success(self):
        print("开始运行方法：", sys._getframe().f_code.co_name)
        except_value = 0
        actual_value = login("admin", "123456").get("code")
        self.assertEqual(except_value, actual_value)

    def test_user_wrong(self):
        print("开始运行方法：", sys._getframe().f_code.co_name)
        except_value = 1
        actual_value = login("bca", "123456").get("code")
        self.assertEqual(except_value, actual_value)
    def test_password_is_null(self):
        print("开始运行方法：", sys._getframe().f_code.co_name)
        except_value = 1
        actual_value = login("admin", "").get("code")
        self.assertEqual(except_value, actual_value)
if __name__ == '__main__':
    suite_a = unittest.TestSuite()
    suite_a.addTest(TestLogin("test_login_success"))
    suite_a.addTest(TestLogin("test_user_wrong"))
    suite_a.addTest(TestLogin("test_password_is_null"))

    print(suite_a)
    test_report = '.test_report.html'
    with open (test_report, "wb") as f:
        runner = HTMLTestRunner(f, title="测试报告", description="测试描述")
        runner.run(suite_a)

