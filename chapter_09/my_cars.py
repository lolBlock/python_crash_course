# coding = uft-8
from electric_car import Car, ElectricCar

my_audi = Car('audi', 'A6L', 2016)
print(my_audi.car_describe())

my_tesla = ElectricCar('tesla', 'roadster', 2017)
print(my_tesla.car_describe())

my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
