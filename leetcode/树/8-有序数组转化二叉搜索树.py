#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   8-有序数组转化二叉搜索树.py
@Time    :   2020/12/13 01:04:06
@Author  :   Dll 
@Contact :   dengll1783600@foxmail.com
@Desc    :   将一个按照升序排列的有序数组，转换为一棵高度平衡二叉搜索树。
'''

# here put the import lib
'''
一个高度平衡二叉树是指一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1。
示例:

给定有序数组: [-10,-3,0,5,9],
一个可能的答案是：[0,-3,9,-10,null,5]，它可以表示下面这个高度平衡二叉搜索树：

      0
     / \
   -3   9
   /   /
 -10  5

思路：二叉搜索树的特性：二叉搜索树的中序遍历结果为递增序列。
所以其实就是要我们实现这一特性的逆过程。
递归设计：
1、选取要构造关系的节点并创建它
2、构造该节点的左子树
3、构造该节点的右子树
函数的输入为递增数组，函数的返回为完成构造的节点。
何时结束：
当输入的递增数组为空时，只能构成一棵空树，此时返回空节点。
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sortedArrayToBST(self, nums: list) -> TreeNode: 
        if not nums:
            return None
        mid = len(nums) // 2
        root = TreeNode(nums[mid])
        left_nums = nums[:mid]
        right_nums = nums[mid+1:]
        root.left = self.sortedArrayToBST(left_nums)
        root.right = self.sortedArrayToBST(right_nums)
        return root