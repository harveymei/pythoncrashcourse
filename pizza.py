#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2020/11/30 4:10 下午
# @Author  : Harvey Mei <harvey.mei@msn.com>
# @FileName: pizza.py
# @IDE     : PyCharm
# @GitHub  ：https://github.com/harveymei/

# 在字典中存储列表
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],  # 列表作为值
}

print("You ordered a " + pizza['crust'] + "-crust pizza" +
      "with the following toppings:")

for topping in pizza['toppings']:  # for循环遍历字典中的列表并赋值给变量
    print("\t" + topping)  # 打印变量


#
favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
}

# 遍历字典中列表，将名称和语言依次赋值给变量name和languages
for name, languages in favorite_languages.items():
    print("\n" + name.title() + "'s favorite languages are:")
    for language in languages:  # 遍历列表中的语言，并赋值给变量
        print("\t" + language.title())  # 插入制表符，打印变量

# 列表和字典的嵌套层级不应太多

# 在字典中存储字典
users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },

    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    },
}

for username, user_info in users.items():  # 遍历字典中列表，并赋值给变量
    print("\nUsername: " + username)
    full_name = user_info['first'] + " " + user_info['last']  # 使用字典中多个值拼接完整名称并赋值变量
    location = user_info['location']  # 使用字典中地点信息值赋值给变量

    print("\tFull name: " + full_name.title())  # 首字母大写打印完整名称
    print("\tLocation: " + location.title())  # 首字母大写打印地点信息




