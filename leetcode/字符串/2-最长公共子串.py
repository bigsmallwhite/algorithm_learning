#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   2-最长公共子串.py
@Time    :   2020/10/14 00:12:55
@Author  :   Dll 
@Contact :   dengll1783600@foxmail.com
@Desc    :   查找两个字符串的最大公共子串
'''

# here put the import lib
'''
公共子串必须是连续的子串
a = 'abcd'
b = 'abdc'
最大的公共子串：'ab'

思路一：动态规划，dp[i][j] 表示 A 中前 i 个数字和 B 中前 j 个数字中最长子数组的长度
判断 A[i]==B[j], 相等的话在 dp[i-1][j-1] 的基础上 + 1
否则的话，dp[i][j] = 0

思路二：滑动窗口，

思路三：起点加长度
'''



        

if __name__ == '__main__':
    str1 = 'abcd'
    str2 = 'abdc'
    print(solution1(str1, str2))