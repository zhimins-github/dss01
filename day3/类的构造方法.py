#创建学生类，要求有属性，姓名和年级，学习的方法，打印学生的上课情况
class Students():
    name = ""
    grade = ""

    def study(self):
        # print("这里的self是：", self)
        print("{}年级的学生{}正在学习".format(self.grade, self.name))

# s = Students()
# s.grade = "三"
# s.name = "张三"
# s.study()

