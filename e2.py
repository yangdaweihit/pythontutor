#! /usr/bin/env python3
# -*- coding: utf-8 -*-
"""
异常处理

try:
   try_suite
except expression_group1 as variable1:
   except_suite1
...
except expression_groupN as variableN:
   except_suiteN
...
else:
   else_suite
finally:
   finally_suite
"""


# def devide(a, b):
#     try:
#         res = a /b
#     except ZeroDivisionError as e:
#         print(e)
#     except Exception as e:
#         print(e)

#     return res


# print(devide(1, 2))
# print(devide(1, 0))

# # 例1
# d = range(5)
# print(list(d))

# try:
#     x = d[4]
#     # print(4 / 0)
# except LookupError:
#     print("Lookup error occurred.")
# except ZeroDivisionError:
#     print("Zero division occurred.")
# finally:
#     print("always run here.")
#     # print("通常在这里确保资源被正确释放。")

# # 例2
# def list_find(lst, target):
#     try:
#         index = lst.index(target)
#     except ValueError:
#         index = -1
#     return index

# print(list_find(d, 0))
# print(list_find(d, 100))

# # 例3
# def read_data(filename):
#     lines = []
#     fh = None
#     try:
#         fh = open(filename, encoding='utf8')
#         for line in fh:
#             if line.strip():
#                 lines.append(line)
#                 print(lines)
#     except (IOError, OSError) as err:
#         print(err)
#         return []
#     finally:
#         if fh is not None:
#             fh.close()
#     return lines

# read_data('test.txt')
