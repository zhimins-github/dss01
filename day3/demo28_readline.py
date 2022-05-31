# 写文件


#1.打开文件
f = open('a.txt', "r")


#2.按行读取

while True:
    line = f.readline()
    print(line, end="")
    if not line:
        break
#3. 关闭文件
f.close()