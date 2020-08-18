#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   有效括号.py
@Time    :   2020/08/13 11:22:24
@Author  :   Dll 
@Contact :   dengll1783600@foxmail.com
@Desc    :   判断括号的有效性
'''

# here put the import lib
'''
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。

示例 1:       示例 2:           示例 3:        示例 4:         示例 5:
输入: "()"    输入: "()[]{}"    输入: "(]"     输入: "([)]"    输入: "{[]}"
输出: true    输出: true        输出: false    输出: false     输出: true

思路一：入栈出栈
遍历字符串，如果栈为空，则pull，如果不为空，则判断当前遍历括号是否与栈顶元素匹配
如果匹配，则push栈顶元素，最后判断栈是否为空，为空则有效，反之无效。

思路二：字符串替换
直接利用字符串的in功能，判断'{}' '()' '[]'是否in string，如果存在，
则替换为空，继续对新的字符串进行迭代
如果没有任何一对括号在string中，就对字符串是否为空字符串进行判断，
如果是，则有效，反之无效。
'''

class Solution:
    def isValid1(self, s: str) -> bool:
        # 为了方便匹配，赋值判断和是否为0
        dic = {'(': 1, ')': -1, '{': 2, '}': -2, '[': 3, ']': -3}
        if len(s) == 1:
            return False
        if len(s) == 0:
            return True
        result = [s[0]]
        for i in s[1:]:
            # 列表为空，直接pull新括号
            if not result:
                result.append(i)
            # 列表不为空，需要进行匹配判断
            else:
                if dic[i] + dic[result[-1]] == 0:
                    result.pop()
                else:
                    result.append(i)
        if len(result) == 0:
            return True
        else:
            return False
    
    def isValid2(self, s: str) -> bool:
        # 迭代去掉字符串中有效的括号对
        while '{}' in s or '()' in s or '[]' in s:
            s = s.replace('{}', '')
            s = s.replace('[]', '')
            s = s.replace('()', '')
        return s == ''