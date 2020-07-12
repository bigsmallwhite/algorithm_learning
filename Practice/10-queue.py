#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   10-queue.py
@Time    :   2020/07/12 00:36:04
@Author  :   Dll 
@Contact :   dengll1783600@foxmail.com
@Desc    :   None
'''

# here put the import lib

class Queue(object):
    """队列"""
    def __init__(self):
        """用顺序表来存储数据,list尾进头出"""
        self.__list = []

    def inqueue(self, item):
        """队列里添加一个元素"""
        self.__list.append(item)

    def dequeue(self):
        """队列里弹出一个元素"""
        return self.__list.pop(0)

    @property
    def is_empty(self):
        """判断队列是否为空"""
        return not bool(self.__list)

    def size(self):
        """返回队列的大小"""
        return len(self.__list)


if __name__ == '__main__':
    q = Queue()
    q.inqueue(1)
    q.inqueue(5)
    q.inqueue(7)
    print(q.is_empty)
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
