#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   5-两两交换链表中的节点.py
@Time    :   2020/09/07 20:14:24
@Author  :   Dll 
@Contact :   dengll1783600@foxmail.com
@Desc    :   实现两两交换链表中的节点
'''

# here put the import lib
'''
给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。
你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
示例:
给定 1->2->3->4, 你应该返回 2->1->4->3.

思路一：迭代，前后指针，与反转链表类似，需要每次移动两步
思路二：递归，前一步回溯的结果当做已经完成的结果，即head+next+[前一步结果]
       只需要交换前两个节点即可-->next+head+[前一步结果]
'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 迭代
    def swapPairs(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        newlist = ListNode(0)
        # 前指针指向新链表头
        pre = newlist
        # 当前指针指向原链表头（交换对的第一个节点）
        cur = head
        while cur and cur.next:
            # 记录交换对的第一个节点
            first = cur
            # 记录交换对的第二个节点
            second = cur.next
            # 记录下一个交换对的第一个节点
            third = cur.next.next
            # 前指针指向交换对的第二个节点
            pre.next = second
            # 第二个节点指向第一个节点，完成当前交换对的交换
            second.next = first
            # 交换后当前结果指向下一个交换对的第一个节点
            first.next = third
            # 前指针移动两步
            pre = first
            # 当前指针移动两步
            cur = third
        return newlist.next
    
    # 递归
    def swapPairs1(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        # 记录第一个节点
        cur = head
        # 第一个节点移动到第二个位置
        head = head.next
        # 第一个节点指向前一步递归结果（第二个节点以后的部分）
        cur.next = self.swapPairs1(head.next)
        # 第二个节点指向第一个节点
        head.next = cur
        return head
        



