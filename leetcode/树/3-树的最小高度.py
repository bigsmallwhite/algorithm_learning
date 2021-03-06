#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   树的最小高度.py
@Time    :   2020/08/19 22:06:37
@Author  :   Dll 
@Contact :   dengll1783600@foxmail.com
@Desc    :   求二叉树的最小高度
'''

# here put the import lib
'''
给定一个二叉树，找出其最小深度。
最小深度是从根节点到最近叶子节点的最短路径上的节点数量。
说明: 叶子节点是指没有子节点的节点。

示例:
给定二叉树 [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
返回它的最小深度2.

思路一：递归，由于做过树的最大高度，所以直接把maxdepth 改成 mindepth，但是需要注意的是，
最大高度是根节点到最下面的一个子节点的路径长度，而最小高度则是根节点到最近的叶子节点的长度。
举个简答的例子，[1, 2]，这个的最小高度不是1，是2，因为1不是叶子节点，只有左右子节点都为空的节点才是叶子节点。
所以我们不能单纯地把maxdepth 改成 mindepth，还要增加一下判断边界条件，如果有子树为空，只能返回另一个子树的高度

思路二：BFS，从根节点开始，找到第一个叶子节点，遍历完一层depth+1，中间节点用队列存储
'''

from typing import NoReturn


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    # 递归
    def minDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        # 必须是到叶子节点
        # 左子节点为空，当前节点不为叶子节点，继续从右子节点找
        if root.left is None and root.right is not None:
            return 1 + self.minDepth(root.right)
        # 右子节点为空，当前节点不为叶子节点，继续从左子节点找
        elif root.left is not None and root.right is None:
            return 1 + self.minDepth(root.left)
        else:
            return min(self.minDepth(root.left), self.minDepth(root.right)) + 1

    # 广度优先遍历
    def bfs(self, root):
        if root is None:
            return 0
        queue = [root]
        depth = 1
        while queue:
            length = len(queue)
            for i in range(length):
                node = queue.pop(0)
                # 遇到叶子节点就退出
                if node.left is None and node.right is None:
                    return depth
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            # 一层循环结束，深度+1
            depth += 1
        
        

