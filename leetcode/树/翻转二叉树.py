#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   翻转二叉树.py
@Time    :   2020/08/21 22:14:41
@Author  :   Dll 
@Contact :   dengll1783600@foxmail.com
@Desc    :   None
'''

# here put the import lib
'''
翻转一棵二叉树。
示例：
输入：
     4
   /   \
  2     7
 / \   / \
1   3 6   9
输出：
     4
   /   \
  7     2
 / \   / \
9   6 3   1

这道理的主要思路就是从上到下交换子树，再交换子树的子树，循环下去……，把每一个节点的子树交换后，即可。
所以核心的任务就是遍历节点了，不管是用递归还是迭代，都行。
思路一：递归，包括前序遍历、中序遍历、后序遍历
思路二：迭代，层次遍历，把节点一个个放在队列中
'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    
    # 自己想的方法，直接交换镜像位置的节点的值，但是有些案例跑不通，费解……
        #     return root
        # def invert(node1, node2):
        #     if not node1 and not node2:
        #         return 
        #     elif not node1 and node2:
        #         node1 = TreeNode(node2.val)
        #         node2 = TreeNode(None)
        #     elif not node2 and node1:
        #         node2 = TreeNode(node1.val) 
        #         node1 = TreeNode(None)
        #     else:
        #         node1.val, node2.val = node2.val, node1.val
        #     invert(node1.left, node2.right)
        #     invert(node1.right, node2.left)
        # invert(root.left, root.right)
        # return root
    
    # 递归：前序遍历
    def invertTree1(self, root: TreeNode) -> TreeNode:
        if root is None:
            return root
        # 先交换当前节点的左右子树
        root.left, root.right = root.right, root.left
        # 递归左子节点
        self.invertTree1(root.left)
        # 递归右子节点
        self.invertTree1(root.right)
        return root
    
    # 递归：中序遍历
    def invertTree2(self, root: TreeNode) -> TreeNode:
        if root is None:
            return root
        # 先交换左子节点
        self.invertTree2(root.left)
        # 再交换当前节点
        root.left, root.right = root.right, root.left
        # 最后交换右子节点，注意此时的右子节点已经是root.left了
        self.invertTree2(root.left)
        return root
    
    # 递归：后序遍历
    def invertTree3(self, root: TreeNode) -> TreeNode:
        if root is None:
            return root
        # 递归左子节点
        self.invertTree3(root.left)
        # 递归右子节点
        self.invertTree3(root.right)
        # 交换左右子树
        root.left, root.right = root.right, root.left
        return root

    # 层次遍历
    def invertTree4(self, root: TreeNode) -> TreeNode:
        if root is None:
            return root
        queue = [root]
        while queue:
            node = queue.pop(0)
            node.left, node.right = node.right, node.left
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return root
