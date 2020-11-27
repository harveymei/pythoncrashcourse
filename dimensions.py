# 元组
# 元素不可变的列表称为元组
# 矩形长宽
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

# 遍历元组中的所有值
dimensions = (200, 50)
for dimension in dimensions:
    print(dimension)

# 修改元组变量
# 元组中的元素不可修改，但元组变量可以重新赋值
# 元组用于存储在程序整个生命周期内都不变的数值
dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)

# 自助餐
foods = ('egg', 'bread', 'milk', 'pizza', 'apple')
for food in foods:
    print(food)

# 菜单调整，替换其中两种食品
foods = ('egg', 'hotdog', 'milk', 'pizza', 'orange')
for food in foods:
    print(food)

print("new food: " + foods[1])
print("new food: " + foods[4])

# Python改进提案
# Python Enhancement Proposal
