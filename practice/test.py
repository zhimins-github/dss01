#
#
# # 1. 终端登录
# def load(user, password):
#     pass
# # 2. 验证信息
#     # 2.1 用户 密码
#     # 2.2 账号 部门
# def vertify_user_and_pd(user, password):
#     pass
#
# def vertify_account_and_partment(account, partment):
#     pass
# # 3.

class Load():
    user_rea = "admin"
    pd_rad = "123456"
    acount_rea = "dssa_ccount"
    partment_rea = "dss_part"

    user = ""
    pd = ""

    account = ""
    partment = ""

    load_success = False

    def __init__(self, user, pd, acuount, partment, **kwargs):
        self.user = user
        self.pd = pd
        self.account = acuount
        self.partment = partment

    def vertify_user_and_pd(self):
        if self.user == self.user_rea:
            print("登录用户正确")
            print(self.user, "******")  # 若输入的用户名正确，返回登录用户的信息，password字段不显示
            if self.pd == self.pd_rad:
                print("密码登录正确")
                self.load_success = True
            else:
                self.load_success = False
                print("密码错误")
        else:
            self.load_success = False
            print("无查询结果的提示") # 若输入的用户名不正确，给出无查询结果的提示
        pass

    def vertify_account_and_partment(self):
        if self.load_success == True:
            if self.account == self.acount_rea:
                print("账户信息登录正确")
                if self.partment == self.partment_rea:
                    print("部门信息登录正确")
                    pass
                else:
                    print("部门信息登录失败")
                    pass
            else:
                print("账户信息登录失败")
        else:
            pass


user = input("user:")
pd = input("pd:")
account = input("account:")
partment = input("partment:")

load = Load(user, pd, account, partment)

load.vertify_user_and_pd()

load.vertify_account_and_partment()
