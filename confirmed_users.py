#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2020/11/30 6:13 下午
# @Author  : Harvey Mei <harvey.mei@msn.com>
# @FileName: confirmed_users.py
# @IDE     : PyCharm
# @GitHub  ：https://github.com/harveymei/

# 使用while循环来处理列表和字典
# 在列表之间移动元素
unconfirmed_users = ['alice', 'brian', 'candace']  # 定义未验证用户列表
confirmed_users = []  # 定义已验证用户列表

while unconfirmed_users:  # 直到未认证用户全部移动到已验证用户列表时停止循环
    current_user = unconfirmed_users.pop()  # 在未验证列表依次弹出用户并赋值变量

    print("Verifying user: " + current_user.title())  # 打印当前用户并首字母大写
    confirmed_users.append(current_user)  # 将当前用户追加入已确认用户列表

print("\nThe following users have been confirmed:")  # 循环退出后继续执行打印
for confirmed_user in confirmed_users:  # 遍历已确认用户列表并赋值变量
    print(confirmed_user.title())  # 打印变量


