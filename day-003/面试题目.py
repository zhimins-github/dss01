# 从键盘输入一个字符串，判断其中 英文字母字符的个数，数字字符的个数，空格的个数以及其它类型字符的个数。

# # for i in range(1, 10):   #  1 - 9
# 	    for j in range(1, i+1):
# 	        print("%d*%d=%-2d" % (j, i, i*j), end="\t")
# 	    print()    # 换行

# s = input("情输入一个字符串")
s1 = "1112378785895667"
x = 0
c = 0

for i in s1:
    # print(i)
    if int(i) == 1:
        x += 1
    elif int(i) == 2:
        c += 1
print(x)
print(c)

"""
1. for
2. in
3. if elif
4. ==
5. int()
"""

"""
1. for
2. 
"""

# print(s1.count("1"))
# print(s1.count("2"))
# print(s1.count("3"))
# print(s1.count("4"))
# print(s1.count("5"))




