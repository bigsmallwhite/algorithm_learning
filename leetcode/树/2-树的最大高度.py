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
思路一：递归，

      root(max(x,y)+1)
      / \
 (x)left right(y)
 
简化为三个节点：root、root.left、root.right，root.left和root.right分别记录的是root的左右子树的最大深度x和y。
那么本级递归应该做什么就很明确了，自然就是在root的左右子树中选择较大的一个，
再加上1就是以root为根的子树的最大深度max(x,y)+1，然后再返回这个深度即可。

思路二：BFS，广度优先遍历，一层层的遍历节点，一直遍历到最后一层结束。

思路三：DFS，深度优先遍历，利用栈存储中间节点（先进后出），这里需要创建两个栈，同时记录节点和深度值，两个同时pull和pop。
'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 递归
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        left_deepth = self.maxDepth(root.left)
        right_deepth = self.maxDepth(root.right)
        return max(left_deepth, right_deepth) + 1
    
    # 广度优先遍历
    def bfs(self, root):
        if root is None:
            return 0
        queue = [root]
        depth = 0
        # 遍历完整树
        while queue:
            length = len(queue)
            for i in range(length):
                # 先进先出
                node = queue.pop(0)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            # 一层迭代完depth+1
            depth += 1
        return depth

    # 深度优先遍历
    def dfs(self, root):
        if root is None:
            return 0
        stack = [root]
        level = [1]
        max_depth = 0
        while stack:
            # 节点值和该节点的深度值同时出栈
            node = stack.pop()
            temp = level.pop()
            max_depth = max(max_depth, temp)
            # 左节点和深度值同时入栈
            if node.left:
                stack.append(node.left)
                level.append(temp+1)
            # 右节点和深度值同时入栈
            if node.right:
                stack.append(node.right)
                level.append(temp+1)
        return max_depth