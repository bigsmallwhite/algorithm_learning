#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   12-Heap.py
@Time    :   2020/07/12 22:58:28
@Author  :   Dll 
@Contact :   dengll1783600@foxmail.com
@Desc    :   实现堆结构
'''

# here put the import lib

class Heap(object):
    """大顶堆、小顶堆"""

    def __init__(self):
        """
        由于堆数据是完全二叉树，可以通过计算索引来访问，这里利用列表来存储数据
        如果一个节点的索引为i（根节点为0），则左子节点：2*i+1；右子节点：2*i+2
        """
        self.data = []

    def get_parent_index(self, index):
        """获取父节点的索引，分左右节点"""
        if index >= len(self.data) or index == 0:
            return None
        else:
            return (index-1) >> 1
    
    def swap(self, a, b):
        """交换两个元素"""
        self.data[a], self.data[b] = self.data[b], self.data[a]

    def heapify(self, index):
        """
        大顶堆为例：自顶向下堆化数组
        小顶堆如下：
        if left <= length and self.data[current_index] > self.data[left]
        if right <= length and self.data[current_index] > self.data[right]
        """
        length = len(self.data) - 1
        while True:
            current_index = index
            left = current_index * 2 + 1  # 左子结点
            right = current_index * 2 + 2  # 右子节点
            if left <= length and self.data[current_index] < self.data[left]:
                current_index = left
            if right <= length and self.data[current_index] < self.data[right]:
                current_index = right
            if current_index == index:
                break
            self.swap(index, current_index)
            index = current_index
    
    def insert(self, item):
        """插入元素，先把数据放到数组最后，然后向前堆化"""
        self.data.append(item)
        index = len(self.data) - 1
        parent = self.get_parent_index(index)
        while parent is not None and self.data[index] > self.data[parent]:
            # 交换元素
            self.swap(index, parent)
            index = parent
            parent = self.get_parent_index(parent)
    
    def removeMax(self):
        """删除堆顶元素，将最后一个元素放在堆顶，再从上往下依次堆化"""
        if len(self.data) < 1:
            return None
        Max_value = self.data[0]
        self.data[0] = self.data[-1]
        self.data.pop()
        self.heapify(0)
        return Max_value

if __name__ == '__main__':
    h = Heap()
    h.insert(0)
    h.insert(3)
    h.insert(4)
    h.insert(2)
    h.insert(6)
    h.insert(9)
    h.insert(10)
    h.insert(90)
    print(h.data)
    h.removeMax()
    print(h.data)
