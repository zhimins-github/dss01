#将一个列表的数据复制到另一个列表中
alst = [2, 34, 675, 22]
blst = ["1", "ss", "dd"]
clst = [2, 34, 675, 22]
alst.extend(blst)
print(alst)

#打印九九乘法表
for x in range(1, 10):
    for y in range(1, x+1):
        print(y, " * ", x, " = ", y * x, end="")
    print()

