#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   SingleLink.py
@Time    :   2020/07/01 21:39:47
@Author  :   Dll
@Contact :   dengll1783600@foxmail.com
@Desc    :   None
'''
# here put the import lib


class Node(object):
    """节点"""
    def __init__(self, element):
        self.element = element
        self.next = None
        

class SingleLinkList(object):
    """单链表"""
    def __init__(self, node=None):
        self.head = node

    @property
    def is_empty(self):
        """列表是否为空"""
        return self.head is None

    @property
    def length(self):
        """链表长度"""
        # cur 游标，记录当前的指针
        cur = self.head
        # count 计数
        count = 0
        while cur:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        """遍历整个列表"""
        cur = self.head
        while cur:
            print(cur.element, end=' ')
            cur = cur.next
        print('\r')

    def add(self, item):
        """链表头部添加元素"""
        node = Node(item)
        if self.is_empty:
            self.head = node
        else:
            node.next = self.head
            self.head = node


    def append(self, item):
        """链表尾部添加元素"""
        node = Node(item)
        if self.is_empty:
            self.head = node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = node

    def insert(self, position, item):
        """在指定位置插入元素"""
        node = Node(item)
        scale = self.length
        if position < 0:
            position = scale + position
        # 链表为空
        if scale == 0:
            self.head = node
            return
        # 插入首位
        if position == 0:
            self.add(item)
        else:
            cur = self.head
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
        cur = self.head
        count = 0
        while cur:
            if cur.element == item:
                return count
            else:
                cur = cur.next
                count += 1
        return None

    def remove(self, item):
        """删除元素"""
        cur = self.head
        pre = None
        count = 0
        while cur:
            if cur.element == item:
                # 判断是否为头节点
                if cur == self.head:
                    self.head = cur.next
                else:
                    pre.next = cur.next
                return (count, item)
            else:
                count += 1
                pre = cur
                cur = cur.next
        return False

if __name__ == '__main__':
    
    sll = SingleLinkList()
    print(f'链表是否为空:{sll.is_empty}')
    print(f'链表长度:{sll.length}')
    sll.append(1)
    sll.append(2)
    sll.append(3)
    sll.append(4)
    sll.append(5)
    sll.append(6)
    sll.add(10)
    sll.insert(1, 100)
    sll.insert(7, 100)
    sll.insert(0, 1000000)
    sll.insert(-1, 1000000)
    sll.travel()
    print(f'链表是否为空:{sll.is_empty}')
    print(f'链表长度:{sll.length}')
    print(f'{6}查询结果{sll.search(6)}')
    print(f'{15}查询结果{sll.search(15)}')
    print(sll.remove(1))
    sll.travel()


