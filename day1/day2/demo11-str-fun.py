astr = "+"
bstr = astr.join("world")
print(bstr)

cstr = "helloworldpythonjavaphp"
dstr = cstr.split("o")
print(dstr)

estr = "helloworld"
print(estr.find("l"))
print(estr.find("x"))
print(estr.index("l"))

fstr = "测试版报告.doc"
if fstr.endswith(".doc"):
    print("他是一个word文档")

# hstr = "hello", "world"
# print(hstr.replace(hello, "你好"))
# a = input("请输入一行字符")
#输入一行字符，分别统计出其中英文字母，空格，数字和其他字符的个数
x = input("请输入一行字符串")
zf = 0
kg = 0
sz = 0
other = 0
for y in x:
    if y.isalpha():
        zf += 1
    elif y.isdigit():
        sz += 1
    elif y.isspace():
        kg += 1
    else:
        other += 1
print("字符：", zf)
print("数字：", sz)
print("空格：", kg)
print("其他：", other)


