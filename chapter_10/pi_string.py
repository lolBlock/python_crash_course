# coding = uft-8

filename = r'files\pi_digits.txt'  # linux和mac中用斜杠(/)，win中用反斜杠(\)且应尽量以原始字符串的方式指定路径，即在单引号前加r
with open(filename) as file_object:
    lines = file_object.readlines()  # 读取每一行，并将其存储在列表lines，它可在with外使用

pi_string = ''
for line in lines:
    pi_string += line.strip()  # 删除行首末的换行符后加入pi_string

print(pi_string)
print(len(pi_string))

print(pi_string[:6] + "...")  # da打印小数点后4位
