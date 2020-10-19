#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   6-下一个更大元素 II.py
@Time    :   2020/10/19 18:29:41
@Author  :   Dll 
@Contact :   dengll1783600@foxmail.com
@Desc    :   求循环列表中下一个更大的元素
'''

# here put the import lib
'''
给定一个循环数组（最后一个元素的下一个元素是数组的第一个元素），输出每个元素的下一个更大元素。
数字 x 的下一个更大的元素是按数组遍历顺序，这个数字之后的第一个比它更大的数，
这意味着你应该循环地搜索它的下一个更大的数。如果不存在，则输出 -1。

示例 1:
输入: [1,2,1]
输出: [2,-1,2]
解释: 第一个 1 的下一个更大的数是 2；
数字 2 找不到下一个更大的数； 
第二个 1 的下一个最大的数需要循环搜索，结果也是 2。

思路：其实是下一个更大元素问题的延伸，只是现在可以循环列表了
处理的方法是把两个数组拼接一起，同时利用求余来处理索引翻倍的问题

'''

class Solution:
    def nextGreaterElements(self, nums):
        duble_nums = nums + nums
        stack = []
        res = [-1] * len(nums)
        for i, n in enumerate(duble_nums):
            i %= len(nums)
            while stack and nums[stack[-1]] < n:
                res[stack.pop()] = n
            stack.append(i)
        return res