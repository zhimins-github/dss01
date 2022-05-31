# # 1. 输入a,b,c,d4个整数，计算a+b-c*d的结果
a = input('请输入一个整数')
b = input('请输入一个整数')
c = input('请输入一个整数')
d = input('请输入一个整数')
print(int(a) + int(b) -int(c) * int(d))
# # 打印1~100内被3整除的所有数的和 。
y = 1
sum_value = 0
while y <= 100:
    if y % 3 == 0:
        sum_value += y
    y += 1
print(sum_value)

sum = 0
for x in range(1, 101):
    if x % 3 == 0:
        sum += x
print(sum)
# #使用range()输出1~10内的所有奇数
for x in range(1, 11, 1):
    if x % 2 != 0:
        print(x)

# #打印1~100所有偶数的和 减去 所有奇数的和的值
sum1 = 0
sum2 = 0
for x in range(1, 101):
    if x % 2 == 0:
        sum1 += x
    else:
        sum2 += x
print(sum1-sum2)

#求1+2+3+...+100的和
a = 1
b = 0
while a <= 100:
    b += a
    a += 1
print(b)
# # 判断一个数n能同时被3和5整除
n = 3
if n % 3 == 0 and n % 5 == 0:
    print(n)
else:
    print("不通过")

# #定义一个整数变量，判断该变量值是否是1-100内的某个数，如果是打印出来
for x in range(1, 101, 1):
    print(x)
#  #输入三个整数x,y,z，请把这三个数由小到大输出。备注：输入方法：input()
#利用条件运算符的嵌套来完成此题：学习成绩>=90分的同学用A表示，60-89分之间的用B表示，
x = 98
if x >= 90 :
    print(A)
elif x > 60 and x < 89:
    print(B)



