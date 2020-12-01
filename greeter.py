#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2020/12/1 9:16 上午
# @Author  : Harvey Mei <harvey.mei@msn.com>
# @FileName: greeter.py
# @IDE     : PyCharm
# @GitHub  ：https://github.com/harveymei/

# 函数
def greet_user():
    """Display a simple greeting."""  # 文档字符串
    print("Hello!")


greet_user()  # 调用函数

# Passing Information to a Function
# 向函数传递参数
def greet_user(username):
    """Display a simple greeting."""
    print("Hello, " + username.title() + "!")


greet_user('jesse')

# 实参Arguments和形参Parameters
# 函数定义中的参数称为形参，函数调用中的参数称为实参


# 位置实参 Positional Arguments
def describe_pet(animal_type, pet_name):  # 定义函数，定义两个参数
    """Display information about a pet."""
    print("\nI have a " + animal_type + ".")  # 打印传入的参数
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")


describe_pet('hamster', 'harry')
# 再次调用函数
describe_pet('dog', 'willie')

# 位置参数的顺序
describe_pet('harry', 'hamster')

# 关键字实参 Keyword Arguments
def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")


# 调用函数，传入关键字实参
describe_pet(animal_type='hamster', pet_name='harry')
# 关键字实参可以改变传入的顺序
describe_pet(pet_name='harry', animal_type='hamster')


# 函数的参数默认值 Default Values
def describe_pet(pet_name, animal_type='dog'):
    """Display information about a pet."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")


# 使用参数默认值
describe_pet(pet_name='willie')
describe_pet('harry')

# 修改参数默认值
describe_pet(pet_name='harry', animal_type='hamster')
