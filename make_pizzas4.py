#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2020/12/1 2:51 下午
# @Author  : Harvey Mei <harvey.mei@msn.com>
# @FileName: make_pizzas4.py
# @IDE     : PyCharm
# @GitHub  ：https://github.com/harveymei/

# 为模块指定别名
# Using as to Give a Module an Alias
import pizza2 as p

p.make_pizza(16, 'pepperoni')
p.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# import module_name as mn

# 导入函数的所有模块（不建议）
# from module_name import *
