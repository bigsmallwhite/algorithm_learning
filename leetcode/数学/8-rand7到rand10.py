#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   8-rand7到rand10.py
@Time    :   2020/10/10 00:13:09
@Author  :   Dll 
@Contact :   dengll1783600@foxmail.com
@Desc    :   实现不同范围内随机数的生成
'''

# here put the import lib
'''
已有方法 rand7 可生成 1 到 7 范围内的均匀随机整数，试写一个方法 rand10 生成 1 到 10 范围内的均匀随机整数。
不要使用系统的 Math.random() 方法。
示例 1:
输入: 1
输出: [7]
示例 2:
输入: 2
输出: [8,4]
示例 3:
输入: 3
输出: [8,1,10]

思路：rand7实现[1,2,3,4,5,6,7]随机生成
      rand7-1 实现[0,1,2,3,4,5,6]的随机生成
      (rand7-1)*7实现[0,7,14,21,28,35,42]的随机生成
      (rand7-1)*7 + rand7实现[1-49]的随机生成，每个的概率是1/7*1/7(前后两个事件独立)
'''

class Solution():
    def rand7(self):
        pass
    def rand10(self):
        while True:
            res = (self.rand7()-1)*7 + self.rand7()
            # 这里如果单纯地判断res<=10,效率是很慢的
            # 因为大部分的数据都是在10-49范围内
            # 所以为了提高效率
            # 我们可以把范围扩展到离49最近的10的整数倍范围内，即1-40
            # 因为10的整数倍内对10取余，然后+1，就可以得到1-10
            # 如果转化到rand9(),即可扩展到1-45
            if res <= 40:
                break
        return res%10 + 1