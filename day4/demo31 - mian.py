#main 属性： __manin __  运行入口
def div1(x, y):
    try:
        z = x / y
        return z
    except Exception as e:
        print("除法不能出现被零除的情况")
if __name__ == "__main__":
    print(div1(1, 2))
