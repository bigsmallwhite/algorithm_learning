#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   合并两个有序链表.py
@Time    :   2020/08/11 11:29:38
@Author  :   Dll 
@Contact :   dengll1783600@foxmail.com
@Desc    :   合并两个有序链表
'''

# here put the import lib
'''
将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 
示例：

输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4

思路一、迭代：合并有序链表其实和归并排序中合并有序序列一模一样，所以可以完全参照归并排序，
就是不断比较两个链表的头节点，如果某一个链表迭代完成，另一个链表还有节点，直接指向剩余的链表即可。

思路二、递归：

'''

class ListNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        newlist = ListNode(None)
        head = newlist
        while l1 and l2:
            if l1.val < l2.val:
                head.next = ListNode(l1.val)
                l1 = l1.next
            else:
                head.next = ListNode(l2.val)
                l2 = l2.next
            head = head.next
        while l1:
            # 这里可以优化一下，直接head.next = l1就行，因为l1有序
            head.next = ListNode(l1.val)
            l1 = l1.next
            head = head.next
        while l2:
            # 同上的优化方法
            head.next = ListNode(l2.val)
            l2 = l2.next
            head = head.next
        return newlist.next

    # 递归的思路