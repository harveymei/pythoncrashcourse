#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2020/11/30 5:30 下午
# @Author  : Harvey Mei <harvey.mei@msn.com>
# @FileName: counting.py
# @IDE     : PyCharm
# @GitHub  ：https://github.com/harveymei/

# 使用while循环
current_number = 1
while current_number <= 5:  # 循环，直到大于5时终止
    print(current_number)  # 打印当前值
    current_number += 1  # 当前值加1并重新赋值

# 让用户选择循环的退出时间
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "  # 拼接两行字符串，并使用换行符
message = ""
while message != 'quit':  # 循环，直到用户输入quit为止
    message = input(prompt)
    print(message)

# 修复quit作为消息打印的问题
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

message = ""
while message != 'quit':
    message = input(prompt)

    if message != 'quit':  # 加入判断，即输入quit时，不再打印用户的输入，同时结束循环
        print(message)


# 设置标志，用于判断程序是否应继续运行
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

active = True  # 设置标志
while active:
    message = input(prompt)

    if message == 'quit':
        active = False  # 不再运行时修改标志
        print(active)
    else:
        print(message)

