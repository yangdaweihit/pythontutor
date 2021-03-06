#! /usr/bin/env python3
# -*- coding: utf-8 -*-

# -----------------------------------------------------------------------
# 2021年3月2日 浅拷贝和深拷贝
# 主讲：杨大伟
# 参考
# - https://www.python-course.eu/python3_deep_copy.php
# -《Pythond基础教程》第59页

from copy import deepcopy
a = [1, 2, 3, [1, 2, 3]]
b = a
c = a.copy()
d = deepcopy(a)

b[0] = 0
print("a = {}\nb = {}\nc = {}\nd = {}".format(a, b, c, d))
# 注意，a,b的第1个元素全都变为了0，为什么？
# 注意，c,d的第1个元素没有变，为什么？

c[0] = -1
print("a = {}\nb = {}\nc = {}\nd = {}".format(a, b, c, d))
# 注意，c的第1个元素全都变为了-1，其它没有变，为什么？

c[3][0] = 4
print("a = {}\nb = {}\nc = {}\nd = {}".format(a, b, c, d))
# 注意，a,b,c的第4个元素(一个列表)中的第一个值全是4，为什么？

c[3] = [5, 2, 3]
print("a = {}\nb = {}\nc = {}\nd = {}".format(a, b, c, d))
# 注意，c的第4个元素(一个列表)变化了，但a,b的第4个元素没变，为什么？

# ----------------------------------------------------------------------
# 2021年3月4日 输出格式化
# 主讲：杨大伟
# 参考
# - https://www.python-course.eu/python3_formatted_output.php
# -《Pythond基础教程》第3章3.2节

q = 459
p = 0.098
print(q, p, p * q, '1', 0, 2, 'adf', [12, 2, 3])
print(q, p, p * q, sep=".....")


def add(a, b):
    return a + b


print(add(1, 2))
print(add(1, 2, 3))
print(str(q) + " " + str(p) + " " + str(p * q))
print("%5d" % (3 + 2))

print("%10.3e" % (356.08977))
print("%10.4e" % (356.08977))
print("%10.5e" % (356.08977))
print("%10.6e" % (356.08977))
print("%10.7e" % (356.08977))

print("{0:>15s}{1:<8.2f}".format("Spam & Eggs:", 6.99))
print("{0:>15s}{1:<8.2f}".format("Spam :", 12346.99))

# ----------------------------------------------------------------------
# 2021年3月6日 列表生成式
# 主讲：徐福龙
