#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   3-栈内元素的输出顺序种类.py
@Time    :   2020/09/27 00:03:14
@Author  :   Dll 
@Contact :   dengll1783600@foxmail.com
@Desc    :   求栈内元素的输出有多少种情况
'''

# here put the import lib
'''
有一个容量足够大的栈，n 个元素以一定的顺序入栈，出栈顺序有多少种？
比如，AB 两个元素，入栈顺序为 AB，出栈情况有两种：
（1）入 A，出 A，入 B，出 B，出栈顺序为 AB；
（2）入 A，入 B，出 B，出 A，出栈顺序为 BA。
因此，2 个元素时，结果为 2。
思路：分析第一个元素的出栈顺序
举个例子，我们假设入栈元素为 A，B，C，D。我们按照 "A在出栈序列中的位置" 分类讨论：
（1）当 A 第一个出栈时，A 先进，然后马上出栈。这种情况下，共有 “BCD 出栈顺序的种类数” 种方案。
也就是 f (n-1)。
（2）当 A 第二个出栈时，A 先进，B 再进，之后 B 需要马上出来（这样才能确保 A 排第二）。
此时共有 f (n-2) 种方案。
（3）当 A 第三个出栈时，A 先进，之后只要确保排在 A 后面两个的元素比 A 先出即可。
此时共有 f(2)*f(1) 种方案。f(2) 是指 "BC入栈出栈顺序的种类数"，f(1)是指”D 入栈出栈的种类数。

因此，重要的是固定一个元素的出栈位置，如果元素的总数为n，第一个元素的出栈顺序为i（2<=i<=n-1）,
那么在i次出栈之前，有i-1个元素进出栈，种类为f(i-1),
那么在i次出栈之后，有n-i个元素进出栈，种类为f(n-i),
前后的种类是f(i-1)*f(n-i)，当i从小到大变化，f(i-1)递增，f(n-i)递减，把每次的乘积累积即可。
'''
def solution(lst):
    n = len(lst)
    dp = [None] * (n+1)
    if n == 0:
        return 1
    if n <= 2:
        return n
    dp[0] = 1; dp[1] = 1; dp[2] = 2
    for i in range(3, n+1):
        s = 0
        for j in range(i):
            s += dp[j]*dp[i-j-1]
        dp[i] = s
    return dp[n]

if __name__ == '__main__':
    lst = ['a', 'b', 'c', 'd']
    print(solution(lst))