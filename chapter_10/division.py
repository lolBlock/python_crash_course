# coding = uft-8

try:
    answer = 5 / 2
except ZeroDivisionError:
    print("别想除以0")  # pass 则不做任何事情
else:
    print(answer)

filename = r'files\alice.txt'
try:
    with open(filename) as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    print('文件"' + filename + '"不存在')
