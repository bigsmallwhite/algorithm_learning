#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   7-每日温度.py
@Time    :   2020/10/19 23:22:33
@Author  :   Dll 
@Contact :   dengll1783600@foxmail.com
@Desc    :   求第一个高于当前温度的天数
'''

# here put the import lib
'''
根据每日 气温 列表，重新生成一个列表。
对应位置的输出为：要想观测到更高的气温，至少需要等待的天数。
如果气温在这之后都不会升高，请在该位置用 0 来代替。

例如，给定一个列表 temperatures = [73, 74, 75, 71, 69, 72, 76, 73]，
你的输出应该是 [1, 1, 4, 2, 1, 1, 0, 0]

思路：单调栈
'''

class Solution:
    def dailyTemperatures(self, lst):
        stack = []
        res = [0] * len(lst)
        for i, n in enumerate(lst):
            while stack and lst[stack[-1]] < n:
                res[stack.pop()] = i - stack[-1]
            stack.append(i)
        return res

if __name__ == '__main__':
    lst = [73, 74, 75, 71, 69, 72, 76, 73]
    s = Solution()
    print(s.dailyTemperatures(lst))