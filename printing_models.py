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


