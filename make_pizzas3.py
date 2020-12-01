#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2020/12/1 2:47 下午
# @Author  : Harvey Mei <harvey.mei@msn.com>
# @FileName: make_pizzas3.py
# @IDE     : PyCharm
# @GitHub  ：https://github.com/harveymei/

# 赋予函数别名
# Using as to Give a Function an Alias
# 函数名称太长或有冲突，可以使用别名
from pizza2 import make_pizza as mp

mp(16, 'pepperoni')
mp(12, 'mushrooms', 'green peppers', 'extra cheese')
