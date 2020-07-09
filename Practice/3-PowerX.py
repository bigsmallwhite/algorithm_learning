#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   PowerX.py
@Time    :   2020/07/02 23:48:21
@Author  :   Dll 
@Contact :   dengll1783600@foxmail.com
@Desc    :   None
'''

# here put the import lib
# 递归计算幂方，二分优化，2^6 = 2^3*2^3,故可以二分求幂


def powerX(x, n):
    if n == 0:
        return 1
    else:
        temp = powerX(x, n//2)
        result = temp * temp
        if n % 2 == 1:
            result *= x
        return result


print(powerX(2, 5))