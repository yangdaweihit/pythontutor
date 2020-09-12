# a = 321
# b = 12
# print(a + b)    # 333
# print(a - b)    # 309
# print(a * b)    # 3852
# print(a / b)    # 26.75

# True
# False

# # sequence
# list
# tuple
# dict
# set

# numpy
# scipy
# matploblib
# pandas
# a = 100
# b = 12.345
# c = 1 + 5j
# d = 'hello, world'
# e = True
# b = str(a)
# print(type(str(a)))    # <class 'int'>
# print(type(b))    # <class 'float'>
# print(type(c))    # <class 'complex'>
# print(type(d))    # <class 'str'>
# print(type(int(d)))    # <class 'str'>
# print(type(e))    o# <class 'bool'>
"""
a = float(input('a = '))
b = float(input('b = '))
print('%d + %d = %d' % (a, b, a + b))
print('{2:>5.3f} = {1:>8.3f}+ {0:>8.3f}'.format(a, b, a + b))
print('%d - %d = %d' % (a, b, a - b))
print('%d * %d = %d' % (a, b, a * b))
print('%d / %d = %f' % (a, b, a / b))
print('%d // %d = %d' % (a, b, a // b))
print('%d %% %d = %d' % (a, b, a % b))
print('%d ** %d = %d' % (a, b, a ** b))
"""

# a = 10
# b = 3
# a += b        # 相当于：a = a + b
# a *= a + 2    # 相当于：a = a * (a + 2)
# print(a)      # 算一下这里会输出什么
"""
将华氏温度转换为摄氏温度

Version: 0.1
Author: 骆昊
"""
f = float(input('请输入华氏温度: '))
c = (f - 32) / 1.8
print('%.1f华氏度 = %.1f摄氏度' % (f, c))