# coding = utf-8

# 列表[]
names = ['Wu Guangqiang', 'Cheng Chao', 'Hu Xuefeng']
for who in names:  # 这里有一个冒号
    print(who)
    print(who + " in 5-319")

print("for的范围在相同的缩进里，本句在for之外")
print(who)  # for之外的who的生命周期仍未结束，但这不是一个不好的用法

# range(start_int_with, stop_int_without, step) 左闭右开
print(range(1, 2, 10))  # 打印的是：range(1, 2, 10)

for value in range(1, 10, 2):
    print(value)  # 打印列表会有换行的效果

# list()将range()的结果直接转换为列表
numbers = list(range(1, 11))
print(numbers)

# 列表元素求平方方法1
squares = []
for value in numbers:  # 等效于 for value in range(1, 11)
    squares.append(value ** 2)

print(squares)

# 列表元素求平方方法2：列表解析
squares_quick = [value ** 2 for value in range(1, 11)]  # 列表名、表达式、提供值的for循环(不需要冒号)
print(squares_quick)

# 简单的统计功能
print(min(numbers))
print(max(numbers))
print(sum(numbers))

# 使用[]取列表的一部分，即切片。左开右闭
print(numbers[2:5])
print(numbers[2:])
print(numbers[:5])
print(numbers[-3:])
print(numbers[:])  # 全打印
print(numbers[2:50])  # 可以超出索引，但只打印存在的元素
print(numbers[-3:0])  # 不会输出8、9、10、0，而是输出空 []
# print(names[]) 语法错误

# 遍历切片
for value in numbers[-3:]:
    print(value)

# 列表的复制
numbers_cpoy_all = numbers[:]
print(numbers_cpoy_all)
numbers_copy_part = numbers[2:5]
print(numbers_copy_part)
numbers_copy_same = numbers  # 他们是同一个列表，修改是会彼此影响

# 元组() 不可变的列表成为元组
dimensions = (200, 500)
for dimension in dimensions:
    print(dimension)  # 打印元组会有换行的效果

# dimensions[0] = 2  报错，不能修改元组元素的值
dimensions = (1, 2, 3)  # 可以重新定义
for dimension in dimensions:
    print(dimension)
