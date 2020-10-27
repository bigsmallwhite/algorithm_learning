#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   21-迭代生成器列表降维.py
@Time    :   2020/10/27 20:27:18
@Author  :   Dll 
@Contact :   dengll1783600@foxmail.com
@Desc    :   利用生成器对嵌套列表降维
'''

# here put the import lib
'''
# 递归生成器，把多维列表转换为一维列表
lst = [4,[1,2,[3,5,6]],[4,3,[1,2,[4,5]],2],[1,2,4,5,7]]
'''
from typing import Type


def solution1(lst):
    try:
        for sublst in lst:
            for element in solution1(sublst):
                yield element
    except TypeError:
        yield lst

def solution2(lst):
    for sublst in lst:
        if not isinstance(sublst, list):
            yield sublst
        else:
            for ele in solution2(sublst):
                yield ele

if __name__ == '__main__':
    lst = [4,[1,2,[3,5,6]],[4,3,[1,2,[4,5]],2],[1,2,4,5,7]]
    for i in solution2(lst):
        print(i)