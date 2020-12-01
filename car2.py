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
        self.odometer_reading = 0

    def get_descriptive_name(self):  # 定义描述完整信息的方法
        """Return a neatly formatted descriptive name."""
        long_name = str(self.year) + " " + self.make + " " + self.model  # 拼接变量字符串并赋值变量
        return long_name.title()  # 返回字符串并首字母大写

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print("This car has " + str(self.odometer_reading) + " miles on it.")


my_new_car = Car("audi", "a4", 2016)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

