# 读取文件

# 打开文件
f = open('a.txt', 'r')


#读取文件
result = f.read()

print(result)


#关闭文件
f.close()