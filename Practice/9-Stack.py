#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   9-Stack.py
@Time    :   2020/07/09 23:30:05
@Author  :   Dll 
@Contact :   dengll1783600@foxmail.com
@Desc    :   None
'''

# here put the import lib

class Stack(object):
    """
    采用顺序表实现栈
    """
    def __init__(self):
        self.__list = []

    def push(self, item):
        """添加一个新的元素"""
        self.__list.append(item)    # 尾部作为栈入口
        # self.__list.insert(0, item)    # 头部作为栈入口

    def pop(self):
        """弹出栈顶元素"""
        if self.__list:
            return self.__list.pop()
        else:
            return None

    def peek(self):
        """返回栈顶元素"""
        if self.__list:
            return self.__list[-1]
        else:
            return None

    def is_empty(self):
        """判断是否为空"""
        if self.__list:
            return False
        else:
            return True
        # return self.__list == []

    def size(self):
        """返回栈的元素个数"""
        return len(self.__list)

if __name__ == '__main__':
    
    s = Stack()
    s.push(1)
    s.push(5)
    s.push(7)
    print(s.pop())
    print(s.pop())
    print(s.pop())