#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   1-搜索插入位置.py
@Time    :   2020/12/14 17:04:18
@Author  :   Dll 
@Contact :   dengll1783600@foxmail.com
@Desc    :   在有序数组中找到目标值并返回其索引
'''

# here put the import lib
'''
给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。
如果目标值不存在于数组中，返回它将会被按顺序插入的位置。你可以假设数组中无重复元素。

示例 1:
输入: [1,3,5,6], 5
输出: 2

示例 2:
输入: [1,3,5,6], 2
输出: 1

示例 3:
输入: [1,3,5,6], 7
输出: 4

示例 4:
输入: [1,3,5,6], 0
输出: 0

思路一：遍历，一个个比较
思路二：二分
'''

from typing import List

# 遍历
def solution1(nums: List[int], target: int) -> int:
    n = len(nums)
    i = 0
    while i < n:
        if nums[i] == target:
            return i
        elif nums[i] > target and i == 0:
            return 0
        elif nums[i] > target and nums[i-1] < target:
            return i
        elif nums[i] < target and i == n-1:
            return n
        else:
            i += 1

# 二分
def solution2(nums: List[int], target: int) -> int:
    left = 0
    right = len(nums)
    while left < right:
        mid = (left + right) // 2
        if target == nums[mid]:
            return mid
        elif target < nums[mid]:
            right = mid
        else:
            left = mid + 1
    return left

if __name__ == '__main__':
    nums = [1, 3, 5, 7, 9, 11]
    target = 4
    print(solution1(nums, target))
    print(solution2(nums, target))