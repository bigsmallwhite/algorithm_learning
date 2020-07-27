#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   14-findBigSmall.py
@Time    :   2020/07/25 09:31:21
@Author  :   Dll 
@Contact :   dengll1783600@foxmail.com
@Desc    :   递归查找数组的最大值和最小值
'''

# here put the import lib
class Findbigsmall(object):

    def findbig(self, lst):
        if len(lst) == 1:
            return lst[0]
        else:
            return max(lst[0], self.findbig(lst[1:]))
    
    def findsmall(self, lst):
        if len(lst) == 1:
            return lst[0]
        else:
            return min(lst[0], self.findsmall(lst[1:]))


if __name__ == '__main__':

    lst = [1, 3, 4, 2, 7, 8, 5]
    f = Findbigsmall()
    print(f.findbig(lst))
    print(f.findsmall(lst))
    