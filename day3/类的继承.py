class People():


    def eat(self, people_type):
        print(people_type, "在吃饭")

class Students(People):
    pass

class Teacher(People):
    pass


s = Students()
s.eat("学生")

t = Teacher()
t.eat("老师")
