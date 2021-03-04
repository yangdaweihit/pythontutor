#! /usr/bin/env python3
# -*- coding: utf-8 -*-

# 参考
# https://www.python-course.eu/python3_formatted_output.php
# 《Pythond基础教程》第3章3.2节

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
