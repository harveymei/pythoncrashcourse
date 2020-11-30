#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2020/11/30 4:43 下午
# @Author  : Harvey Mei <harvey.mei@msn.com>
# @FileName: parrot.py
# @IDE     : PyCharm
# @GitHub  ：https://github.com/harveymei/
message = input("Tell me something, and I will repeat it back to you: ")
print(message)

name = input("Please enter your name: ")
print("Hello, " + name + "!")

prompt = "If you tell us who you are, we can personalize the message you see."
prompt += "\nWhat is your first name? "

name = input(prompt)
print("\nHello, " + name + "!")

