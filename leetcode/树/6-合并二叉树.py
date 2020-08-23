#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   6-合并二叉树.py
@Time    :   2020/08/22 15:17:18
@Author  :   Dll 
@Contact :   dengll1783600@foxmail.com
@Desc    :   合并两个二叉树
'''

# here put the import lib
'''
给定两个二叉树，想象当你将它们中的一个覆盖到另一个上时，两个二叉树的一些节点便会重叠。
你需要将他们合并为一个新的二叉树。合并的规则是如果两个节点重叠，那么将他们的值相加作为节点合并后的新值，
否则不为 NULL 的节点将直接作为新二叉树的节点。

示例 1:
输入: 
	Tree 1                     Tree 2                  
          1                         2                             
         / \                       / \                            
        3   2                     1   3                        
       /                           \   \                      
      5                             4   7                  
输出: 
合并后的树:
	     3
	    / \
	   4   5
	  / \   \ 
	 5   4   7
注意: 合并必须从两个树的根节点开始。

思路一：递归，

思路二：迭代，BFS，广度优先遍历
'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 递归修改树结构
    def mergeTrees1(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if not t1:
            return t2
        if not t2:
            return t1
        # 合并根节点
        t1.val += t2.val
        # 迭代左子节点
        t1.left = self.mergeTrees1(t1.left, t2.left)
        # 迭代右子节点
        t1.right = self.mergeTrees1(t1.right, t2.right)
        return t1
    
    #递归不修改树结构
    def mergeTrees2(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if not t1:
            return t2
        if not t2:
            return t1
        root = TreeNode(-1)
        root.val = t1.val + t2.val
        root.left = self.mergeTrees2(t1.left, t2.left)
        root.right = self.mergeTrees2(t1.right, t2.right)
        return root
    
    # 迭代，修改树结构(t1)
    def mergeTrees3(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if t1 is None:
            return t2
        if t2 is None:
            return t1
        # 这里也可以不用元组结构，但是需要同时pull和push两树对应的节点
        queue = [(t1, t2)]
        while queue:
            n1, n2 = queue.pop(0)
            # 进队列的都不为空,直接赋值相加
            n1.val += n2.val
            # 如果节点的左子节点都不为空，则都进队列
            if n1.left and n2.left:
                queue.append((n1.left, n2.left))
            # 由于是合并到t1，不需要考虑t2左子节点为空,t1左子节点不为空的情况
            if not n1.left:
                n1.left = n2.left
            # 右节点同理
            if n1.right and n2.right:
                queue.append((n1.right, n2.right))
            if not n1.right:
                n1.right = n2.right
        return t1
