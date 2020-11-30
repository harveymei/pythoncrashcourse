#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2020/11/30 5:16 下午
# @Author  : Harvey Mei <harvey.mei@msn.com>
# @FileName: rollercoaster.py
# @IDE     : PyCharm
# @GitHub  ：https://github.com/harveymei/

# 判断一个人的身高是否满足坐过山车的身高要求
height = input("How tall are you, in inches? ")
height = int(height)  # 将字符串类型转换为整数类型

if height >= 36:  # 使用转换后的数值进行布尔运算比较
    print("\nYou're tall enough to ride!")
else:
    print("\nYou'll be able to ride when you're a little older.")

# 求模运算符
# 两数相除返回余数
print(4 % 3)  # 余1
print(5 % 3)  # 余2
print(6 % 3)  # 余0
print(7 % 3)  # 余1

# 判断奇数或者偶数
number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)

if number % 2 == 0:
    print("\nThe number " + str(number) + " is even.")
else:
    print("\nThe number " + str(number) + " is odd.")

