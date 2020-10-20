#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   1-字符计数输出.py
@Time    :   2020/10/20 16:17:15
@Author  :   Dll 
@Contact :   dengll1783600@foxmail.com
@Desc    :   把重复的字符计数后输出
'''

# here put the import lib
'''
输入：'aaabbcccd'
输出：'a3b2c3d'
思路：按顺序计数字符的个数，如果不超过1，就只打印字符，超过1，就打印字符和字符数
while + for 
'''

def solution(string):
    dic = {}
    n = len(string)
    if n <= 1:
        return string
    cur = 0
    res = ''
    while cur < n:
        res += string[cur]
        temp = 1
        for i in range(cur+1, n):
            if string[i] == string[cur]:
                temp += 1
            else:
                break
        if temp > 1:
            res += str(temp)
        cur += temp
    return res

if __name__ == '__main__':
    string = 'aaabbc'
    print(solution(string))