#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   disk_usage.py
@Time    :   2020/07/01 00:35:01
@Author  :   Dll 
@Contact :   dengll1783600@foxmail.com
@Desc    :   递归遍历磁盘空间和目录
'''

# here put the import lib

import os

def diskUsage(path):
    '''
    递归遍历文件夹目录
    '''
    total = os.path.getsize(path)
    if os.path.isdir(path):
        for filename in os.listdir(path):
            childpath = os.path.join(path, filename)
            total += diskUsage(childpath)
    print('{0:<10}'.format(total), path)
    return total

diskUsage(r'C:\code\spyder')