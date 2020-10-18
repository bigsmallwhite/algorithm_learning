#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   20-迭代器.py
@Time    :   2020/10/18 23:15:44
@Author  :   Dll 
@Contact :   dengll1783600@foxmail.com
@Desc    :   实现python的迭代器
'''

# here put the import lib
'''
python的迭代器包括__iter__和__next__方法
实现1，1+2，1+2+3，1+2+3+4，……
'''
class Test(object):
    def __init__(self, n):
        self.n = n
        self.cur = 1
    def __next__(self):
        if self.cur > self.n:
            raise StopIteration
        res = 0
        for i in range(1, self.cur+1):
            res += i
        self.cur += 1
        return res
    def __iter__(self):
        return self

if __name__ == '__main__':
    n = 5
    t = Test(n)
    for i in t:
        print(i)
