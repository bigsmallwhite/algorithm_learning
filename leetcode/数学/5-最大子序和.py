#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   5-最大子序和.py
@Time    :   2020/09/21 01:16:24
@Author  :   Dll 
@Contact :   dengll1783600@foxmail.com
@Desc    :   求一个数组的子序（相连）的最大和
'''

# here put the import lib
'''
给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
示例:
输入: [-2,1,-3,4,-1,2,1,-5,4]
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。

通常我们遍历子串或者子序列有三种遍历方式
1、以某个节点为开头的所有子序列：如 [a]，[a, b]，[ a, b, c] ... 再从以 b 为开头的子序列开始遍历 [b] [b, c]。
2、根据子序列的长度为标杆，如先遍历出子序列长度为 1 的子序列，在遍历出长度为 2 的 等等。
3、以子序列的结束节点为基准，先遍历出以某个节点为结束的所有子序列，因为每个节点都可能会是子序列的结束节点，
因此要遍历下整个序列，如：以 b 为结束点的所有子序列: [a , b] [b]，
以 c 为结束点的所有子序列: [a, b, c] [b, c] [ c ]。


思路一：暴力
1、暴力中的暴力，针对每一个元素，依次计算其不同长度的子序和，O(n^2)，超时……，
其实我们只需要知道所有值的最大值，没必要把所有的子序和都列出来。
2、暴力优化，一次遍历，判断上一个值是否大于0，如果大于零就加上当前元素，然后与上一个最大值比大小；
如果小于0，就记录当前元素。
思路二：动态规划
dp[i] 代表的是前i个元素所组成的连续子数组的最大和
它的状态方程可以理解成，如果dp[i-1]<=0（前i−1 个元素对我们后面没有正的贡献），
所以dp[i]=nums[i], 否则，我们需要把正贡献加到后面去，
也就是dp[i]=dp[i-1]+nums[i]
最后返回max(dp)
'''

class Solution():
    
    # 暴力中的暴力，计算以每一个元素为起点的序列和
    def maxSum1(self, nums):
        maxSum = nums[0]
        length = len(nums)
        for i in range(length):
            temp = []
            tmp = 0
            for j in range(i, length):
                tmp = tmp + nums[j]
                temp.append(tmp)
            maxSum = max(maxSum, max(temp))
        return maxSum
    
    # 暴力优化,一次遍历，实际就是dp的思想
    def maxSum1plus(self, nums):
        length = len(nums)
        temp = nums[0]
        max_ = temp
        for i in range(1, length):
            if temp > 0:
                temp += nums[i]
                max_ = max(max_, temp)
            else:
                temp = nums[i]
                max_ = max(max_, temp)
        return max_

    # python的魅力
    def maxSum1plusplus(self, nums):
        length = len(nums)
        for i in range(1, length):
            nums[i] = nums[i] + max(nums[i-1], 0)
        return max(nums)



        