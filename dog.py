#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2020/12/1 3:10 下午
# @Author  : Harvey Mei <harvey.mei@msn.com>
# @FileName: dog.py
# @IDE     : PyCharm
# @GitHub  ：https://github.com/harveymei/

class Dog():
    """A simple attempt to model a dog."""

    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(self.name.title() + " is nwo sitting.")

    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(self.name.title() + " rolled over!")

