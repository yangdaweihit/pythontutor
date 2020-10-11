#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from package import module
from package.base import basemodule

# print(basemodule.a)
# module.foo()
# basemodule.foo()

mydict = {'6': [1, 2, 3], '8': [5, 6, 7]}

for key in mydict:
    val = mydict[key]
    for iv in val:
        print(iv)
