#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   15-hanoiTower.py
@Time    :   2020/07/28 00:00:47
@Author  :   Dll 
@Contact :   dengll1783600@foxmail.com
@Desc    :   汉诺塔问题
'''

# here put the import lib

def hanoi(n, a, b, c):
    if n == 1:  # 如果只有一片，直接移动到c
        print(a, '-->', c)
    else:
        hanoi(n-1, a, c, b)  # 先把上面的n-1片移动到b
        print(a, '-->', c)   # 再把下面的最后一片移动到c
        hanoi(n-1, b, a, c)  # 最后把b上的n-1片移动到c


if __name__ == '__main__':
    hanoi(5, 'a', 'b', 'c')