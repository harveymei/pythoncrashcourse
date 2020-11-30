#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2020/11/30 6:21 下午
# @Author  : Harvey Mei <harvey.mei@msn.com>
# @FileName: pets.py
# @IDE     : PyCharm
# @GitHub  ：https://github.com/harveymei/

# 删除包含特定值的所有列表元素
# 使用remove()函数
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)  # 打印列表中所有动物

while 'cat' in pets:  # 在列表中不再有cat元素时终止
    pets.remove('cat')  # 对列表执行删除元素操作

print(pets)  # 打印不含cat的列表

# 7.3.3 使用用户输入来填充字典
