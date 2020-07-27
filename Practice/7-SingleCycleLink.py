#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   SingleCycleLink.py
@Time    :   2020/07/05 01:19:08
@Author  :   Dll 
@Contact :   dengll1783600@foxmail.com
@Desc    :   实现循环列表
'''

# here put the import lib
class Node(object):
    """节点"""
    def __init__(self, element):
        self.element = element
        self.next = None

class SingleCycleLinkList(object):
    """单向循环链表"""
    def __init__(self, node=None):
        self.__head = node
        if node:
            node.next = node
    
    @property
    def is_empty(self):
        """列表是否为空"""
        return self.__head == None

    @property
    def length(self):
        """链表长度"""
        # 判断是否为空
        if self.is_empty:
            return 0
        # cur 游标，记录当前的指针
        cur = self.__head
        # count 计数
        count = 1
        while cur.next != self.__head:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        """遍历整个列表"""
        cur = self.__head
        while cur:
            print(cur.element, end=' ')
            if cur.next == self.__head:
                break
            cur = cur.next
        print('\r')

    def add(self, item):
        """链表头部添加元素"""
        node = Node(item)
        if self.is_empty:
            self.__head = node
            node.next = node
        else:
            cur = self.__head
            while cur.next != self.__head:
                cur = cur.next
            node.next = self.__head
            self.__head = node
            cur.next = node

    def append(self, item):
        """链表尾部添加元素"""
        node = Node(item)
        if self.is_empty:
            self.__head = node
            node.next = node
        else:
            cur = self.__head
            while cur.next != self.__head:
                cur = cur.next
            cur.next = node
            node.next = self.__head

    def insert(self, position, item):
        """在指定位置插入元素"""
        node = Node(item)
        scale = self.length
        if position < 0:
            position = scale + position
        # 链表为空
        if scale == 0:
            self.__head = node
            node.next = node
            return
        # 插入首位
        if position == 0:
            self.add(item)
        else:
            cur = self.__head
            # 插入位置大于链表长度，直接放入尾部
            if position > scale - 1:
                self.append(item)
            # 插入链表中间
            else:
                count = 0
                while count < position-1:
                    count += 1
                    cur = cur.next
                node.next = cur.next
                cur.next = node

    def search(self, item):
        """查找元素"""
        cur = self.__head
        count = 0
        if self.is_empty:
            return None
        while cur.next != self.__head:
            if cur.element == item:
                return count
            else:
                cur = cur.next
                count += 1
        if cur.element == item:
            return count
        return None
    
    def remove(self, item):
        """删除元素"""
        cur = self.__head
        pre = None
        count = 0
        if self.is_empty:
            return None
        while cur.next != self.__head:
            if cur.element == item:
                # 判断是否为头节点
                if cur == self.__head:
                    # 删除头结点，需要找到尾节点
                    temp = self.__head
                    while temp.next != self.__head:
                        temp = temp.next
                    self.__head = cur.next
                    temp.next = self.__head
                # 中间节点
                else:
                    pre.next = cur.next
                return (count, item)
            else:
                count += 1
                pre = cur
                cur = cur.next
        # 退出循环，cur指向尾节点
        if cur.element == item:
            if cur == self.__head:
                self.__head = None
                return (0, item)
            else:
                pre.next = cur.next
                return (count, item)
        return None

if __name__ == '__main__':
    
    scll = SingleCycleLinkList()
    print(f'链表是否为空:{scll.is_empty}')
    print(f'链表长度:{scll.length}')
    scll.append(1)
    scll.append(2)
    scll.append(3)
    scll.append(4)
    scll.append(5)
    scll.append(6)
    scll.add(10)
    print(scll.search(10))
    print(scll.search(6))
    scll.insert(1, 100)
    scll.insert(7, 100)
    scll.insert(0, 1000000)
    scll.insert(-1, 1000000)
    scll.travel()
    print(scll.remove(1000000))
    print(f'链表是否为空:{scll.is_empty}')
    print(f'链表长度:{scll.length}')
    # print(f'{6}查询结果{scll.search(6)}')
    # print(f'{15}查询结果{scll.search(15)}')
    # print(scll.remove(1))
    scll.travel()