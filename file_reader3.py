#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2020/12/2 3:23 下午
# @Author  : Harvey Mei <harvey.mei@msn.com>
# @FileName: file_reader3.py
# @IDE     : PyCharm
# @GitHub  ：https://github.com/harveymei/

# Working with a File's Contents
filename = 'pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()
    print(lines)

pi_string = ""  # 空字符串赋值变量
for line in lines:  # 遍历每个字符
    # pi_string += line.rstrip()  # 拼接每个字符
    # 同时去除字符串中左侧和右侧的空白字符
    pi_string += line.strip()

print(pi_string)  # 打印完整拼接后的字符
print(len(pi_string))  # 计算拼接后字符串的长度
