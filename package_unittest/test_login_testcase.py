from practice.iiter3_add_user import login
from loguru import logger
import unittest
import sys
class TestLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print("开始运行方法：", sys._getframe().f_code.co_name)
    @classmethod
    def tearDownClass(cls) -> None:
        print("开始运行方法：", sys._getframe().f_code.co_name)
    def setUp(self) -> None:
        print("开始运行方法：", sys._getframe().f_code.co_name)
    def tearDown(self) -> None:
        print("开始运行方法：", sys._getframe().f_code.co_name)

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
    unittest.main()



#1.测试登录的测试用例

#case1 输入正确的用户名和正确的密码进行登录


#case2 输入错误的密码或者密码登录


#case3 输入空的用户或密码登录

