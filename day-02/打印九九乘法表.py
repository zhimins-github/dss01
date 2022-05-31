#打印九九乘法表
# 1*1
# 1*2=2 2*2

i = 1
while i <= 9:
    n =1

    while n <= i:
        print("%d * %d = %-2d" % (i, n, i * n), end = " ")
        n += 1

    print()
    i += 1

print()





# print("%3d" % (n), end="")
