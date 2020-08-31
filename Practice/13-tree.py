#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   13-tree.py
@Time    :   2020/07/20 18:59:47
@Author  :   Dll 
@Contact :   dengll1783600@foxmail.com
@Desc    :   实现树结构（二叉树）
'''

# here put the import lib

class Node(object):
    """构造树节点"""
    def __init__(self, item):
        self.element = item
        self.lchild = None
        self.rchild = None
        

class Tree(object):
    """二叉树"""
    def __init__(self, root = None):
        self.root = root
        self.lst = []

    def add(self, item):
        """添加元素"""
        node = Node(item)
        if self.root is None:
            self.root = node
            return
        queue = [self.root]
        while queue:
            cur_node = queue.pop(0)
            if cur_node.lchild is None:
                cur_node.lchild = node
                return
            else:
                queue.append(cur_node.lchild)
            if cur_node.rchild is None:
                cur_node.rchild = node
                return
            else:
                queue.append(cur_node.rchild)

    def bread_travel(self):
        """广度优先遍历/层次遍历"""
        queue = [self.root]
        while queue:
            cur_node = queue.pop(0)
            print(cur_node.element)
            if cur_node.lchild:
                queue.append(cur_node.lchild)
            if cur_node.rchild:
                queue.append(cur_node.rchild)
            
    """
    深度遍历方式：先序、中序、后序（针对根节点的遍历顺序，永远是左在前，右在后）
    先序：根->左->右
    中序：左->根->右
    后续：左->右->根
    example:
    层次遍历：0, 1, 2, 3, 4, 5, 6, 7, 8, 9
    先序遍历：0, 1, 3, 7, 8, 4, 9, 2, 5, 6
    中序遍历：7, 3, 8, 1, 9, 4, 0, 5, 2, 6
    后序遍历：7, 8, 3, 9, 4, 1, 5, 6, 2, 0
    """
    
    def pre_deep_travel(self, node):
        """先序遍历"""
        if node is None:
            return 
        print(node.element, end='  ')
        self.pre_deep_travel(node.lchild)
        self.pre_deep_travel(node.rchild)
    
    # 先序遍历非递归
    def pre_deep_travel1(self, node):
        if node is None:
            return 
        stack = [node]
        while stack:
            node = stack.pop()
            print(node.element, end= '  ')
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        
    def in_deep_travel(self, node):
        """中序遍历"""
        if node is None:
            return 
        self.in_deep_travel(node.lchild)
        print(node.element, end='  ')
        self.in_deep_travel(node.rchild)
    
    # 中序遍历非递归
    def in_deep_travel1(self, node):
        stack = []
        while node or stack:
            # 先添加所有左节点
            while node is not None:
                stack.append(node)
                node = node.left
            if stack:
                node = stack.pop()
                print(node.element, end='  ')
                # 再添加右节点
                node = node.right
        
    def post_deep_travel(self, node):
        """后序遍历"""
        if node is None:
            return 
        self.post_deep_travel(node.lchild)
        self.post_deep_travel(node.rchild)
        print(node.element, end='  ')

    # 后序遍历非递归，双栈法
    def post_deep_travel1(self, node):
        if node is None:
            return
        stack1 = [node]
        stack2 = []
        while stack1:
            node = stack1.pop()
            stack2.append(node)
            if node.left:
                stack1.append(node.left)
            if node.right:
                stack1.append(node.right)
        while stack2:
            node = stack2.pop()
            print(node.element, end='  ')

        
        
if __name__ == '__main__':
    t = Tree()
    for i in range(15):
        t.add(i)
    t.bread_travel()
    t.pre_deep_travel(t.root)
    print()
    t.in_deep_travel(t.root)
    print()
    t.post_deep_travel(t.root)












