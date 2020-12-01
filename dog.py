#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2020/12/1 3:10 下午
# @Author  : Harvey Mei <harvey.mei@msn.com>
# @FileName: dog.py
# @IDE     : PyCharm
# @GitHub  ：https://github.com/harveymei/

class Dog():  # 类的名称首字母大写，空括号表示从空白创建该类
    """A simple attempt to model a dog."""

    def __init__(self, name, age):  # 类中的函数称为方法，这是一个特殊的默认方法
        """Initialize name and age attributes."""
        self.name = name  # 以self为前缀的变量可供类中的所有方法使用
        self.age = age  # 类的任何实例也可以访问这些变量

    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(self.name.title() + " rolled over!")

# 可通过实例访问的变量称为实例的属性


# 根据类创建实例
# Making an Instance from a Class
my_dog = Dog('willie', 6)  # 创建实例，传入参数。调用__init__()方法并传入两个参数。

# 访问实例的属性，并拼接打印字符串
print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")

# 访问属性
# Accessing Attributes
print(my_dog.name)
print(my_dog.age)

# 调用方法
# Calling Methods
# 实例名称+点号+方法名
my_dog.sit()
my_dog.roll_over()

# 创建多个实例
# Creating Multiple Instances
my_dog = Dog("willie", 6)
your_dog = Dog("lucy", 3)

print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")
my_dog.sit()

print("\nYour dog's name is " + your_dog.name.title() + ".")
print("Your dog is " + str(your_dog.age) + " years old.")
your_dog.roll_over()

