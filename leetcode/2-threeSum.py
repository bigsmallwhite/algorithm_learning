#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   2-threeSum.py
@Time    :   2020/07/13 22:34:43
@Author  :   Dll 
@Contact :   dengll1783600@foxmail.com
@Desc    :   三数之和（对撞指针）
'''


"""
找出列表中是否有三个数的值等于目标值，返回三数的索引值
如[4, 7, 1, 0, 3, 5, 6]，目标为9，则返回[2, 4, 5](1, 3, 5)
"""
# 对撞指针法，遍历


class Solution:

    def threeSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        """
        result = []
        nums.sort()  # 先对数组进行排序
        n = len(nums)
        for i in range(n):
            left = i + 1    # 左指针
            right = n - 1   # 右指针
            # 判断遍历的元素是否与上一个相同
            if i >=1 and nums[i] == nums[i-1]:
                continue
            # 指针对撞
            while left < right:
                # 和小于目标值，左指针右移
                if nums[i] + nums[left] + nums[right] < target:
                    left += 1
                    # 左指针重复
                    while left < right and nums[left-1] == nums[left]:
                        left += 1
                # 和大于目标值，右指针左移
                elif nums[i] + nums[left] + nums[right] > target:
                    right -= 1
                    # 右指针重复
                    while left < right and nums[right+1] == nums[right]:
                        right -= 1
                else:
                    result.append((nums[i], nums[left], nums[right]))
                    left += 1
                    right -= 1
                    # 判断下一个左右指针元素是否相等
                    while left < right and nums[left-1] == nums[left]:
                        left += 1
                    while left < right and nums[right+1] == nums[right]:
                        right -= 1
        return result


if __name__ == '__main__':

    ts = Solution()
    nums = [2, 7, 1, 0, 3, 5, 6]
    target = 9
    print(ts.threeSum(nums, target))

