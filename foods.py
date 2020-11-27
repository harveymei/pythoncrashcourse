# 复制列表
# 创建一个包含整个列表的切片，方法是同时省略起始索引和终止索引（[:]）
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]  # 复制列表并赋值变量
print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)

# 在两个列表中添加不同食品
my_foods.append('cannoli')
friend_foods.append('ice cream')
print(my_foods)
print(friend_foods)

# 列表切片
cars = ['bmw', 'toyota', 'honda', 'benz', 'ford']
# 打印列表前三个元素
print("The first three items in the list are:")
print(cars[:3])
# 打印列表中间三个元素
print("Three items from the middle of the list are:")
print(cars[1:4])
# 打印末尾三个元素
print("The last three items in the list are:")
print(cars[-3:])


