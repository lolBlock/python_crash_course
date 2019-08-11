# coding = utf-8

age_0 = 1993
age_1 = 1992
age_2 = 1991
age_3 = 1991
ages = [1991, 1992, 1993]
names = ['wgq', 'cc', 'hxf', 'ysj']

if age_0 > age_2 and 1991 in ages:  # and、or、in、not in
    print("True")  # 可以不用""
elif age_2 != age_3:
    print(False)  # 可以打印布尔值
elif age_2 not in ages:
    print(" multiple elif")
else:
    print("if-elif-else")

if names:  # 可以判断列表是否为空
    print("names is not empty")
else:
    print("names is empty")
