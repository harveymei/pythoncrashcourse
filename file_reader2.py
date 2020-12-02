#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2020/12/2 2:57 下午
# @Author  : Harvey Mei <harvey.mei@msn.com>
# @FileName: file_reader2.py
# @IDE     : PyCharm
# @GitHub  ：https://github.com/harveymei/

# 逐行读取文件内容
filename = 'pi_digits.txt'

with open(filename) as file_object:
    for line in file_object:
        # print(line)
        # 去除字符串右侧空字符
        print(line.rstrip())

# 在with句块以外访问文件的内容
# 将文件逐行读出放入列表并打印
filename = 'pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()  # 使用方法readline()逐行读取放入列表并赋值变量
    print(lines)

for line in lines:
    print(line.rstrip())

