#! /usr/bin/env python3
# -*- coding: utf-8 -*-
"""
模块
- 模块就是一个py文件包含的函数和类

"""
"""
导入模块

import importable

import importable1, ..., importableN

import importable as preferred_name

from importable import object as preferred_name

from importable import objec1, object2, ...,objectN

from importable import objec1, object2, object3,
   object4, ...,objectN

from importable import *
"""

import os
import os.path as path
from os import path as mypath
from os.path import basename
import sys

print(os.path.basename(__file__))
print(path.basename(__file__))
print(mypath.basename(__file__))
print(basename(__file__))

# 搜索模块的路径列表
print(sys.path)

# 包(package)
#
# 包是一个目录
# 包 = 一组模块 + `__init__.py`
# 例：
#
# Graphics/
#    __init__.py
#    Bmp.py
#    Jpeg.py
#    Png.py
#    Tiff.py
#    Vector/
#       __init__.py
#       Eps.py
#       Svg.py

# 例1
# import Graphics.Bmp
# import Graphics.Jpeg as jpeg
# import Graphics.Vector.Svg as svg

# 相对路径
# `.`表示跨越一层目录

# 例2
# Svg.py
# import ..Graphics import Png

# 解释 __name__
# Python在执行.py文件时，会为这个文件创建一个名为__name__的变量
# 并将其设置为`__main__`。
# 因此，如果将一个.py文件视为主程序时，可以在文件中的主程序代码放在
# 一个分支判断结构中
#
# if __name__ == '__main__':
#     主程序代码
#
# 这种方式使得一个模块被别的代码导入时，并不执行分支判断结构这部分内容
#
