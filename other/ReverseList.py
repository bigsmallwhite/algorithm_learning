#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   ReverseList.py
@Time    :   2020/07/02 22:34:37
@Author  :   Dll 
@Contact :   dengll1783600@foxmail.com
@Desc    :   None
'''

# here put the import lib
# 翻转列表

def reverseList(data, start, stop):
    while start < stop -1:
        data[start], data[stop] = data[stop], data[start]
        start += 1
        stop -= 1
        # reverseList(data, start, stop)

lst = list('1234567890')
reverseList(lst, 0, len(lst)-1)
print(lst)
