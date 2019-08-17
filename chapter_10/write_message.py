# coding = utf-8
# open()的参数可以是'r'(默认),'w','r+','a'(附加模式)
# 如果写入的文件不存在，open()会自动创建
# 'w'模式下，原文件若存在会先被清空

filename = r'files\programming.txt'
with open(filename, 'w') as file_object:
    file_object.write("I love programming.\n")  # 写入了一行
    file_object.write("I love apple.")  # 又写入了一行

with open(filename, 'w') as file_object:  # 清空了前面的内容
    file_object.write("I love banana.\n")
