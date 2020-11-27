# 遍历列表，根据名称判断打印全大写名称还是首字母大写名称
cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())  # 使用upper()方法转换小写字母为大写字母
    else:
        print(car.title())  # 使用title()方法转换首字母为大写字母

