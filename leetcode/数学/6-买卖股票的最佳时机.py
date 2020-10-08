#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   6-买卖股票的最佳时机.py
@Time    :   2020/10/08 20:08:14
@Author  :   Dll 
@Contact :   dengll1783600@foxmail.com
@Desc    :   求买卖股票的最佳时机
'''

# here put the import lib
'''
给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。
如果你最多只允许完成一笔交易（即买入和卖出一支股票一次），设计一个算法来计算你所能获取的最大利润。
注意：你不能在买入股票前卖出股票。

示例 1:
输入: [7,1,5,3,6,4]
输出: 5
解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格；同时，你不能在买入前卖出股票。
示例 2:
输入: [7,6,4,3,1]
输出: 0
解释: 在这种情况下, 没有交易完成, 所以最大利润为0。

思路一：暴力，只需要求出每个元素的最大差值，时间复杂度O(n^2)
思路二：动态规划，时间复杂度O(n)，遍历到当前元素时，
只需要判断 当前元素和前面最小值的差值 与 前面所有元素最小值的大小即可
(max(dp[n-1], nums[n]-min(nums[:n-2])))
'''

class Solution:
    # 暴力求解
    def maxProfit1(self, prices) -> int:
        n = len(prices)
        if n <= 1:
            return 0
        max_p = 0
        for i in range(n):
            for j in range(1+1, n):
                max_p = max(max_p, prices[j]-prices[i])
        return max_p
    
    # 动态规划
    def maxProfit2(self, prices) -> int:
        n = len(prices)
        if n <= 1:
            return 0
        dp = [0] * n
        dp[1] = prices[1] - prices[0]
        min_ele = min(prices[:2])
        for i in range(2, n):
            dp[i] = max(dp[i-1], prices[i]-min_ele)
            min_ele = min(min_ele, prices[i])
        if dp[n-1] < 0:
            return 0
        else:
            return dp[n-1]

if __name__ == '__main__':
    prices = [7,1,5,3,6,4]
    s = Solution()
    print(s.maxProfit2(prices))
    

