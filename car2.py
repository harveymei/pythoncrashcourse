#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2020/12/1 7:05 下午
# @Author  : Harvey Mei <harvey.mei@msn.com>
# @FileName: car2.py
# @IDE     : PyCharm
# @GitHub  ：https://github.com/harveymei/

# 设置属性的默认值
# Setting a Default Value for an Attribute
class Car():

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0  # 指定属性（里程表）的默认值

    def get_descriptive_name(self):  # 定义描述完整信息的方法
        """Return a neatly formatted descriptive name."""
        long_name = str(self.year) + " " + self.make + " " + self.model  # 拼接变量字符串并赋值变量
        return long_name.title()  # 返回字符串并首字母大写

    def read_odometer(self):  # 定义读取里程表的方法
        """Print a statement showing the car's mileage."""
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):  # 定义修改里程表的方法（使用方法修改属性值）
        """Set the odometer reading to given value.
        Reject the change if it attempts to roll the odometer back.
        """
        if mileage >= self.odometer_reading:  # 增加判断，最新里程表读数只能大于当前读数
            self.odometer_reading = mileage  # 使用该方法传入参数值重新赋值给属性
        else:
            print("You can't roll back an odometer!")  # 提示用户不可以回调读数

    def increment_odomter(self, miles):  # 定义累加计算里程表读数的方法，传入新增里程参数
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles  # 最新里程读数计算


my_new_car = Car("audi", "a4", 2016)  # 传入参数创建实例
print(my_new_car.get_descriptive_name())  # 调用实例的get_descriptive_name()方法，打印完整描述信息
my_new_car.read_odometer()  # 调用实例的read_odometer()方法，打印拼接里程表读数的字符串信息

# 修改属性值
# Modifying Attribute Values
# 直接修改属性值
# Modifying an Attribute's Value Directly
my_new_car.odometer_reading = 23
my_new_car.read_odometer()

# 使用方法修改属性（依赖于update_odometer()方法）
# Modifying an Attribute's Value Through a Method
my_new_car.update_odometer(23)
my_new_car.read_odometer()

# 使用方法累加属性值（依赖于increment_odometer()方法）
my_used_car = Car("subaru", 'outback', 2013)  # 创建一个新实例
print(my_used_car.get_descriptive_name())  # 调用实例方法打印实例完整描述信息

my_used_car.update_odometer(23500)  # 调用里程表累加方法，传入新增里程参数
my_used_car.read_odometer()  # 调用该实例的方法获取最新里程读数

my_used_car.increment_odomter(100)
my_used_car.read_odometer()  # 23600



