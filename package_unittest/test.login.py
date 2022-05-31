from practice.iiter3_add_user import login
from loguru import logger
#1.测试登录的测试用例
# C:\Users\zhimins\PycharmProjects\dss01\practice\user_date.txt
#case1 输入正确的用户名和正确的密码进行登录


#case2 输入错误的密码或者密码登录


#case3 输入空的用户或密码登录

# 2.进行测试，使用断言assert

login_result = login("admin", "123456")
logger.debug("登录返回数据：{}".format(login_result))

assert 0 == login_result.get("code")
assert 1 == login_result.get("code")