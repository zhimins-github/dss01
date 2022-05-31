lst = ["red", "hello", 2, 3.5]
print(lst[1])
print(lst[-1])

tp = ("red", "hello", 2, 3.5)
print(tp[1])
print(tp[-1])

my_str = "redhello"
print(my_str[1])
print(my_str[-8])

lst5 = ["red", "green", "blue", "black", "gold", "orange"]
print(lst5[1:5:1])
print(lst5[1:6:2])
print(lst5[1::1])
print(lst5[1:2:])
print(lst5[::2])
print(lst5[2:])
print(lst5[:3:])
print(lst5[2::])

alst = [1, 2]
blst = [3, 4]
clst = alst + blst
print(clst)
dlst = alst * 8
print(dlst)

lst6 = ["red", "green", "blue", "black", "gold", "orange"]
print("gold" in lst6)
print("hello" in lst6)
print(len(lst6))
lst7 = [1, 2, 3, 4, 5, 67, 98]
print(max(lst7))

klst = list()
print(klst)
cstr = "asd"
mlst = list(cstr)
print(mlst)


lst8 = ["red", "green", "blue", "black", "gold", "orange"]
for index, vls in enumerate (lst8):
    print(index, vls)












