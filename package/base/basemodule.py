#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from .. import module

a = 1


def foo():
    print("calling foo in basemodule")
    module.foo()
