# 循环遍历列表
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)

# 在for循环中处理更多事情
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician.title() + ", that was a great trick!")  # 打印三行
    print("I can't wait to see your next trcik, " + magician.title() + ".\n")  # 换行符

# 在for循环之后处理一些事情
print("Thank you, everyone. That was a great magic show!")
