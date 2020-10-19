#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   5-下一个更大的元素Ⅰ.py
@Time    :   2020/10/19 16:29:18
@Author  :   Dll 
@Contact :   dengll1783600@foxmail.com
@Desc    :   求元素的下一个更大的元素
'''

# here put the import lib
'''
给定两个 没有重复元素 的数组 nums1 和 nums2 ，
其中 nums1 是 nums2 的子集。找到 nums1 中每个元素在 nums2 中的下一个比其大的值。
nums1 中数字 x 的下一个更大元素是指 x 在 nums2 中对应位置的右边的第一个比 x 大的元素。
如果不存在，对应位置输出 -1 。

示例 1:
输入: nums1 = [4,1,2], nums2 = [1,3,4,2].
输出: [-1,3,-1]
示例 2:
输入: nums1 = [2,4], nums2 = [1,2,3,4].
输出: [3,-1]

思路一：暴力，直接遍历nums1，然后在nums2索引元素的位置，
并且从索引的下一个位置开始找，一直找到大于当前元素的元素

思路二：单调栈，先在nums2中利用单调栈找到每个元素的下一个更大的元素，
放在dic中，然后遍历nums1，从dic中找对应值
'''

class Solution:
    # 暴力
    def nextGreaterElement1(self, nums1, nums2):
        res = []
        n1 = len(nums1)
        n2 = len(nums2)
        for i in range(n1):
            for j in range(nums2.index(nums1[i])+1, n2):
                if nums2[j] > nums1[i]:
                    res.append(nums2[j])
                    break
            else:
                res.append(-1)
        return res
    
    # 单调栈
    def nextGreaterElement2(self, nums1, nums2):
        stack = []
        dic = {}
        for i in nums2:
            while stack and stack[-1] < i:
                dic[stack.pop()] = i
            stack.append(i)
        res = [dic.get(x, -1) for x in nums1]
        return res

if __name__ == '__main__':
    s = Solution()
    nums1 = [4, 1, 2]
    nums2 = [1, 3, 4, 2]
    print(s.nextGreaterElement1(nums1, nums2))
    print(s.nextGreaterElement2(nums1, nums2))

