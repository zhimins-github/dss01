

"""
1.顺序执行： 从上往下
2.条件执行： if else
3.循环执行： break, while条件不成立
"""
# i = 12
# j = 2
#
# while i >= 0:
#     while j < i:  # i=11 j=4
#         if i % j == 0:
#             i += 1
#             break
#         else:
#             j += 1
#         j += 1
#     i -= 2
#     print(i)
#
# print("end")


i = 1
while i <= 10:
    j = 2
    while j < i:  # i=7 j=3
        if i % j == 0:
            break
        j += 1
        print(i)
    i += 1

print("end")



