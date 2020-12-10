#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   5-二进制求和.py
@Time    :   2020/12/10 16:26:39
@Author  :   Dll 
@Contact :   dengll1783600@foxmail.com
@Desc    :   返回两个二进制字符串的和（二进制形式）
'''

# here put the import lib
'''
给你两个二进制字符串，返回它们的和（用二进制表示）。
输入为 非空 字符串且只包含数字 1 和 0。

示例 1:
输入: a = "11", b = "1"
输出: "100"

示例 2:
输入: a = "1010", b = "1011"
输出: "10101"

思路一：内置函数，先转化为十进制，相加，再转化为二进制
思路二：遍历，先用0补全较小的数，设置一个临时变量记录进位
'''

class Solution:
    # python的内置函数
    def addBinaary1(self, a: str, b: str) -> str:
        return bin(int(a, 2) + int(b, 2))[2:]

    # 遍历进位
    def addBinary2(self, a: str, b: str) -> str:
        # 先补全较小的数，在前面加上0
        if len(a) != len(b):
            if len(a) > len(b):
                b = '0'*(len(a)-len(b)) + b
            else:
                a = '0'*(len(b)-len(a)) + a
        n = len(a)
        result = ''
        # temp是记录是否需要进位
        temp = 0
        for i in range(n-1, -1, -1):
            sum_ = int(a[i]) + int(b[i])
            if sum_ == 0:
                result += str(temp)
                temp = 0
            if sum_ == 1:
                if temp == 0:
                    result += '1'
                else:
                    result += '0'
                    temp = 1
            if sum_ == 2:
                if temp == 0:
                    result += '0'
                    temp = 1
                else:
                    result += '1'
                    temp = 1
        if temp == 1:
            result += '1'
        return result[::-1]