# 将1-10的依次进行平方运算并放入列表
squares = []
for value in range(1, 11):  # for循环遍历1-10并赋值给变量value
    square = value ** 2
    squares.append(square)

print(squares)

# 数值列表的简单统计
# Simple Statistics with a List of Numbers
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))  # min()函数，最小数值
print(max(digits))  # max()函数，最大数值
print(sum(digits))  # sum()函数，求和

# 列表解析
# List Comprehensions
squares = [value ** 2 for value in range(1, 11)]
print(squares)

# 使用一个for循环打印数字1-20（含）
for number in range(1, 21):
    print(number)

# 创建包含1-1000000的列表，并打印列表，最大值，最小值，和累加值
num_list = []
for number in range(1, 1000001):
    num_list.append(number)

print(num_list)
print(min(num_list))
print(max(num_list))
print(sum(num_list))

# 创建奇数列表并使用for循环的打印
num_list = []
for number in range(1, 20, 2):
    num_list.append(number)

print(num_list)

# 创建列表，包含3-30以内能被3整出的数字，使用for循环打印列表中数字
# Threes
treble = []
for number in range(3, 31):
    if number % 3 == 0:
        treble.append(number)

print(treble)

for number in treble:
    print(number)

# 创建列表，包含1-10的立方值，并使用for循环打印列表元素
# Cubes
cube = []
for number in range(1, 11):
    cube.append(number ** 3)
print(cube)

for number in cube:
    print(number)

# 使用列表解析List Comprehension生成包含1-10的立方列表
cube = [number ** 3 for number in range(1, 11)]
print(cube)
