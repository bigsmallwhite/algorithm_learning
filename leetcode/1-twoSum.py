#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   1-twoSum.py
@Time    :   2020/06/24 00:41:05
@Author  :   Dll 
@Contact :   dengll1783600@foxmail.com
@Desc    :   两数之和（哈希）
'''


"""
找出列表中是否有两个数的值等于目标值，返回两数的索引值
如[2, 7, 1, 0, 3, 5, 6]，目标为9，则返回[0, 1]
"""
# 采用哈希索引，遍历的同时构建字典，在遍历到新的元素时，计算目标值
# 与新元素的差值，在字典中查找是否出现，如果出现则返回

class Solution:

    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashmap={}
        for index, num in enumerate(nums):
            another_num = target - num
            if another_num in hashmap:
                return [hashmap[another_num],index]
            hashmap[num] = index

    
if __name__ == '__main__':

    ts = Solution()
    nums = [2, 7, 1, 0, 3, 5, 6]
    target = 9
    print(ts.twoSum(nums, target))


