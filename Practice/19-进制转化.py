#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   19-进制转化.py
@Time    :   2020/10/17 00:11:38
@Author  :   Dll 
@Contact :   dengll1783600@foxmail.com
@Desc    :   实现不同进制之间的转化
'''

# here put the import lib
'''
Python的进制转化可以使用内置函数，也可以使用数学计算
'''

# 内置函数
def solution1():
    # 10 --> 2，结果以'0b'开头
    bin_ = bin(10)
    # 10 --> 8，结果以'0o'开头
    oct_ = oct(10)
    # 10 --> 16，结果以'0x'开头
    hex_ = hex(10)

# 数学计算，任何进制转化
def solution2(num, other):
    res = []
    while num > 0:
        num, rem = divmod(num, other)
        res.append(rem)
    return res[::-1]

print(solution2(10, 2))