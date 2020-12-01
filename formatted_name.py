#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2020/12/1 10:21 上午
# @Author  : Harvey Mei <harvey.mei@msn.com>
# @FileName: formatted_name.py
# @IDE     : PyCharm
# @GitHub  ：https://github.com/harveymei/

# 函数的返回值 Return Values
def get_formatted_name(first_name, last_name):  # 传入两个参数
    """Return a full name, neatly formatted."""
    full_name = first_name + " " + last_name  # 拼接传入的参数并赋值变量
    return full_name.title()  # 返回首字母大写的变量信息


musician = get_formatted_name('jimi', 'hendrix')  # 调用函数传入参数并将返回结果赋值变量
print(musician)  # 打印变量


# 增加可选的实参
def get_formatted_name(first_name, middle_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = first_name + " " + middle_name + " " + last_name
    return full_name.title()


musician = get_formatted_name('john', 'lee', 'hooker')
print(musician)


# 函数改造
def get_formatted_name(first_name, last_name, middle_name=''):  # 定义默认值为空的参数
    """Return a full name, neatly formatted."""
    if middle_name:  # 判断，传入参数不为空，拼接传入参数并赋值变量
        full_name = first_name + " " + middle_name + " " + last_name
    else:  # 传入参数为空，拼接传入参数并赋值
        full_name = first_name + " " + last_name
    return full_name.title()  # 返回变量


musician = get_formatted_name('jimi', 'hendrix')  # 传入参数赋值变量，不含中间名
print(musician)

musician = get_formatted_name('john', 'hooker', 'lee')  # 传入参数赋值变量，含中间名
print(musician)


# 函数返回字典 Return a Dictionary
def build_person(first_name, last_name):  # 定义参数
    """Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name}  # 使用传入参数构建字典并赋值变量
    return person  # 返回变量


musician = build_person('jimi', 'hendrix')  # 调用函数传入参数将返回字典赋值变量
print(musician)  # 打印变量（字典）


# 增加可选形参
def build_person(first_name, last_name, age=''):  # 定义参数默认值为空
    """Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name}  # 使用传入参数构建字典并赋值变量
    if age:  # 判断，可选形参值是否为空
        person['age'] = age  # 修改字典，加入传入参数值
    return person  # 返回变量（字典）


musician = build_person('jimi', 'hendrix', age=str(27))  # 调用函数传入可选参数并将返回字典赋值变量
print(musician)


# 定义使用while循环调用函数
def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = first_name + " " + last_name
    return full_name.title()


while True:  # 无限循环
    print("\nPlease tell me your name:")  # 提示用户输入
    f_name = input("First name: ")  # 用户输入赋值变量
    l_name = input("Last name: ")

    formatted_name = get_formatted_name(f_name, l_name)  # 将用户输入赋值变量后作为参数传入函数后将返回结果赋值变量
    print("\nHello, " + formatted_name + "!")  # 打印变量信息












