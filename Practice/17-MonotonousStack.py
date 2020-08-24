#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   17-单调栈.py
@Time    :   2020/08/24 11:49:25
@Author  :   Dll 
@Contact :   dengll1783600@foxmail.com
@Desc    :   实现单调栈（递增/递减）
'''

# here put the import lib
'''
单调栈指的是栈中存放的数据出栈应该是有序的
单调递增栈：栈中数据出栈的序列为单调递增序列(栈顶到栈底-->递增)
单调递减栈：栈中数据出栈的序列为单调递减序列(栈顶到栈底-->递减)

单调栈主要回答这样的几种问题:
    1、比当前元素更大的下一个元素
    2、比当前元素更大的前一个元素
    3、比当前元素更小的下一个元素
    4、比当前元素更小的前一个元素
'''

class Solution:
    
    # 单调递增栈：查找下一个大元素
    def nextGreaterElement(self, nums):
        '''
        res:'-1'代表没有大于当前元素的值，其他值代表大于当前值的下一个值
        '''
        stack = list()
        res = [-1] * len(nums)
        for i, n in enumerate(nums):
            # 入栈元素只能比栈顶元素小，新元素大于栈顶，就要更新
            while stack and nums[stack[-1]] < n:
                # 这一步执行具体的操作，这里是记录下一个大的数
                res[stack.pop()] = n
            stack.append(i)
        return res
    
    # 单调递减栈：查找下一个小元素
    def nextSmallerElement(self, nums):
        stack = list()
        res = [-1] * len(nums)
        for i, n in enumerate(nums):
            # 入栈元素只能比栈顶元素大
            while stack and nums[stack[-1]] > n:
                # 这一步执行具体的操作，这里是记录下一个小的数
                res[stack.pop()] = n
            stack.append(i)
        return res

    # 单调递增栈：查找上一个大元素
    def preGreaterElement(self, nums):
        stack = list()
        res = [-1] * len(nums)
        for i, n in enumerate(nums):
            # 保证先进栈的元素大
            while stack and nums[stack[-1]] < n:
                stack.pop()
            if stack:
                res[i] = nums[stack[-1]]
            stack.append(i)
    
    # 单调递减栈：查找上一个小元素
    def preSmallerElement(self, nums):
        stack = list()
        res = [-1] * len(nums)
        for i, n in enumerate(nums):
            # 保证先进栈的元素小
            while stack and nums[stack[-1]] > n:
                stack.pop()
            if stack:
                res[i] = nums[stack[-1]]
            stack.append(i)


if __name__ == '__main__':
    nums = [6,5,4,3,2,1,2,6,7]
    s = Solution()
    print(s.nextSmallerElement(nums))
    print(s.nextGreaterElement(nums))
    print(s.preSmallerElement(nums))
    print(s.preGreaterElement(nums))