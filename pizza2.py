#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2020/12/1 2:37 下午
# @Author  : Harvey Mei <harvey.mei@msn.com>
# @FileName: pizza2.py
# @IDE     : PyCharm
# @GitHub  ：https://github.com/harveymei/

# 在模块中存储自定义函数
# Storing Functions in Modules
# 使用模块文件存储自定义函数并在主程序中导入模块
def make_pizza(size, * toppings):
    """"Summarize the pizza we are about to make. """
    print("\nMaking a " + str(size) +
          "-inch pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)
