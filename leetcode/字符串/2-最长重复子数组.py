#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   2-最长重复子数组.py
@Time    :   2020/10/14 00:12:55
@Author  :   Dll 
@Contact :   dengll1783600@foxmail.com
@Desc    :   查找两个数组中公共的长度最长的子数组的长度
'''

# here put the import lib
'''
给两个整数数组 A 和 B ，返回两个数组中公共的、长度最长的子数组的长度。
示例：
输入：
A: [1,2,3,2,1]
B: [3,2,1,4,7]
输出：3
解释：
长度最长的公共子数组是 [3, 2, 1] 。
&&&&&&&&&&&&&&&&
公共子串必须是连续的子串
a = 'abcd'
b = 'abdc'
最大的公共子串：'ab'

最长公共子数组与最长公共子串是一样的

思路一：动态规划，dp[i][j] 表示 A 中前 i 个数字和 B 中前 j 个数字中最长子数组的长度
判断 A[i]==B[j], 相等的话在 dp[i-1][j-1] 的基础上 + 1
否则的话，dp[i][j] = 0

思路二：滑动窗口，

思路三：切片，起点加长度，利用字符串的in来判断切片是否在另一个字符串中，
如果在，就增大切片长度，起点不变；如果不在，就增大起点位置，切片长度不变
'''

class Solution:
    # 动态规划
    def findLength1(self, A, B) -> int:
        m, n = len(A), len(B)
        dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
        if m == 0 or n == 0: return 0
        max_ = 0
        for i in range(1, m+1):
            for j in range(1, n+1):
                if A[i-1] == B[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                    max_ = max(max_, dp[i][j])
        return max_


    
if __name__ == '__main__':
    nums1 = [1,2,3,2,1]
    nums2 = [3,2,1,4,7]
    s = Solution()
    print(s.findLength1(nums1, nums2))