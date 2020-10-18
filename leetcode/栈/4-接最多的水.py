#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   4-接最多的水.py
@Time    :   2020/10/19 00:01:14
@Author  :   Dll 
@Contact :   dengll1783600@foxmail.com
@Desc    :   求能接到最多的水
'''

# here put the import lib
'''
给你 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。
在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0)。
找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。

示例：
输入：[1,8,6,2,5,4,8,3,7]
输出：49

思路：双指针夹逼
使用双指针从两端向中间靠拢，每次移动较矮的柱子
移动柱子不会漏解的原因：虽然长度减少，但是柱子高度不会超过最矮的 面积不会再超 可以移动
'''

class Solution:
    # 双指针夹逼
    def maxArea(self, height) -> int:
        left = 0
        right = len(height) - 1
        res = 0
        while left < right:
            cur = min(height[left], height[right]) * (right - left)
            res = max(res, cur)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return res
