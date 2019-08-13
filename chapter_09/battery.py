# coding = utf-8


class Battery:  # 从空白创建一个类时可以用()，也可以省略
    """创建一个电瓶类"""

    def __init__(self, battery_size=70):
        """初始化电瓶的属性"""
        self.battery_size = battery_size

    def describe_battery(self):
        """打印一条描述电瓶容量的消息"""
        print("本电瓶容量为" + str(self.battery_size) + "-kwh.")
