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
# 思路一：
    # 递归计算幂方，二分优化，2^6 = 2^3*2^3,故可以二分求幂
# 思路二：
    # 位运算，把n转成二进制，如n=9，——>1001，求m的9次方，
    # 即m^9 = m^1000 * m^0001

def powerX1(x, n):
    if n == 0:
        return 1
    else:
        temp = powerX(x, n//2)
        result = temp * temp
        if n % 2 == 1:
            result *= x
        return result


print(powerX1(2, 5))