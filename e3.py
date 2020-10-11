#! /usr/bin/env python3
# -*- coding: utf-8 -*-
"""
自定义函数

def functionName(parameter):
    suite
"""

import math
import string

# 例1
def heron(a, b, c):
    s = (a + b + c) / 2
    return math.sqrt(s * (s - a) * (s - b) * (s - c))

# print(heron(3, 4, 5))

# # 例2
# def letter_count(text, letters=string.ascii_letters):
#     """Return the number characters in text according to `letters`.

#     The string document refers to
#     https://docs.python.org/2/library/string.html
#     """

#     letters = frozenset(letters)
#     count = 0
#     for char in text:
#         if char in letters:
#             count += 1

#     return count

# print(letter_count(r'Adsf[]\$%Adf'))
# print(letter_count(r'Adsf[]\$%Adf', string.ascii_lowercase))
# print(letter_count(r'Adsf[]\$%Adf', string.ascii_uppercase))

# # 例3
# # 拆分操作符 *
# def product(*args):
#     result = 1
#     for arg in args:
#         result *= arg
#     return result


# print(product(5, 3, 8))
# print(product(1, 2, 3, 4))

# # 例4 单个*参数
# def heron2(a, b, c, *, units="meterts"):
#     s = (a + b + c) / 2
#     area = math.sqrt(s * (s - a) * (s - b) * (s - c))
#     return "{0} {1}".format(area, units)

# print(heron2(25, 24, 7))
# print(heron2(41, 9, 40, units='inches'))
# print(heron2(41, 9, 40, 'inches'))

# # 例5 关键参数跟在位置参数之后
# def sum_of_powers(*args, power=1):
#     result = 0
#     for arg in args:
#         result += arg**power
#     return result

# print(sum_of_powers(1, 2, 4))
# print(sum_of_powers(1, 2, 4, power=2))

# 例6
# def print_setup(*,paper="Letter", copies=1, color=False)
# def print_setup()
# def print_setup(paper="A4", color=True)
# def print_setup("A4") # Error

# # 例7 映射拆分操作 **, 对字典映射拆分
# options = dict(paper="A4", color=True)

# def showoptions(**options):
#     for key in options:
#         print(key, options[key])

# showoptions(**options)

# # 例8
# def add_person_details(ssn, surname, **kwargs):
#     print("SSN = ", ssn)
#     print("surname = ", surname)
#     for key in sorted(kwargs):
#         print("  {0} = {1}".format(key, kwargs[key]))

# add_person_details(123, "Mike", forename="Lexis", age=47)
# add_person_details(123, "Mike", forename="Lexis", age=47, gender='male')

# # 例9
# def print_args(*args, **kwargs):
#     for i, arg in enumerate(args):
#         print("位置参数 {0} = {1}".format(i, arg))

#     for key in kwargs:
#         print("关键字参数 {0} = {1}".format(key, kwargs[key]))

# print_args("a", "b", "c", "ABCD", a=1, b=2, c=3, name='abc')

# 例10 Lambda函数lambda parameters:
# expression parameters是由逗号分隔的变量
# 作为位置参数expression不能包含分支或循环(但允许使用条件表达式)
# 也不能包含return语句

# x = 1
# s = lambda x: "" if x == 1 else "s"
# print("{0} file{1} processed".format(1, s(1)))
# print("{0} file{1} processed".format(2, s(2)))

# elements = [(2, 12, 'Mg'), (1, 3, 'Li'), (3, 4, 'Be')]
# print(sorted(elements))
# print(sorted(elements, key=lambda e: e[1]))
# print(sorted(elements, key=lambda e: e[2]))
