#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2020/12/2 2:34 下午
# @Author  : Harvey Mei <harvey.mei@msn.com>
# @FileName: file_reader.py
# @IDE     : PyCharm
# @GitHub  ：https://github.com/harveymei/

# 读取文件
# Reading an Entire File
# 使用open()函数并指定文件名称打开文件
# 使用with关键字在不再访问文件时自动关闭文件，而无需使用close()函数手工关闭
with open("pi_digits.txt") as file_object:  # 打开文件，返回对象并赋值给变量
    contents = file_object.read()  # 使用read()方法读取文件内容，以字符串形式赋值给变量
    print(contents)  # 打印变量（读取的内容）


# 文件的路径
with open('text_files/filename.txt') as file_object:

# 使用绝对路径
file_path = '/home/ehamtthes/other_files/text_files/filename.txt'
with open(file_path) as file_object:



