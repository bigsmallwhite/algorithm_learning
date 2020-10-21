#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   4-最长上升子序列.py
@Time    :   2020/10/21 15:25:55
@Author  :   Dll 
@Contact :   dengll1783600@foxmail.com
@Desc    :   求一个数组中最长的升序子序列
'''

# here put the import lib
'''
给定一个无序的整数数组，找到其中最长上升子序列的长度。

示例:

输入: [10,9,2,5,3,7,101,18]
输出: 4 
解释: 最长的上升子序列是 [2,3,7,101]，它的长度是 4。

思路：动态规划，dp[i]代表以nums[i]结尾的序列中最长的升序序列长度，
那么状态转移方程为：dp[i] > dp[j](i>j) --> dp[i] = dp[j] + 1
'''

class Solution:
    def lengthOfLIS(self, nums) -> int:
        n = len(nums)
        if n == 0: return 0
        dp = [1] * n
        max_ = dp[0]
        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
            max_ = max(max_, dp[i])
        return max_