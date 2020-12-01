#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2020/12/1 11:27 上午
# @Author  : Harvey Mei <harvey.mei@msn.com>
# @FileName: printing_models.py
# @IDE     : PyCharm
# @GitHub  ：https://github.com/harveymei/

# 在函数中修改列表
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']  # 定义未打印列表
completed_models = []  # 定义已打印空列表

while unprinted_designs:  # 循环，直到未打印列表为空时终止
    current_design = unprinted_designs.pop()  # 从未打印列表弹出并赋值变量作为当前打印模型

    print("Printing model: " + current_design)  # 打印消息拼接变量告知当前打印模型
    completed_models.append(current_design)  # 移动列表中元素，将当前打印模型写入已完成模型列表

print("\nThe following models have been printed:")  # 循环结束后打印已打印完成模型信息
for completed_model in completed_models:  # 循环，遍历已完成列表并赋值变量
    print(completed_model)  # 依次打印变量值


# 优化自定义函数
#
def print_models(unprinted_designs, completed_models):  # 定义打印模型函数，传入未打印和已打印列表参数
    while unprinted_designs:  # 循环，直到未打印列表为空时终止
        current_design = unprinted_designs.pop()  # 将为打印列表中元素弹出并赋值变量

        print("Printing model: " + current_design)  # 打印已弹出元素
        completed_models.append(current_design)  # 将已弹出元素写入完成列表


def show_completed_models(completed_models):  # 定义函数，传入已完成列表参数
    print("\nThe following models have been printed:")
    for completed_model in completed_models:  # 遍历已完成列表并赋值变量
        print(completed_model)  # 依次打印变量


unprinted_designs = ['iphone', 'robot', 'car', 'dodecahedron']  # 未打印模型列表
completed_models = []  # 已完成列表，默认为空
print_models(unprinted_designs, completed_models)  # 调用打印函数，传入两个列表参数，将未打印元素移入已完成列表
show_completed_models(completed_models)  # 调用函数，查看已完成列表所有元素


# 传递任意数量的实参
# Passing an Arbitrary Number of Arguments
def make_pizza(*toppings):  # 使用带有*号的形参，创建一个名为toppings的空元组Tuple，并将传入的参数放入元组中
    """Print the list of toppoings that have been requested."""
    print(toppings)  # 打印元组


make_pizza('pepperoni')  # 传入一个参数
make_pizza('mushrooms', 'green peppers', 'extra cheese')  # 传入三个参数


# 函数改造
def make_pizza(*toppings):  # 定义函数，所有实参写入元组
    """Summarize the pizza we are about to make."""
    print("\nMaking a pizza with the following toppings:")  # 打印提示
    for topping in toppings:  # 循环遍历元组并将元素赋值变量
        print("- " + topping)  # 依次打印变量

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')


# 混合使用位置参数和任意参数
# Mixing Positional and Arbitrary Arguments
def make_pizza(size, *toppings):  # 定义函数，指定一个位置参参数和一个任意参数
    """Summarize the pizza we are about to make."""
    print("\nMaking a " + str(size) +
          "-inch pizza with the following toppings:")  # 将传入的数值参数转换为字符串并拼接字符串
    for topping in toppings:  # 遍历任意参数构成的元组并赋值变量
        print("- " + topping)  # 依次打印变量信息


make_pizza(16, 'pepperoni')  # 调用函数，传入位置参数和一个任意参数
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')  # 调用函数，传入位置参数和三个任意参数


# 使用任意关键字实参
# Using Arbitrary Keyword Arguments
def build_profile(first, last, **user_info):  # 使用两个**号构建一个名为user_info的空字典
    """Build a dictionary containing everything we know about a user."""
    profile = {}  # 定义一个空字典
    profile['first_name'] = first  # 向字典写入键值对
    profile['last_name'] = last  # 向字典写入第二个键值对
    for key, value in user_info.items():  # 遍历传入任意实参字典user_info的键值对并赋值给变量
        profile[key] = value  # 依次将变量键值对写入字典profile
    return profile  # 返回字典

# 调用函数，传入两个位置参数和部分任意参数，将返回后的字典赋值给变量
user_profile = build_profile('albert', 'einstein',
                             location='princeton',
                             field='physics')

print(user_profile)  # 打印变量


