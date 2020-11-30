#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2020/11/30 12:24 下午
# @Author  : Harvey Mei <harvey.mei@msn.com>
# @FileName: favorite_languages.py
# @IDE     : PyCharm
# @GitHub  ：https://github.com/harveymei/

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

for name, language in favorite_languages.items():  # 遍历列表中的字典键值对并赋值给变量
    print(name.title() + "'s favorite language is " +
          language.title() + ".")


# 使用方法keys()遍历字典中的所有键
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

for name in favorite_languages.keys():  # 遍历列表中的字典键并赋值给变量
    print(name.title())

print(favorite_languages.keys())


# 遍历字典，在名字为指定名字时打印消息
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
# 定义朋友列表
friends = ['phil', 'sarah']

for name in favorite_languages.keys():  # 使用for循环遍历字典中的键并赋值变量
    print(name.title())  # 打印首字母大写的姓名
    
    if name in friends:  # 判断，姓名在朋友列表中则打印包含该首字母大写姓名和兴趣语言的消息
        print(" Hi " + name.title() +
              ", I see your favorite language is " +
              favorite_languages[name].title() + "!")  # 打印字典中键name对应的首字母大写language值

# 方法keys()遍历字典并返回一个列表
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")


# 按顺序遍历字典中的所有键
# 在for循环中对返回的键进行排序
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

# 使用keys()方法对字典中的name生成列表，并使用storted()函数排序，并依次赋值给变量
for name in sorted(favorite_languages.keys()):
    print(name.title() + ", thank you for taking the poll.")


# 使用values()方法遍历字典中的所有值
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())

# 使用set()集合函数，去除重复项
print("去除重复项")
for language in set(favorite_languages.values()):
    print(language.title())
