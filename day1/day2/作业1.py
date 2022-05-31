#  #输入三个整数x,y,z，请把这三个数由小到大输出。备注：输入方法：input()
lst = []
x = input('请输入一个整数：')
y = input('请输入一个整数：')
z = input('请输入一个整数：')
lst.append(int(x))
lst.append(int(y))
lst.append(int(z))
print(lst)
lst.sort()
print(lst)
#利用条件运算符的嵌套来完成此题：学习成绩>=90分的同学用A表示，60-89分之间的用B表示，
score = int(input("请输入你的分数："))
if score >= 90:
    print("A")
elif score >= 60:
    print("B")
else:
    print("c")




