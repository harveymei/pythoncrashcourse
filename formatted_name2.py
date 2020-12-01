#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2020/12/1 11:10 上午
# @Author  : Harvey Mei <harvey.mei@msn.com>
# @FileName: formatted_name2.py
# @IDE     : PyCharm
# @GitHub  ：https://github.com/harveymei/

# 避免无限循环，加入退出条件
# Define a quit condition
def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = first_name + " " + last_name
    return full_name.title()


while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time to quit)")

    f_name = input("First name: ")
    if f_name == 'q':  # 加入判断，用户输入q则终止循环
        break

    l_name = input("Last name: ")
    if l_name == 'q':  # 加入判断，用户输入q则终止循环
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print("\nHello, " + formatted_name + "!")

