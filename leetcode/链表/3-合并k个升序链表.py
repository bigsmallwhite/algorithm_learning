#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   3-合并k个升序链表.py
@Time    :   2020/09/07 22:15:18
@Author  :   Dll 
@Contact :   dengll1783600@foxmail.com
@Desc    :   合并k个升序链表
'''

# here put the import lib
'''
给你一个链表数组，每个链表都已经按升序排列。
请你将所有链表合并到一个升序链表中，返回合并后的链表。
示例 1：
输入：lists = [[1,4,5],[1,3,4],[2,6]]
输出：[1,1,2,3,4,4,5,6]
解释：链表数组如下：
[
  1->4->5,
  1->3->4,
  2->6
]
将它们合并到一个有序链表中得到。
1->1->2->3->4->4->5->6
示例 2：
输入：lists = []
输出：[]
示例 3：
输入：lists = [[]]
输出：[]

其实最简单的想法就是先合并两个，然后合并第三个、第四个、……一直到最后一个
思路一：分治，我们已经知道如何合并两个有序链表，那么K个就分为 2个2个来合并，
       然后把合并的结果继续合并
思路二：优先队列，把所有链表的头节点放在堆（小顶堆）中，弹出最小值，
       然后最小值所在链表的下一个入堆，继续上述操作
'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 分治
    def mergeKLists1(self, lists):
        n = len(lists)
        # 二分+递归
        def merge(left, right):
            if left > right:
                return 
            if left == right:
                return lists[left]
            mid = (left + right) // 2
            l1 = merge(left, mid)
            l2 = merge(mid+1, right)
            return mergeTwoLists(l1, l2)
        
        # 这里用递归合并两个有序链表，也可以用迭代，速度更快些
        def mergeTwoLists(l1, l2):
            if not l1:
                return l2
            if not l2:
                return l1
            if l1.val < l2.val:
                l1.next = mergeTwoLists(l1.next, l2)
                return l1
            else:
                l2.next = mergeTwoLists(l2.next, l1)
                return l2
        return merge(0, n-1)
    
    # 递归
    def mergeKLists2(self, lists):
        import heapq
        n = len(lists)
        if n == 0:
            return None
        temp = []
        dummy = ListNode(0)
        cur = dummy
        # 所有的链表头节点入堆
        for i in range(n):
            if lists[i]:
                heapq.heappush(temp, (lists[i].val, i))
                lists[i] = lists[i].next
        
        while temp:
            # 弹出最小点，放入新链表，
            val, index = heapq.heappop(temp)
            cur.next = ListNode(val)
            cur = cur.next
            # 入堆弹出的节点的next节点
            if lists[index]:
                heapq.heappush(temp, (lists[index].val, index))
                lists[index] = lists[index].next
        return dummy.next




