#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2020/11/30 11:01 上午
# @Author  : Harvey Mei <harvey.mei@msn.com>
# @FileName: alien.py
# @IDE     : PyCharm
# @GitHub  ：https://github.com/harveymei/

# 字典是一系列键值对，每个键都与一个值相关联。
alien_0 = {'color': 'green', 'points': 5}

# 要获取与键相关联的值，可依次指定字典名和放在方括号内的键。
print(alien_0['color'])
print(alien_0['points'])

# 访问字典中的值
alien_0 = {'color': 'green', 'points': 5}

new_points = alien_0['points']
print("You just earned " + str(new_points) + " points!")

# 添加键值对
# 字典是一种动态结构，可以随时在其中添加键值对。
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

# 创建空字典
alien_0 = {}

alien_0['color'] = 'green'
alien_0['points'] = 5

print(alien_0)

# 修改字典中的值
alien_0 = {'color': 'green'}
print("The alien is " + alien_0['color'] + ".")  # 打印颜色
# 修改颜色
alien_0['color'] = 'yellow'
print("The alien is now " + alien_0['color'] + ".")


# 移动并更新位置
alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print("Original x-postion: " + str(alien_0['x_position']))  # 打印原始x坐标

# 向右移动外星人
# 根据外星人当前速度决定将其移动多元
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3

alien_0['x_position'] = alien_0['x_position'] + x_increment  # 0 + 2
print("New x-position: " + str(alien_0['x_position']))


# 使用del关键字删除键值对
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

del alien_0['points']
print(alien_0)


# 由类似对象组成的字典
# 字典可以存储一个对象的多种信息，也可以存储多种对象的同一种信息
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',  # 在最后一个键值对之后加上逗号，为新一行键值对添加做好准备
}

# 给定名字获取语言
print("Sarah's favorite language is " +
      favorite_languages['sarah'].title() +
      ".")


# 遍历字典
# 遍历所有键值对
user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
}
# 使用for循环遍历字典
for key, value in user_0.items():  # items()方法返回一个键值对列表
    print("\nKey: " + key)
    print("Value: " + value)

print(user_0.items())
