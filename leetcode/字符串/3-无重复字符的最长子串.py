#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   3-无重复字符的最长子串.py
@Time    :   2020/10/20 11:25:29
@Author  :   Dll 
@Contact :   dengll1783600@foxmail.com
@Desc    :   求字符串的最长无重复子串
'''

# here put the import lib
'''
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。

示例 1:
输入: "abcabcbb"
输出: 3 

示例 2:
输入: "bbbbb"
输出: 1

示例 3:
输入: "pwwkew"
输出: 3

思路一：暴力，以每个元素为开头，遍历，加入到set中，如果重复就记录长度，然后break

思路二：滑动窗口，构造一个hash表，
遍历元素，如果不在hash中，就添加，如果在，就更新left的值
'''

class Solution:
    # 暴力解决，O(n^2)
    def lengthOfLongestSubstring1(self, s: str) -> int:
        n = len(s)
        res = 0
        for i in range(n):
            temp = set(s[i])
            mid_res = 1
            for j in range(i+1, n):
                if s[j] not in temp:
                    temp.add(s[j])
                    mid_res += 1
                else:
                    break
            res = max(res, mid_res)
        return res

    # 滑动窗口
    def lengthOfLongestSubstring2(self, s: str) -> int:
        dic = {}
        res = 0
        left = 0
        for right, value in enumerate(s):
            if value in dic:
                left = max(dic[value], left)
            dic[value] = right + 1
            res = max(res, right-left+1) 
        return res

if __name__ == '__main__':
    string = "bbbbc"
    s = Solution()
    print(s.lengthOfLongestSubstring1(string))