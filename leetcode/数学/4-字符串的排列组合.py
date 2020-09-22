#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   4-字符串的排列组合.py
@Time    :   2020/09/22 10:53:51
@Author  :   Dll 
@Contact :   dengll1783600@foxmail.com
@Desc    :   None
'''

# here put the import lib
'''
排列组合最直接的思想就是递归了，简单明了。
arr = ["a","b","c"] 
---> 
['a', 'b', 'c']
['a', 'c', 'b']
['b', 'a', 'c']
['b', 'c', 'a']
['c', 'b', 'a']
['c', 'a', 'b']
思路很简单，就是固定一个元素，求剩余元素的全排列
主要有两种方法，一种是插入，一种换位
方法一：把当前元素插入剩余元素全排列的结果中，
比如[a,b,c]
a --> [b,c]
      b --> [c]
             c 
b插入[c] --> [bc, cb]
a插入[b,c] --> [abc,bac,bca],[acb,cab,cba]
就是把当前元素插入上层结果的每一个位置，a插入bc，即?b?c?，三个问号位置都是可插入位置
方法二：调换当前元素与其余元素的位置，求剩余元素的全排列
本质上就是确定当前位置的所有可能，确定下一个位置所有可能
比如[a,b,c]
a和a交换：a[bc]
a和b交换：b[ac]
a和c交换：c[ab]
确定第一个位置的abc后，对[bc] [ac] [ab]递归上述的操作
'''

def permutation1(lst):
    if len(lst) <= 1:
        return lst
    else:
        result = []
        key = lst[0]
        temp = permutation1(lst[1:])
        for i in temp:
            for j in range(len(i)):
                result.append(i[:j]+key+i[j:])
            result.append(i+key)
        return result
    
def permutation2(lst, start, end):
    if start == end:
        return lst
    else:
        result = []
        for i in range(start, end):
            lst[i], lst[start] = lst[start], lst[i]
            result.append(permutation2(lst, start+1, end))
            lst[i], lst[start] = lst[start], lst[i]
        return result


if __name__ == '__main__':
    lst = ["a","b","c","d","e"]
    permutation1(lst)
    permutation2(lst, 0, len(lst))