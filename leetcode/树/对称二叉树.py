#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   对称二叉树.py
@Time    :   2020/08/21 15:02:54
@Author  :   Dll 
@Contact :   dengll1783600@foxmail.com
@Desc    :   对称二叉树的判断
'''

# here put the import lib
'''给定一个二叉树，检查它是否是镜像对称的。
例如，二叉树 [1,2,2,3,4,4,3] 是对称的。
    1
   / \
  2   2
 / \ / \
3  4 4  3
但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:
    1
   / \
  2   2
   \   \
   3    3

思路一：BFS迭代，层次遍历每一层，判断每一层的值是否是回文数

思路二：递归，如果左树的左孩子与右树的右孩子对称，左树的右孩子与右树的左孩子对称，那么这个左树和右树就对称
def 函数A（左树，右树）：左树节点值等于右树节点值 且 函数A（左树的左子树，右树的右子树）and 函数A（左树的右子树，右树的左子树）为真 才返回真
'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # bfs
    def isSymmetric1(self, root: TreeNode) -> bool:
        if root is None:
            return True
        # 队列存储中间节点
        queue = [root]
        while queue:
            # 存储每一层节点的值
            result = []
            length = len(queue)
            for i in range(length):
                node = queue.pop(0)
                # 如果节点为空，直接添加None，不再进队列
                if not node:
                    result.append(None)
                    continue
                queue.append(node.left)
                queue.append(node.right)
                result.append(node.val)
            # 判断当前层是否对称
            temp = result[::-1]
            if result != temp:
                return False 
        return True
    
    # 递归
    def isSymmetric2(self, root: TreeNode) -> bool:
        def check(node1, node2):
            # 两个节点都为空，对称
            if not node1 and not node2:
                return True
            # 有一个节点不为空，不对称
            elif not node1 or not node2:
                return False
            # 节点的值不等，不对称
            if node1.val != node2.val:
                return False
            return check(node1.left, node2.right) and check(node1.right, node2.left)
        return check(root, root)

