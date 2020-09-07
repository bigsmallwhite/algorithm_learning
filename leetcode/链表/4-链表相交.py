#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   4-链表相交.py
@Time    :   2020/09/06 00:12:31
@Author  :   Dll 
@Contact :   dengll1783600@foxmail.com
@Desc    :   判断链表是否相交
'''

# here put the import lib
'''
给定两个（单向）链表，判定它们是否相交并返回交点。
请注意相交的定义基于节点的引用，而不是基于节点的值。换句话说，
如果一个链表的第 k 个节点与另一个链表的第 j 个节点是同一节点（引用完全相同），则这两个链表相交。

输入：intersectVal = 2, listA = [0,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1
输出：Reference of the node with value = 2
输入解释：相交节点的值为 2 （注意，如果两个列表相交则不能为 0）。
从各自的表头开始算起，链表 A 为 [0,9,1,2,4]，链表 B 为 [3,2,4]。
在A中，相交节点前有 3 个节点；
在B中，相交节点前有 1 个节点。

思路一：很直白的比较方法，因为相交的地方及其后续的节点全部相同，
所以需要把两个链表右对齐，长的链表先走完长的那部分，然后再逐个节点比较
过程：
    1、计算链表长度
    2、比较长度，长的先走完长的部分
    3、逐个节点对比

思路二：双指针，逐个节点做比较，假设两个链表分别为ABC，DBC
很明显AB和DB的长度不同，两段BC完全相同，两个指针先走完自己的链表，
然后走对方的链表，由于AB+BC+DB =DB+BC+AB，所以两个指针肯定会同时在D点相遇，
而相遇的节点就是相交的地方
'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        # 判断是否空链表
        if not headA:
            return None
        if not headB:
            return None
        curA = headA; curB = headB
        # 计算两个链表的长度
        lengthA = 0; lengthB = 0
        while curA:
            lengthA += 1
            curA = curA.next
        while curB:
            lengthB += 1
            curB = curB.next
        # 长的链表先走
        curA = headA; curB = headB
        if lengthA > lengthB:
            for i in range(lengthA-lengthB):
                curA = curA.next
        else:
            for i in range(lengthB-lengthA):
                curB = curB.next
        # 逐个节点比较
        while curA:
            if curA == curB:
                return curA
            curA = curA.next
            curB = curB.next
        return None

    # 双指针法
    def getIntersectionNode1(self, headA: ListNode, headB: ListNode) -> ListNode:
        curA = headA
        curB = headB
        while curA != curB:
            # 如果链表A没有走完就继续走
            if curA:
                curA = curA.next
            # 如果链表A走完就开始走链表B
            else:
                curA = headB
            # 链表B同理
            if curB:
                curB = curB.next
            else:
                curB = headA
        return curA
