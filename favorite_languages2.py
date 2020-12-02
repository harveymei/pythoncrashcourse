#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2020/12/2 2:20 下午
# @Author  : Harvey Mei <harvey.mei@msn.com>
# @FileName: favorite_languages2.py
# @IDE     : PyCharm
# @GitHub  ：https://github.com/harveymei/

# 使用Python标准库
# 使用collections模块中的OrderedDic有序字典类，按照字典中键值对添加顺序排序
from collections import OrderedDict

favorite_languages = OrderedDict()  # 实例化类（创建一个空有序字典），并赋值给变量

favorite_languages['jen'] = 'python'  # 依次向字典添加键值对
favorite_languages['sarah'] = 'c'
favorite_languages['edward'] = 'ruby'
favorite_languages['phil'] = 'python'

for name, language in favorite_languages.items():  # 遍历列表存储的键值对并赋值给变量
    print(name.title() + "'s favorite language is " +  # 依次打印首字母大写变量值及拼接字符串
          language.title() + ".")
