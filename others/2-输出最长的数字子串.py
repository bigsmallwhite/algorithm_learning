#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   2-输出最长的数字子串.py
@Time    :   2020/12/13 01:14:25
@Author  :   Dll 
@Contact :   dengll1783600@foxmail.com
@Desc    :   在字母和数字的组合字符串中找到最长的数字子串
'''

# here put the import lib
'''
举例：
str_ = 'abc1234bs123456789n312n12312n3n123'
最长的数字子串就是'123456789'

思路：while+for循环，时间复杂度O(n)
'''

def solution(string):
    n = len(string)
    result = []
    i = 0
    while i < n:
        if string[i].isdigit():
            temp = string[i]
            for j in range(i+1, n):
                # 判断字符是否为数字，可以用str的内置函数isdigit()
                # 或者用ascii码ord()
                # 48～57为0到9十个阿拉伯数字；65～90为26个大写英文字母；97～122号为26个小写英文字母
                if string[j].isdigit():
                    temp += string[j]
                else:
                    break
            result.append(temp)
            i += len(temp)
        else:
            i += 1
    result.sort(key=len, reverse=True)
    return result[0]

if __name__ == '__main__':
    string = 'abc1234bs123456789n312n12312n3n123'
    print(solution(string))