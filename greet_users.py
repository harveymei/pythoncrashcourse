#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2020/12/1 11:16 上午
# @Author  : Harvey Mei <harvey.mei@msn.com>
# @FileName: greet_users.py
# @IDE     : PyCharm
# @GitHub  ：https://github.com/harveymei/


# 传递列表 Passing a List
def greet_users(names):  # 定义函数和参数
    """Print a simple greeting to each user in the list."""
    for name in names:  # 遍历传入的参数并赋值变量
        msg = "Hello, " + name.title() + "!"  # 传入变量首字母大写并拼接字符串并赋值变量
        print(msg)  # 打印字符串变量


usernames = ['hannah', 'ty', 'margot', 'tom', 'jerry']  # 定义一个列表
greet_users(usernames)  # 调用函数，传入列表，返回函数处理后的字符串信息

