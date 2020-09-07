#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   2-反转链表.py
@Time    :   2020/09/07 16:53:52
@Author  :   Dll 
@Contact :   dengll1783600@foxmail.com
@Desc    :   反转链表
'''

# here put the import lib
'''
反转一个单链表。
示例:
输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL

思路一：迭代，
1、由于题目没有要求不能修改节点的值，所以我们可以遍历节点，
保存节点的值，然后再遍历反向赋值即可
2、前后指针，不断地前后指针后移，同时改变前后节点的指向
       
思路二：递归，主要是搞清楚每一层如何过度，假如后面的节点已经反转（简称反转结果），
则需要让反转结果的最后一个节点（这个节点也就是当前节点的下一个节点（head.next））指向当前节点，
而当前节点指向None即可
'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 迭代1，修改值
    def reverseList1(self, head: ListNode) -> ListNode:
        nodes = []
        cur1 = head; cur2 = head
        while cur1:
            nodes.append(cur1.val)
            cur1 = cur1.next
        # 反向赋值
        while cur2:
            cur2.val = nodes.pop()
            cur2 = cur2.next
        return head
    
    # 迭代2，修改指向
    def reverseList2(self, head: ListNode) -> ListNode:
        # 前一个节点
        pre = None
        # 当前节点
        cur = head
        while cur:
            # 因为当前节点要指向前一个节点，所以需要先保存当前节点的下一个节点
            temp = cur.next
            # 当前节点指向前一个节点
            cur.next = pre
            # 前一个节点后移
            pre = cur
            # 当前节点后移
            cur = temp
        # 循环结束后，当前节点指向None，前一个节点指向尾节点（新链表头结点）
        return pre

    # 递归
    def reverseList3(self, head: ListNode) -> ListNode:
        # 如果链表为空或者只有一个节点，返回head
        if head is None or head.next is None:
            return head
        # 接收上一步的递归结果
        cur = self.reverseList3(head.next)
        # 让上一步递归结果的最后一个节点指向当前节点
        head.next.next = head
        # 让当前节点指向None
        head.next = None
        return cur
