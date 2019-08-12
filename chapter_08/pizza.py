# coding = utf-8


def show_pizza(*toppings):
    """形参*toppings可以接受任意数量的相同类型的实参，且会封装到一个元组
    如果使用**toppings，则可以接受任意数量的关键字实参/键-值对，且会封装到一个字典"""
    print(toppings)


def make_pizza(size, color='red', *toppings):
    """要想函数接受不同类型的实参，需要把*toppings放到后面
    此时再用默认参数是有些鸡肋的"""
    print("The " + color + " pizza is " + str(size) + "cm")
    print(toppings)


make_pizza(25, 'green', 'a', 'b', 'c')
make_pizza(30, 'green')  # *toppings可以为空

# 将函数存储在模块，从模块导入函数阅读书籍8.6即可