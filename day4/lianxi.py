# 错误和异常
def div(x, y):
    z = x / y
    return z
print(div(3, 4))
print(div(3, o))
#使用try ....except语句
def div1(x, y):
    try:
        z = x / y
        return z
    except Exception as e:
        print("除法不能出现被零除的情况")

print(div1(3, 4))
print(div1(3, 0))


