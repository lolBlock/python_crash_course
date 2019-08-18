# coding = utf-8
# 手动测试get_formatted_name
from name_function import get_formatted_name

print("Enter 'q' at any time to quit.")
while True:
    first = input("\nEnter your first name: ")
    if first == 'q':
        break

    last = input("\nEnter your last name: ")
    if last == 'q':
        break

    format_name = get_formatted_name(first, last)
    print(format_name)
