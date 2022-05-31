def show_info(*args):
    print(args)
show_info()
show_info("python")


# 可变化参数—字典形式得到参数
def show_info(**AV):
    print(AV)

dt_date = {"x" : 1, "y" : 2}
print(show_info(a ="hello", b ="world", c="123"))
print(show_info(a ="hello", b ="world"))
print(show_info(**dt_date))
#

