#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   2-递归实现栈逆序.py
@Time    :   2020/08/24 22:55:39
@Author  :   Dll 
@Contact :   dengll1783600@foxmail.com
@Desc    :   只能用递归实现栈的逆序
'''

# here put the import lib
'''
只能使用递归来将栈的元素反转（逆序），不能使用其他的数据结构
假如一个空栈[],先后入栈元素3、2、1，--> [3, 2, 1],
只利用递归实现[3, 2, 1] --> [1, 2, 3]
解决该问题的核心其实是：如何通过递归算法来获取栈底元素，也就是getLast函数的算法
只要获取了栈底的元素，然后递归的进行逆序就行
'''

def reverseStack(stack):
    # 递归地把栈内元素取出来
    if stack:
        temp = getLast(stack)
        reverseStack(stack)
        # 递归后，后取出的先入栈
        stack.append(temp)
    return stack

def getLast(stack):
    top = stack.pop()
    if not stack:
        return top
    else:
        # 递归的弹出元素
        res = getLast(stack)
        # 把前两次递归弹出的元素按相同的顺序入栈
        stack.append(top)
        return res

if __name__ == '__main__':
    stack = [3, 2, 1]
    print(reverseStack(stack))
