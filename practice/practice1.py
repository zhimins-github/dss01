# 需求-迭代1：登录功能
# 1.定义两条用户数据 ，要求用户数据的属性包括用户角色，用户账号，密码，部门
# 2.要求返回的格式是字典形式 ，包含两个字段，code和message ,code为0代表成功，为1代表失败 ；message给出相应的提示 ，格式如 ：{'code':0,'message':'登录成功'}
# 3.用户通过控制台输入用户名和密码，判断用户名和密码是否和定义数据中的用户名密码相匹配，若匹配返回成功登录消息体，并把用户列表也追加到返回结果中,{'code':0,'message':'登录成功',user_list:[]}
# 4.若用户名输入为空或密码输入为空，都给出对应的提示，如用户名不能为空
# 5.若用户名或密码不匹配，都给出登录失败，请检查您的用户名或密码是否填写正确。提示
user = input("用户：")
pd = input("密码：")


class Landing():
    user = ""
    pd = ""
# user_dct = {'role': 'admin', 'account': 'admin', 'password': '123456', 'dept': 'tester'}
user_dct = {'role': 'admin', 'password': '123456'}
code = 0
message = "登录成功"
# 用户通过控制台输入用户名和密码，判断用户名和密码是否和定义数据中的用户名密码相匹配
for value in user_dct.values():
    if user == 'admin'and pd == '123456':
        print("成功登录")
    else:
        print("登录失败，请检查您的用户名或密码是否填写正确！")
        break
# else:
#     print("登录失败，请检查您的用户名或密码是否填写正确！")


    # elif values != ""


# if user == user_dct["role"]:
#     if pd == user_dct["password"]:
#         print("登录成功")
#         print(message)
#         print(user_dct)
#     else:
#         print("登录失败，请检查您的用户名或密码是否填写正确！")
# else:
#     print("登录失败，请检查您的用户名或密码是否填写正确！")

# for x, y in user_dct.items():
#     if user_dct.fromkeys("code", "message"):
#         pass
# print([code, message])
# print({code: message})
