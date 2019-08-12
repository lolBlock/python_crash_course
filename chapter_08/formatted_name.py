# coding = uft-8


def get_full_name(first_name, last_name):  # 默认参数可以让实参变成可选，eg. middle_name='' 函数体里加if middle_name:
    """返回全名"""
    full_name = first_name + ' ' + last_name
    return full_name.title()  # 可以返回简单值、字典


musician = get_full_name('guangqiang', 'wu')
print(musician)


def greet_users(names):  # names[:] 则表示传副本
    """向列表中的每位用户都发出简单的问候"""
    for name in names:
        print("Hello, " + name.title() + "!")


user_names = ['Hannah', 'Tom', 'jack']
greet_users(user_names)  # 列表的传递默认传本身
greet_users(user_names[:])  # 可以通过加[:]来传副本
