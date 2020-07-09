#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   binary_search.py
@Time    :   2020/06/30 00:13:40
@Author  :   Dll 
@Contact :   dengll1783600@foxmail.com
@Desc    :   None
'''
# here put the import lib

lst = [1, 3, 4, 7, 21, 34, 57, 68, 97]

def binarySearch(data, target):
    '''
    有序数组中的二分法，按照前闭后开"[)"的方式查找
    end 取数组的长度
    begin 取0
    方便直接计算中间数组的个数（end-begin）
    '''
    length = len(data)
    begin = 0
    end = length
    while begin < end:
        middle = (begin + end) // 2
        if target > data[middle]:
            begin = middle + 1
        elif target < data[middle]:
            end = middle
        else:
            return data[middle]
    return None


if __name__ == '__main__':
    print(binarySearch(lst, 7))