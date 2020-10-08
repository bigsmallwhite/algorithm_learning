#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   6-环形链表.py
@Time    :   2020/10/09 00:28:36
@Author  :   Dll 
@Contact :   dengll1783600@foxmail.com
@Desc    :   判断是否是环形链表
'''

# here put the import lib
'''
给定一个链表，判断链表中是否有环。
如果链表中有某个节点，可以通过连续跟踪 next 指针再次到达，则链表中存在环。 
为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。
如果 pos 是 -1，则在该链表中没有环。注意：pos 不作为参数进行传递，仅仅是为了标识链表的实际情况。
如果链表中存在环，则返回 true 。 否则，返回 false 。

思路：快慢指针，快指针每次走两步，慢指针每次一步，如果有环，两个指针肯定会相遇
（奇思妙想：还可以对每次遍历的节点进行赋值（奇怪的值），如果遇到一个节点的值与赋值相同，则可以认为有环）
'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head or not head.next:
            return False
        fast = head
        slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        return False

