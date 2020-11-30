#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2020/11/30 3:06 下午
# @Author  : Harvey Mei <harvey.mei@msn.com>
# @FileName: aliens.py
# @IDE     : PyCharm
# @GitHub  ：https://github.com/harveymei/

# 将一系列字典存储在列表中，或将列表作为值储存在字典中，称为嵌套。
# 字典列表
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)

# 定义空列表
aliens = []

for alien_number in range(30):  # 使用for循环，对列表写入30条字典记录
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

for alien in aliens[:5]:  # 遍历列表前5个字典并赋值给变量并依次打印
    print(alien)
print("...")

print("Total number of aliens: " + str(len(aliens)))  # 使用len()函数计算列表中字典数量

#