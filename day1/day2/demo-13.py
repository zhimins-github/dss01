from typing import List, Union

a_str = "今天星期{},丁双双买了{}斤苹果，{}斤猕猴桃"
print(a_str.format("一", 3, 6))
a_str1 = "今天丁双买了{1}件衣服和{0}双鞋子"
print(a_str1.format("1", "2"))
a_str2 = "今天想买{x}斤苹果"
print(a_str2.format(x=5))

a_lst = [1, 2, 3, 4, 5, 6]
a_lst.append("hello")
print(a_lst)
print(a_lst.count(1))
b_lst =["orange", "gold", "black"]
# print(b_lst.index("black"))
# b_lst.insert(1, "green")
# print(b_lst)




