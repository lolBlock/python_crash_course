# coding = utf-8
import json


def get_stored_username(username):
    filename = r'files\username.json'
    try:
        with open(filename) as f_obj:
            users_name = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        if username in users_name:
            return username
        else:
            return None


def story_new_username(username):
    filename = r'files\username.json'
    try:
        with open(filename) as f_obj:
            names = json.load(f_obj)
    except FileNotFoundError:
        with open(filename, 'w') as f_obj:
            first_user = [username]
            json.dump(first_user, f_obj)
    else:
        with open(filename, 'w') as f_obj:  # 这样效率感觉不行啊，每次都会整取整存，怎么追加呢？利用长度？切片？
            names.append(username)
            json.dump(names, f_obj)


def greet_user():
    """用户欢迎界面"""
    cur_user = input("请输入你的名字： ")
    username = get_stored_username(cur_user)
    if username:
        print("Welcome back, " + username + "!")
    else:
        story_new_username(cur_user)
        print("注册成功！")


greet_user()
