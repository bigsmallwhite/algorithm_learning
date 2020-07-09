#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   DoubleLink.py
@Time    :   2020/07/01 21:39:47
@Author  :   Dll
@Contact :   dengll1783600@foxmail.com
@Desc    :   None
'''
# here put the import lib
import SingleLink

class Node(SingleLink.Node):
    """节点"""
    def __init__(self, element):
        super().__init__(element)
        self.pre = None

class DoubleLinkList(SingleLink.SingleLinkList):
    """
    双链表，增加前驱、后置
    其中 判断是否为空、链表长度、遍历、搜索与单链表一致，直接继承即可
    """
    def __init__(self, node=None):
        super().__init__(node)

    def add(self, item):
        """链表头部添加元素"""
        node = Node(item)
        if self.is_empty:
            self.head = node
        else:
            node.next = self.head
            self.head.pre = node
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
            node.pre = cur

    def insert(self, position, item):
        """在指定位置插入元素"""
        node = Node(item)
        scale = self.length
        if position < 0:
            position = scale + position
        if scale == 0:  # 链表为空
            self.head = node
            return
        if position == 0:  # 插入首位
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
                cur.next.pre = node
                cur.next = node
                cur.next.pre = cur

    def remove(self, item):
        """删除元素"""
        cur = self.head
        count = 0
        while cur:
            if cur.element == item:
                # 判断是否为头节点
                if cur == self.head:
                    self.head = cur.next
                    if cur.next:  # 考虑只有一个节点
                        cur.next.pre = None
                else:
                    cur.pre.next = cur.next
                    if cur.next:  # 考虑删除最后一个节点
                        cur.next.pre = cur.pre
                return (count, item)
            else:
                count += 1
                cur = cur.next
        return False 

# 实例化
if __name__ == '__main__':
    dll = DoubleLinkList()

    print(f'链表是否为空:{dll.is_empty}')
    print(f'链表长度:{dll.length}')
    dll.add(10)
    dll.travel()
    dll.add(0)
    dll.append(1)
    dll.append(2)
    dll.append(3)
    dll.append(4)
    dll.append(5)
    dll.append(6)
    dll.travel()
    print(f'链表长度:{dll.length}')
    dll.insert(1, 100)
    dll.insert(7, 100)
    dll.insert(0, 1000000)
    dll.insert(-1, 1000000)
    dll.travel()
    # print(f'链表是否为空:{dll.is_empty}')
    # print(f'链表长度:{dll.length}')
    # print(f'{6}查询结果{dll.search(6)}')
    # print(f'{15}查询结果{dll.search(15)}')
    print(dll.remove(1))
    # dll.travel()


