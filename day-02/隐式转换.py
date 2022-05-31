# 隐式转换
# int 类型和 bool类型
# int类型与float类型进行计算时。会自动将int转换为float，进行运算，结果为float
# num1 = 100
# num2 = 3.14
# num3 = num1 + num2
# print(num3, type(num3))
# 显示转换
s1 = "1011"
num1 = int(s1)
print(num1, type(num1))

s3 = "3.14"
num3 = float(s3)
print(num3, type(num3))

# 转换成bool类型为false的值
# 0， 0.0， “”， （）， [], {}, set(), none
