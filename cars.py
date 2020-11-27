# 使用sort()方法对列表进行永久排序
# 按照字母顺序进行排序
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)
# 也可以反向排列
# Sort this list in reverse alphabetical order
cars.sort(reverse=True)  # 向sort()方法传递参数
print(cars)

# 使用sorted()函数对列表进行临时排序
# Sorting a List Temporarily with the sorted() Function
cars = ['bmw', 'audi', 'toyota', 'subaru']

print("Here is the original list: ")
print(cars)

print("\nHere is the sorted list: ")
print(sorted(cars))

print("\nHere is the original list again: ")
print(cars)
# sorted()函数同样支持reverse=True参数进行反向排序

# 打印反向排序的列表
# Print a List in Reverse Order
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)

cars.reverse()  # 使用reverse()方法反转整个列表中元素的排序
print(cars)

# 获取列表长度
# Finding the Length of a List
len(cars)

# Seeing the World
locations = ['tokyo', 'taiwan', 'korea', 'thailand', 'hongkong', 'macau']
print("Print list in original order: \n" + str(locations))
# 排序，不改变列表内实际内容
print(sorted(locations))
print(locations)  # 列表内容未改变
# 反向排序列表
print("反向排序：")
locations.reverse()
print(locations)
print("再次反向排序：")
locations.reverse()
print(locations)

# Dinner Guests
guests = ['jimmy chen', 'thomas leng', 'benson deng']
print("There are " + str(len(guests)) + " Persons.")



