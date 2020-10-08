#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   1-最长公共前缀.py
@Time    :   2020/10/08 22:23:34
@Author  :   Dll 
@Contact :   dengll1783600@foxmail.com
@Desc    :   求多个字符串最长公共前缀
'''

# here put the import lib
'''
编写一个函数来查找字符串数组中的最长公共前缀。
如果不存在公共前缀，返回空字符串 ""。

示例 1:
输入: ["flower","flow","flight"]
输出: "fl"
示例 2:
输入: ["dog","racecar","car"]
输出: ""
解释: 输入不存在公共前缀。
说明:
所有输入只包含小写字母 a-z 。

思路一：利用python的zip函数，对共同长度的字符串进行打包
然后对每个打包的元组进行set去重，如果长度为1就相同，不为1就说明当前位置的元素不同，return
思路二：先求出最短的字符串，然后每个字符对比是否全部相同
'''

class Solution:
    # python的zip函数
    def longestCommonPrefix1(self, strs) -> str:
        # zip(*lst) 是把列表内的所有元素zip
        strs = list(map(set, zip(*strs)))
        res = ''
        for i in strs:
            if len(i) > 1:
                break
            res += list(i)[0]
        return res

    # 暴力
    def longestCommonPrefix2(self, strs) -> str:
        n = len(strs)
        if n == 0:
            return ""
        if n == 1:
            return strs[0]
        min_n = len(strs[0])
        for i in strs:
            min_n = min(min_n, len(i))
        for i in range(min_n):
            for j in strs:
                if j[i] != strs[0][i]:
                    return strs[0][:i]
        return strs[0][min_n-1]

if __name__ == '__main__':
    strs = ["flower","flow","flight"]
    s = Solution()
    print(s.longestCommonPrefix2(strs))