#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   03-数组重复数字.py
@Time    :   2020/08/12 10:12:51
@Author  :   Dll 
@Contact :   dengll1783600@foxmail.com
@Desc    :   找出数组中重复的数字
'''

# here put the import lib
'''
找出数组中重复的数字。

在一个长度为 n 的数组 nums 里的所有数字都在 0～n-1 的范围内。
数组中某些数字是重复的，但不知道有几个数字重复了，也不知道每个数字重复了几次。
请找出数组中任意一个重复的数字。

示例 1：
输入：
[2, 3, 1, 0, 2, 5, 3]
输出：2 或 3 

思路一：哈希表，遍历一次nums，依次放入哈希表，如果索引重复，则return
时间O(n)，空间O（n）

思路二：原地查重，由于元素的大小小于len(nums)，则可以根据列表的索引和元素一一对应的关系来查找重复，
如果没有重复，那么元素就一一对应索引，否则，元素与索引就存在多对一的关系。
'''


class Solution:
    def findRepeatNumber1(self, nums) -> int:
        # 哈希表
        dic = {}
        for i in nums:
            if i not in dic:
                dic[i] = 1
            else:
                return i
    

    def findRepeatNumber2(self, nums) -> int:
        for index, value in enumerate(nums):
            if index != value:
                if value == nums[value]:
                    return value
                # 由于交换的过程中value会变化，所以需要记录一下value的值
                temp = value
                value, nums[temp] = nums[temp], value

