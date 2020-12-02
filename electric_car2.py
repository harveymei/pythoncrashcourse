#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2020/12/2 11:40 上午
# @Author  : Harvey Mei <harvey.mei@msn.com>
# @FileName: electric_car2.py
# @IDE     : PyCharm
# @GitHub  ：https://github.com/harveymei/

# 将实例用作属性
class Car():
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + " " + self.make + " " + self.model
        return long_name.title()

    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles


class Battery():  # 定义一个电池类，在子类ElectricCar()中调用该类作为属性并赋值
    def __init__(self, battery_size=70):
        self.battery_size = battery_size

    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + "-KWh battery.")

    def get_range(self):
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270

        message = "This Car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)


class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()  # 新增属性，类Battery()实例化时未指定参数，则使用默认参数


my_tesla = ElectricCar("tesla", "model s", 2016)  # 创建实例时都同时创建一个Battery实例
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()  # 调用实例中battery方法的describe_battery()方法，打印电池容量信息
my_tesla.battery.get_range()  # 调用实例中battery方法的get_range()方法，打印可行驶里程信息
