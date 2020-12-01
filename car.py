#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2020/12/1 6:44 下午
# @Author  : Harvey Mei <harvey.mei@msn.com>
# @FileName: car.py
# @IDE     : PyCharm
# @GitHub  ：https://github.com/harveymei/

class Car():  # 从空白创建类
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):  # 定义默认方法
        """Initialize attributes to describe a car."""
        self.make = make  # 传入变量赋值给可供类中其他方法调用或实例调用的变量
        self.model = model
        self.year = year

    def get_descriptive_name(self):  # 定义描述完整信息的方法
        """Return a neatly formatted descriptive name."""
        long_name = str(self.year) + " " + self.make + " " + self.model  # 拼接变量字符串并赋值变量
        return long_name.title()  # 返回字符串并首字母大写


my_new_car = Car('audi', 'a4', 2016)  # 创建实例，传入参数
print(my_new_car.get_descriptive_name())  # 调用实例中的方法，打印完整信息

