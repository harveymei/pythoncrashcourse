#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2020/12/1 6:44 下午
# @Author  : Harvey Mei <harvey.mei@msn.com>
# @FileName: car.py
# @IDE     : PyCharm
# @GitHub  ：https://github.com/harveymei/

class Car():  # 从空白创建类
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = str(self.year) + " " + self.make + " " + self.model
        return long_name.title()

my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
