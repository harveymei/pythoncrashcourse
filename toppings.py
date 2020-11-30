#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : ${DATE} ${TIME}
# @Author  : Harvey Mei <harvey.mei@msn.com>
# @FileName: ${NAME}.py
# @IDE     : ${PRODUCT_NAME}
# @GitHub  ：https://github.com/harveymei/

# 第5章
# 检查是否不相等
requested_topping = 'mushrooms'

if requested_topping != 'anchovies':  # 判断，不相等，返回True，继续执行
    print("Hold the anchovies")

# 比较数字
# 检查是否18岁
age = 18
print(age == 18)

# 检查两个数字是否相等
answer = 17

if answer != 42:
    print("That is not the correct answer. Please try again!")

# 检查多个条件
# 检查是否两个条件都为True，可以使用and关键字
age_0 = 22
age_1 = 18
print(age_0 >= 21 and age_1 >= 21)  # 左侧通过，右侧未通过，结果返回False

age_1 = 22
print(age_0 >= 21 and age_1 >= 21)  # 左侧通过，右侧通过，结果返回True

# 使用关键字in检查特定值是否包含在列表中
requested_toppings = ['mushrooms', 'onions', 'pineapple']
print('mushrooms' in requested_toppings)
print('pepperoni' in requested_toppings)

# 使用关键字not in检查特定值是否不包含在列表中
# 禁言用户列表
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'

if user not in banned_users:  # if True:
    print(user.title() + ", you can post a response if you wish.")

# 布尔表达式的结果要么为Tue，要么为False

# 投票
age = 19
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")

# if-else语句
age = 17
if age >= 18:  # if False:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
else:  # 条件不满足时打印提示信息，实际不满足
    print("Sorry, you are too young to vote.")
    print("Please register to vote as soon as you turn 18!")

# 使用if-elif-else检查超过两个判断的情形
# 根据年龄段收费的游乐场
age = 12

if age < 4:
    print("Your admission cost is $0.")
elif age < 18:  # 输入年龄为12，仅执行检查通过的代码块
    print("Your admission cost is $5.")
else:
    print("Your admission cost is $10.")

# 更简洁的门票价格
age = 12

if age < 4:
    price = 0
elif age < 18:
    price = 5
else:
    price = 10
# 打印，使用str()函数将价格变量转化为字符串类型，并拼接字符串
print("Your admission cost is $" + str(price) + ".")


# 使用多个elif代码块，对于65岁以上老人半价购买门票
age = 12

if age < 4:
    price = 0
elif age < 18:  # 4岁以上，18岁以下
    price = 5
elif age < 65:  # 18岁以上，65岁以下
    price = 10
else:  # 65岁以上
    price = 5

# 省略else代码块
# 只要不满足if或elif中的条件测试，代码就会执行，可能会引入无效甚至恶意的数据
# 如果知道最终要测试的条件，应考虑使用一个elif代码块来代替else代码块
age = 66

if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
elif age >= 65:
    price = 5

print("Your new admission cost is $" + str(price) + ".")

# 5.3.6 测试多个条件
# if-elif-else仅适用于只有一个条件满足的情况
requested_toppings = ['mushrooms', 'extra cheese']

if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:  # 不存在，因此不会打印输出
    print("Adding pepperoni.")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")

print("\nFinished making your pizza!")

# 使用if语句处理列表
# 检查特殊元素
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
    print("Adding " + requested_topping + ".")

print("\nFinished making your pizza!")

# 使用for循环中包含if语句，处理一种材料用完的情况
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("Sorry, we are out of green peppers right now.")
    else:
        print("Adding " + requested_topping + ".")

print("\nFinished making your pizza!")

# 确定列表不是空的
requested_toppings = []

if requested_toppings:  # requested_topping = True 列表不为空
    for requested_topping in requested_toppings:
        print("Adding " + requested_topping + ".")
    print("\nFinished making your pizza!")
else:  # requested_topping = False 列表为空
    print("Are you sure you want a plain pizza?")


# 使用多个列表
available_toppings = ['mushrooms', 'olives', 'green peppers',
                      'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
# 使用for循环获取列表中的元素并使用if语句判断该元素是否存在于另外一个列表中
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print("Adding " + requested_topping + ".")
    else:
        print("Sorry, we don't have " + requested_topping + ".")
    print("\nFinished making your pizza!")
