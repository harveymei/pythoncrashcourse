#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2020/11/30 4:10 下午
# @Author  : Harvey Mei <harvey.mei@msn.com>
# @FileName: pizza.py
# @IDE     : PyCharm
# @GitHub  ：https://github.com/harveymei/

# 在字典中存储列表
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
}

print("You ordered a " + pizza['crust'] + "-crust pizza" +
      "with the following toppings:")

for topping in pizza['toppings']:
    print("\t" + topping)


