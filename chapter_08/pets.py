# coding = uft-8


def describe_pet(animal_type, pet_name='dopa'):  # 默认参数必须右对齐
    """显示宠物的信息"""
    print("\nI have a " + animal_type + ", its name is " + pet_name + ".")


# 位置实参:顺序很重要，但不用指定形参
describe_pet('dog', 'pi')

# 关键字实参：顺序不重要，但要准确指定形参
describe_pet(pet_name='mi', animal_type='cat')  # PEP8关键字/变量相等后面不需要空格
