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
