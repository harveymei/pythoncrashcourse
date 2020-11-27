# 列表包含多个元素，列表名称应使用复数。
# 用方括号表示列表，用逗号分割列表中的元素。

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

# 访问列表中的元素
# 通过位置position或索引index访问列表中的元素
print(bicycles[0])

# 使用title()方法格式化输出字符串,首字母大写
print(bicycles[0].title())

# 位置索引从0开始而不是从1开始
print(bicycles[1])  # 列表中的第2个元素
print(bicycles[3])  # 列表中的第4个元素

# Python支持反向索引，从-1开始
print(bicycles[-1].title())

# 从列表中取值
message = "My first bicycle was a " + bicycles[0].title() + "."
print(message)

# 存储朋友名称，依次打印
friends = ['thomas leng', 'jimmy chen', 'benson deng']
print("First friend is " + friends[0].title())
print("Second friend is " + friends[1].title())
print("Third friend is " + friends[-1].title())


