#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   7-整数反转.py
@Time    :   2020/10/08 17:05:07
@Author  :   Dll 
@Contact :   dengll1783600@foxmail.com
@Desc    :   实现整数反转
'''

# here put the import lib
'''
则其数值范围为 [−2^31,  2^31−1]。请根据这个假设，如果反转后整数溢出那么就返回 0。
思路一：字符串反转
思路二：数学计算
'''

class Solution():
    # 字符串反转
    def solution1(self, x):
        lst = list(str(abs(x)))
        res = int(''.join(lst[::-1]))
        if x >= 0 and res <= (2**31-1):
            return res
        elif x < 0 and res <= 2**31:
            return -res
        else:
            return 0
    # 数学计算
    def solution2(self, x):
        num = abs(x)
        res = 0
        while num > 0:
            temp = num % 10
            res = res*10 + temp
            num //= 10
        if x >= 0 and res <= (2**31-1):
            return res
        elif x < 0 and res <= 2**31:
            return -res
        else:
            return 0

