#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   PowerX.py
@Time    :   2020/07/02 23:48:21
@Author  :   Dll 
@Contact :   dengll1783600@foxmail.com
@Desc    :   优化m的n次方
'''

# here put the import lib
# 思路一：
    # 递归计算幂方，二分优化，2^6 = 2^3*2^3,故可以二分求幂
# 思路二：
    # 位运算，把n转成二进制，如n=9，——>1001，求m的9次方，
    # 即m^9 = m^1000 * m^0001，所以只需要把是1的乘数累积到结果中
    # 如2^9，拆分为1000,0001（8,1）


def powerX1(x, n):
    if n == 0:
        return 1
    else:
        temp = powerX1(x, n//2)
        result = temp * temp
        if n % 2 == 1:
            result *= x
        return result

def powerX2(x, n):
    result = 1
    temp = x
    while n != 0:
        if n & 1 == 1:
            result *= temp
        temp *= temp
        n >>= 1
    return result


if __name__ == '__main__':
    
    print(powerX1(2, 5))
    print(powerX2(2, 10))