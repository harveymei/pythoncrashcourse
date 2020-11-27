# 列表切片
# List Slice
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])  # 打印列表第1-3个元素
print(players[1:4])  # 2-4个元素
print(players[:4])  # 1-4个元素
print(players[2:])  # 3-末尾
# 复数索引返回离列表末端相应距离的元素
# 输入最后三名队员
print(players[-3:])

# 使用for循环和切片遍历列表中的部分元素
print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())
