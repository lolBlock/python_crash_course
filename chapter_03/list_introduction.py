# coding = utf-8

# 列表的下表从0开始
# 查
names = ['吴光强', '程超', '胡雪锋']
print(names)
print(names[0] + '是咸鱼')
print(names[1] + "是苦比")
print(names[2] + "是逗比")

# 改
names[1] = 'CC'

# 增
names.append('叶颂基')    # 添加到列表末尾
names.insert(3, '周敬')  # 添加到指定下标

# 删
del names[0]  # 删除指定下标对应的元素，无返回值
print(names.pop() + "被删除了")  # 删除末尾，并返回
print(names.pop(1) + "也被删除了")  # 删除指定下标对应的元素，并返回
names.remove('CC')  # 删除第一个指定的值，无返回值
print(names)

names = ['Wu Guangqiang', 'ChengChao', 'Hu xuefeng']

# 列表的临时排序，并输出
print(sorted(names))

# 列表的永久排序，不输出
names.sort()  # 默认正序
print(names)
names.sort(reverse=True)  # 逆序
print(names)
names.reverse()  # 反转
print(names)

# 列表名是“指针”？
names_319 = names
names.append('Ye Songji')  # names 也被改了
print(names)

# 返回表长
print("5-319有" + str(len(names)) + "个机智boy")
