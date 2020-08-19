#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   树的最大高度.py
@Time    :   2020/08/16 23:23:11
@Author  :   Dll 
@Contact :   dengll1783600@foxmail.com
@Desc    :   求二叉树的最大高度
'''

# here put the import lib
'''
给定一个二叉树，找出其最大深度。
二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。
思路：递归，

      root(max(x,y)+1)
      / \
 (x)left right(y)
 
简化为三个节点：root、root.left、root.right，root.left和root.right分别记录的是root的左右子树的最大深度x和y。
那么本级递归应该做什么就很明确了，自然就是在root的左右子树中选择较大的一个，
再加上1就是以root为根的子树的最大深度max(x,y)+1，然后再返回这个深度即可。
'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        left_deepth = self.maxDepth(root.left)
        right_deepth = self.maxDepth(root.right)
        return max(left_deepth, right_deepth) + 1