# coding = utf-8
from battery import Battery


class CarBattery(Battery):  # 继承
    """创建一个汽车电瓶类"""

    def __init__(self, car_brand='others'):  # 子类的构造函数
        super().__init__()  # 先初始化父类的属性，调用父类的构造函数
        self.car_brand = car_brand  # 再初始化汽车电瓶特有的属性

        if self.battery_size == 70:
            self.run_range = 240
        elif self.battery_size == 85:
            self.run_range = 270
        else:
            self.run_range = 250

    def describe_battery(self):  # 可以重写父类的函数
        print("这是用于" + self.car_brand + "的电瓶，容量为" + str(self.battery_size) + "kwh。")

    def get_range(self):
        message = "充满电状态下，这辆车可以行使" + str(self.run_range)
        message += "公里。"
        print(message)
