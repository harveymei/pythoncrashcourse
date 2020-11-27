# 修改列表元素
# Modifying Elements in a List
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

# 指定列表名称和元素索引，并指定希望修改的值
motorcycles[0] = 'ducati'
print(motorcycles)

# 向列表中添加元素
# Adding Elements to a List
# 在列表末尾追加元素
# append()方法在不影响列表中其他数据情形下添加新元素
motorcycles.append('ducati')
print(motorcycles)

# append()方法可以快速构建动态列表
motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)

# 在列表中插入元素
# Insert Elements into a List
# insert()方法在位置0插入对应值
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(0, 'ducati')
print(motorcycles)

# 删除元素，使用del语句
# Removing an Item Using the del Statement
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
del motorcycles[0]
print(motorcycles)

# 使用位置索引可以移除任何位置的元素
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
del motorcycles[1]
print(motorcycles)

# 使用pop()方法移除列表中元素
# Removing an Item Using the pop() Method
# 使用从列表中已经移除的元素值
# pop()方法移除（弹出）列表中的最后一个元素
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
poped_motocycles = motorcycles.pop()  # 将弹出列表元素赋值给变量
print(motorcycles)
print(poped_motocycles)  # 打印已移除的元素

#
motorcycles = ['honda', 'yamaha', 'suzuki']
last_owned = motorcycles.pop()
print("The last motorcycle I owned was a " + last_owned.title() + ".")

# 使用位置索引弹出列表中的元素
# Poping Items from any Position in a List
motorcycles = ['honda', 'yamaha', 'suzuki']
first_owned = motorcycles.pop(0)  # 弹出列表中第一个元素
print(motorcycles)
print("The first motorcycle I owned was a " + first_owned.title() + ".")
# 选择使用del语句还是pop()方法
# 删除元素后不再使用该元素使用del语句，删除后仍然需要使用该元素值则使用pop()方法

# 在不知道元素位置索引的情况下，使用元素值移除列表中元素
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

motorcycles.remove('ducati')
print(motorcycles)

#
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

too_expensive = 'ducati'  # 将元素赋值给变量
motorcycles.remove(too_expensive)  # 对变量执行remove()方法
print(motorcycles)
print("\nA " + too_expensive.title() + " is too expensive for me.")
# remove()方法只能删除列表中第一次出现的元素
# 如果相同元素多次出现则需要使用循环

# 访客列表
# Guest List
guests = ['jimmy chen', 'benson deng', 'thomas leng']
print("Welcome " + guests[0])
print("Welcome " + guests[1])
print("Welcome " + guests[2])

# 修改访客列表
# Changing Guest List
guests[0] = 'harvey mei'  # 替换无法到达访客
print(guests)
print("Welcome " + guests[0].title() + ", " + guests[1].title() + ", " + guests[2].title())

# 更多访客
# More Guests
guests.insert(0, 'tom zhang')  # 在列表中起始处插入新元素
print(guests)
guests.insert(2, 'jerry wang')  # 在列表中部插入新元素
print(guests)
guests.append('toby li')  # 在列表末尾追加新元素
print(guests)

# 清除列表中访客
# Shrinking Guest List
print("New dinner table won't arrive in time for the dinner.")
print(guests)
guests.pop()  # 删除访客，直到列表中仅有两个访客
print(guests)
guests.pop()
guests.pop()
guests.pop()
print(guests)
# 使用del语句删除列表中的剩余两个访客
del guests[:]
print(guests)  # 打印空列表


