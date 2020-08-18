#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   平衡二叉树.py
@Time    :   2020/08/16 23:20:49
@Author  :   Dll 
@Contact :   dengll1783600@foxmail.com
@Desc    :   平衡二叉树的判断
'''

# here put the import lib
'''
给定一个二叉树，判断它是否是高度平衡的二叉树。
本题中，一棵高度平衡二叉树定义为：一个二叉树每个节点的左右两个子树的高度差的绝对值不超过1。

示例 1:
给定二叉树 [3,9,20,null,null,15,7]
    3
   / \
  9  20
    /  \
   15   7
返回 true 。

示例 2:
给定二叉树 [1,2,2,3,3,null,null,4,4]
       1
      / \
     2   2
    / \
   3   3
  / \
 4   4
返回 false 。

思路一：从本质上讲，要求所有子树的高度差不大于1，所以我们直接暴力求解，遍历所有节点的左右子树高度，求差，看是否符合要求

思路二：递归，实际上对思路一的优化，思路一中存在大量重复的计算，按理说只需要从下往上计算一次就应该可以判断出来，
所以我们直接递归计算每一层左右子树的高度，遇到差值大于1的，退出递归。

思路三：递归，思路二毕竟return的是高度，需要设置一个全局控制变量，而且不能退出递归，必须完全递归树的全部层，这样就导致跟多的执行时间，
所以我们希望能在递归的同时判断高度差，直接返回True or False。
这里我们返回的信息应该是既包含子树的深度的int类型的值，又包含子树是否是平衡二叉树的bool类型的值
'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    
    # 定义全局控制变量
    def __init__(self):
        self.flag = False

# 方法一：   
    # 求高度
    def getHight1(self, node):
        if node is None:
            return 0
        else:
            return max(self.getHight1(node.left), self.getHight1(node.right)) + 1

    # 暴力遍历每个节点的左右子树高度差
    def isBalanced1(self, root: TreeNode) -> bool:
        if root is None:
            return True
        
        if (self.isBalanced1(root.left) and self.isBalanced1(root.right) and 
        abs(self.getHight1(root.left) - self.getHight1(root.right)) <= 1):
            return True
        else:
            return False

# 方法二：    
    # 从下往上的一次性递归判断
    def isBalanced2(self, root):
        self.getHight2(root)
        if self.flag:
            return False
        return True

    def getHight2(self, node):
        if node is None:
            return 0
        left = self.getHight2(node.left)
        right = self.getHight2(node.right)
        if abs(left-right) > 1:
            self.flag = True
        return max(left, right) + 1

# 方法三：



    