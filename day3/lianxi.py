#实例变量
# class Students(object):
#     def __init__(self, name, grade):
#
#         self.name = name
#         self.grade = grade
# s =Students("张三", 5)
# print(s.name)
# print(s.grade)

class Students():
    name = "张三"
    __score = "76"

    def set_score(self, score):
        self.__score = score

    def get_score(self):
        return self.__score

print(Students.name)
s = Students()
s.get_score()