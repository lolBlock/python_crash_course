# coding = uft-8


class Car:
    """一次模拟汽车的简单尝试"""

    def __init__(self, make, model, year):
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
        self.mileage = 0  # 默认里程为0

    def car_describe(self):
        """返回整洁的描述性名称"""
        name = str(self.year) + " " + self.make + " " + self.model
        return name.title()

    def read_mileage(self):
        """显示汽车的里程"""
        print("汽车已行驶的总里程为" + str(self.mileage) + "公里")

    def update_mileage(self, mileage):  # 通过方法修改属性值，也可以直接修改，怎么防止直接修改呢？
        """修改汽车里程"""
        if mileage >= self.mileage:
            self.mileage = mileage
        else:
            print("You can't roll back a mileage!")
