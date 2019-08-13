# coding = utf-8
from car import Car
from car_battery import CarBattery


class ElectricCar(Car):
    """模拟电动汽车的独特之处"""
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = CarBattery(make)  # 将实例用作属性
