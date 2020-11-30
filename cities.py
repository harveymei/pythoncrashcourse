#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2020/11/30 6:02 下午
# @Author  : Harvey Mei <harvey.mei@msn.com>
# @FileName: cities.py
# @IDE     : PyCharm
# @GitHub  ：https://github.com/harveymei/

# 使用break语句退出循环
prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.) "

while True:
    city = input(prompt)

    if city == 'quit':
        break  # 退出循环
    else:
        print("I'd love to go to " + city.title() + "!")

