my_str = "张三今年%d" % (25)
print(my_str)
my_str1 = "my name is %s" % ("list")
print(my_str1)
my_str2 = "一斤苹果%f元" % (5)
print(my_str2)

my_str4 = "一斤苹果%12.2f元" % (3.23)
print(my_str4)
my_str5 = "一斤苹果%-12.2f元" % (3.23)
print(my_str5)
my_str6 = "一斤苹果%+-12.2f元" % (3.23)
print(my_str6)

my_str8 = "张三今年{}岁".format(25)
print(my_str8)

my_str9 = "今天星期{}, 张三买了{}斤苹果".format("一", "5")
print(my_str9)

