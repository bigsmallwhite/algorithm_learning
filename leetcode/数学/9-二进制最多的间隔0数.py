#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   9-二进制最多的间隔0数.py
@Time    :   2020/10/17 00:28:05
@Author  :   Dll 
@Contact :   dengll1783600@foxmail.com
@Desc    :   求一个整数二进制下两个1之间最多相隔多少个0
'''

# here put the import lib
'''
5的二进制： 101，返回1
3的二进制：  11，返回0
9的二进制：1001，返回2
求一个整数二进制下两个1之间最多相隔多少个0
思路：记录'1'的位置，求差的最大值
思路一：先求二进制，然后一次遍历
思路二：直接位运算
'''

class Solution():
    # 遍历
    def method1(self, num):
        # 内置函数bin，返回'0b'+'010010010010'
        bin_ = bin(num)[2:]
        max_ = 0
        pre = 0
        for i in range(len(bin_)):
            if bin_[i] == '1':
                max_ = max(max_, i-pre-1)
                pre = i
        return max_

    # 位运算
    def method2(self, num):
        pre = -1
        step = 1
        max_ = 0
        while num > 0:
            if num & 1 == 1:
                if pre == -1:
                    pre = step
                else:
                    max_ = max(max_, step-pre-1)
                    pre = step
            step += 1
            num >>= 1
        return max_

if __name__ == '__main__':
    s = Solution()
    print(s.method1(9))
    print(s.method2(9))

