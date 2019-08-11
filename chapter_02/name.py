# coding = utf-8

string1 = "1.双引号里面可以包含半角单引号' 或者 ''"
string2 = '2.单引号里面可以包含半角双引号" 或者 ""'
string3 = "my Name IS yesongji"

print(string3.title())  # 每个单词的首字母大写
print(string3.upper())  # 全大写
print(string3.lower())  # 全小写

# 合并(拼接)字符串
first_name = "songji"
last_name = "ye"
full_name = first_name + " " + last_name
print("Hello, " + full_name.title() + "!")

message = "Hello, " + full_name.title() + "!"
print(message)

# 转义字符：制表符和换行
print("\t" + message)
print("\t" + message + "\n")
print("Language:\n\tPython\n\tC")

# 删除空白
favorite_language = "  C plus plus  "
print(favorite_language.lstrip())  # 删除左边的空格
print(favorite_language.rstrip())  # 删除右边的空格
print(favorite_language.strip())   # 删除两边的空格
print(favorite_language)           # 不变
favorite_language = favorite_language.strip()  # 赋值
print(favorite_language)           # 改变

# 动手试一试 2-5
print('Lu Xun once said, "表情包多的人，没有男/女朋友"')

famous_person = " Lu Xun "
saying = famous_person.strip() + ' once said, ' + '"表情包多的人，没有男/女朋友"'
print(saying)
