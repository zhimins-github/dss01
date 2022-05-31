# def add(x, y):
#     z = x + y
#     print(z)
#     return z
# def div(x, y):
#     return x + 10, y
# print(div(12 , 1))
def student_lesson(grade, subject):
    z = "{}年级上{}课".format(grade, subject)
    return z


print(student_lesson(grade=2, subject="语文"))
print(student_lesson(subject='语文', grade=5))
print(student_lesson(6, subject='体育'))

def n_subject(name, subjects = "历史" ):
    x = "{},选修{}课".format(name, subjects)
    return x
print(n_subject("丁双双", "数学"))
print(n_subject("邵志敏", "化学"))
print(n_subject("大欣"))

def study_language(name,language='python'):
    info = ("{}要学习{}语言".format(name,language))
    return info
print(study_language("张三","java"))
print(study_language("李四","java"))
print(study_language("王二"))
#需求：要求可以输入任何个数相加
def add(x, y, *args):
    z = x + y + sum(args)
    return z
print(add(3, 4, 5, 6, 7, 8, 9))
print(add(3, 4, *[5, 6, 7, 8, 9]))






