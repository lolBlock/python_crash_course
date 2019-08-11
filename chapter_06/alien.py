# coding = utf-8

# 字典类似于列表，但让你能够将不同信息关联起来
# 字典是一系列“键-值”对，用{}表示，可将任何Python对象用作字典中的值

alien_0 = {'point': 5}  # 也可以创建空字典
alien_0['color'] = 'green'  # 添加
print(alien_0)
print("You just earned " + str(alien_0['point']) + " points!")  # 通过键访问值

alien_0['point'] = 10  # 通过键修改值

del alien_0['color']  # 删除键-值对

user_0 = {
    'green': '绿色',
    'yellow': '黄色',
    'red': '红色',  # 最后可以有逗号
    # 'green': '重复测试' 会覆盖前面的键-值对，这个注释不能顶格，否则破坏了该字典
    }
print(user_0)

# 获取字典的元素时，获取顺序是不可预测的
# ①遍历键-值对
for key, value in user_0.items():  # 返回一个键-值对列表
    print("key is " + key)
    print("value is " + value)

# ②遍历所有键
for k in user_0.keys():  # 返回一个键列表
    print(k)

for k in user_0:  # 默认就是遍历所有键
    print(k)

for k in sorted(user_0.keys()):  # 把返回的键列表,用sorted排序后再存到k
    print(k)

# ③遍历所有值
for v in user_0.values():  # 返回一个值列表，包含重复
    print(v)

for v in set(user_0.values()):  # 返回一个值列表，用set去除重复
    print(v)

# 嵌套
# ①用字典构成的列表
alien_1 = {'color': 'green', 'points': 5}
alien_2 = {'color': 'red', 'points': 15}
alien_3 = {'color': 'yellow', 'points': 10}
aliens = [alien_1, alien_2, alien_3]
print(aliens)

# ②字典中存储列表
favorite_language = {
    'wgq': 'C',
    'cc': ['C', 'PHP'],
    'hxf': ['Python'],
    }
print(favorite_language)

# ③字典中存储字典
# 每位用户的字典结构应该都相同，虽然Python没有这样的要求，但是结构相同会使得嵌套的字典处理起来更容易
user_1 = {
    'name': 'wgq',
    'age': '26'
}

user_2 = {
    'name': 'cc',
    'age': '27'
    }

# users = {user_1, user_2} 错误，应使用①，字典的格式应该是键-值对
users = {
    'child_1': {
        'name': 'wgq',
        'age': '26'
    },

    'child_2': {
        'name': 'cc',
        'age': '27'
    }
}

print(users)
