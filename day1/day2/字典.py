det1 = {}
det2 = {"字典1": 1, "字典2": 2, "字典3": 3}
print(det2)
print("获取字典det2中键名为1的值：", det2["字典1"])
print("获取字典det2中键名为1的值：", det2.get("字典4"))
det2['字典3'] = 4
print(det2)
det3 = {'e': 22, 'f': 'hello'}
det2.update(det3)
print('更新后的字典：', det2)




