#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   11-Dqueue.py
@Time    :   2020/07/12 12:25:35
@Author  :   Dll 
@Contact :   dengll1783600@foxmail.com
@Desc    :   None
'''

# here put the import lib

class Dqueue(object):
    """双端队列"""
    def __init__(self):
        self.__list = []

    def add_front(self, item):
        """列表头部添加一个元素"""
        self.__list.insert(0, item)
    
    def add_rear(self, item):
        """列表尾部添加一个元素"""
        self.__list.append(item)

    def remove_front(self):
        """列表头部添加一个元素"""
        self.__list.pop(0)

    def remove_rear(self):
        """列表尾部添加一个元素"""
        self.__list.pop()
    
    def peek_front(self):
        """返回队列的头部元素"""
        return self.__list[0]
    
    def peek_rear(self):
        """返回队列的尾部元素"""
        return self.__list[-1]
    
    @property
    def is_empty(self):
        """判断队列是否为空"""
        return not bool(self.__list)

    def size(self):
        """返回双端队列的大小"""
        return len(self.__list)

if __name__ == '__main__':
    dq = Dqueue()
    dq.add_front(1)
    dq.add_rear(10)
    print(dq.is_empty)
    print(dq.size())
    dq.add_front(100)
    dq.add_rear(105)
    dq.add_front(120)
    print(dq.peek_front())
    print(dq.peek_rear())
    print(dq.size())