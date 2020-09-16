# 打印100到999中的水仙花数

for x in range(100, 1000):
    a = int(x / 100)
    b = int((x - a * 100) / 10)
    c = x - a * 100 - b * 10
    y = a**3 + b**3 + c**3
    if x == y:
        print("{0}**3 + {1}**3 + {2}**3 = {3}".format(a, b, c, x))
