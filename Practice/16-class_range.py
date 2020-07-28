#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   16-class_range.py
@Time    :   2020/07/28 23:21:15
@Author  :   Dll 
@Contact :   dengll1783600@foxmail.com
@Desc    :   实现python的range类
'''

# here put the import lib


class Range(object):
    '''
    range class 
    '''
    def __init__(self, start, stop = None, step=1):
        ''' Initialize args'''
        if step == 0:
            raise ValueError('step cannot be 0')
        if stop is None:  # 如果只输入一个数字，默认开始为0
            start, stop = 0, start
        self._length = max(0, (stop-start+step-1)//step)
        self._start = start
        self._step = step
    
    def __len__(self):
        '''Return number of entries in the range '''
        return self._length
    
    def __getitem__(self, k):
        '''Return entry at index k '''
        if k < 0:
            k += self._length
        if not 0 <= k < self._length:
            raise IndexError('index out of range')
        return self._start + k * self._step
    
    
    