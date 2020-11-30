#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2020/11/30 6:49 下午
# @Author  : Harvey Mei <harvey.mei@msn.com>
# @FileName: mountain_poll.py
# @IDE     : PyCharm
# @GitHub  ：https://github.com/harveymei/

responses = {}  # 定义空字典

polling_active = True  # 设置一个标志Flag

while polling_active:  # 循环直到标志设置修改为False时终止
    name = input("\nWhat is your name? ")  # 输入用户名
    response = input("Which mountain would you like to clim someday? ")  # 输入信息

    responses[name] = response  # 将用户输入信息放入以用用户名为key的字典
    repeat = input("Would you like to let another person respond? (yes/ no) ")  # 选择是否继续录入
    if repeat == 'no':
        polling_active = False  # 用户选择不再输入是修改标志，停止循环

print("\n--- Poll Results ---")
for name, response in responses.items():  # 遍历字典中列表并赋值给变量（用户名对应输入信息）
    print(name + " would like to clim " + response + ".")  # 打印用户名及对应输入信息



