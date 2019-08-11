# coding = utf-8

# input() 将用户输入解读为字符串
message = input("Tell me something, and I will repeat it back to you: ")  # \n 不会换行，但input()会自动换行，应该是隐藏了\n
print(message)

# int() 用来获取数值输入
age = int(input("How old are you? "))  # 将字符串转换为数值
print(age)

# while()
current_number = 1
message = 'start'
active = True
while current_number <= 10 and message != 'quit' and active:
    current_number += 1  # 使用次数控制退出循环
    message = input("Tell me something: ")  # 用户输入 quit 退出循环
    if message == 'False':  # == 误写成 = 会直接报错
        active = False  # 使用布尔标志退出循环
    elif message == 'continue':
        continue
    elif message == 'break':
        break  # 使用 break 退出循环
    else:
        print("current_number is " + str(current_number) + message)

# 列表间移动元素
users_1 = ['wgq', 'cc', 'hxf']
users_2 = []

while users_1:
    users_2.append(users_1.pop())

print(users_1)  # 列表的打印会自动换行
print(users_2)

while 'cc' in users_2:
    users_2.remove('cc')

print(users_2)

# 使用用户输入来创建字典
person_all = {}
person_current = {}

while 1:
    name = input("What's your name: ")
    gender = input("What is your gender? ")
    age = int(input("How old are you: "))

    person_current['gender'] = gender  # []里不能用 gender
    person_current['age'] = age
    person_all[name] = person_current  # []里不能用 'name'

    if input("Do you want to continue? (y/n) ") == 'n':
        break

print(person_all)
