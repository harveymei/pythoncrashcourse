#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2020/12/2 10:00 上午
# @Author  : Harvey Mei <harvey.mei@msn.com>
# @FileName: electric_car.py
# @IDE     : PyCharm
# @GitHub  ：https://github.com/harveymei/

# 类的继承 Inheritance
# 如果你要编写的类是另一个现成类的特殊版本，可使用继承。
# 一个类继承另一个类时，它将自动获得另一个类的所有属性和方法；原有的类称为父类，而新类称为子类。
# 子类继承了其父类的所有属性和方法，同时还可以定义自己的属性和方法。
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


# 定义一个新类，从Car类创建新类
class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """Initialize attribute of the parent class."""
        super().__init__(make, model, year)  # super()函数是调用父类也称为超类（superclass）的方法，


my_tesla = ElectricCar("tesla", 'model s', 2016)  # 调用子类传入参数并创建实例
print(my_tesla.get_descriptive_name())  # 调用实例的和实例继承的方法打印完整描述信息


# 定义子类的专有属性和方法
# Defining Attributes and Methods for the Child Class
class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery_size = 70  # 新增属性并设置初始值

    def describe_battery(self):  # 定义一个新方法用于显示电池容量信息
        print("This car has a " + str(self.battery_size) + "-KWh battery.")  # 调用属性取值并拼接字符串


my_tesla = ElectricCar('tesla', 'model s', 2016)  # 调用子类传入参数并创建实例
print(my_tesla.get_descriptive_name())  # 调用子类的继承方法打印完整描述信息
my_tesla.describe_battery()  # 调用子类的新增方法，打印电量信息

# 父类的方法不符合子类情况的，都可以重写父类

