#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   18-绕圈圈打印整数.py
@Time    :   2020/10/11 21:13:55
@Author  :   Dll 
@Contact :   dengll1783600@foxmail.com
@Desc    :   实现绕圈圈打印顺序整数
'''

# here put the import lib
'''
要求实现如下的顺序整数：
01 12 11 10
02 13 16 09
03 14 15 08
04 05 06 07

思路：主要的问题是解决方向的转换问题
size:边长
n：行；m：列
1、左下到右上的对角线方向：n+m = size-1
    如果在左下角，需要变向（向下->向右）
    如果在右上角，需要变向（向上->向左）
2、右下到左上的对角线方向：n == m and m >= size/2
    在右下角，需要变向（向右->向上）
3、左上的变向在[12,16,08]方向上：n = m-1 and m <= size/2
    在左上角，需要变向（向左->向下）
四个变向确定好后，然后确定不同方向下的n和m变化：
orient=0：向下，n += 1
orient=1：向右，m += 1
orient=2：向上，n -= 1
orient=3：向左，m -= 1
'''
def solution(size):
    array = [[0] * size]
    for i in range(size-1):
        array += [[0] * size]
    # 这地方array空列表的生成需要注意
    # 如果采用列表生成式[[] for i in range(n)]或者[] * n
    # 那么每个子列表都是浅拷贝，一变都变
    orient = 0 # orient控制方向，0代表向下，1代表向右，2代表向上，3代表向左
    n = 0; m = 0 # n控制行，m控制列
    for i in range(1, size*size+1):
        array[n][m] = i
        if n+m == size-1: # 左下到右上对角线
            if n > m: # 左下角
                orient = 1           
            else: # 右上角
                orient = 3
        elif (n == m) and (n >= size/2): # 右下角
            orient = 2    
        elif (n == m-1) and (m <= size/2): # 左上角
            orient = 0        
        
        if orient == 0:
            n += 1
        if orient == 1:
            m += 1
        if orient == 2:
            n -= 1
        if orient == 3:
            m -= 1