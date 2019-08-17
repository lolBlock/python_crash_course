# coding = uft-8

filename = r'files\pi_digits.txt'  # linux和mac中用斜杠(/)，win中用反斜杠(\)且应尽量以原始字符串的方式指定路径，即在单引号前加r
with open(filename) as file_object:
    contents = file_object.read()
    print(contents)  # 打印文件内容
    print(contents.rstrip())  # 打印文件内容，并删除字符串末尾的空白

with open(filename) as file_object:
    for line in file_object:  # 遍历文件的每一行，包含空行，行末包含换行符(\n)
        print(line)

    # open() 打开的文件是一个可迭代对象,第一次循环后，迭代结束了，文件指针指到文件句柄的尾部
    for line in file_object:  # 这两行为什么不起效
        print(line.rstrip())  # 打印时删除字符串(此时的字符串是读进来的行)末尾的空白

    # 可以通过seek设置文件指针
    file_object.seek(0)  # 指向文件头部
    for line in file_object:
        print(line.rstrip())  # 打印时删除字符串(此时的字符串是读进来的行)末尾的空白


with open(filename) as file_object:
    lines = file_object.readlines()  # 读取每一行，并将其存储在列表lines，它可在with外使用

for line in lines:  #
    print(line.rstrip())
