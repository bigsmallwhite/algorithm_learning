#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   progression.py
@Time    :   2020/06/27 23:43:13
@Author  :   Dll
@Contact :   dengll1783600@foxmail.com
@Desc    :   None
'''

# here put the import lib

'''
面向对象编程，创建自然数组，然后继承创建 等差、等比数列
'''
class Progression(object):

    def __init__(self,start, test=0):
        self._current = start

    def _advance(self):
        self._current += 1

    def __next__(self):
        if self._current is None:
            raise StopIteration()
        else:
            answer = self._current
            self._advance()
            return answer

    def __iter__(self):
        return self

    def print_progression(self, n):
        print(' '.join(str(next(self)) for i in range(n)))        

# p = Progression()
# p.print_progression(5)

class DCha(Progression):

    def __init__(self, start, increment):
        # super().__init__(args1, args2,……)继承的参数个数与父类一致
        # （前提是父类其余参数都未指定默认值），即继承的参数个数与父类中
        # 
        # 按位置传参，子类可赋值覆盖
        super().__init__(start)
        self._increment = increment
    
    def _advance(self):
        self._current += self._increment

class DBi(Progression):

    def __init__(self, start, increment):
        super().__init__(start)
        self._increment = increment

    def _advance(self):
        self._current *= self._increment

if __name__ == '__main__':
    dc = DCha(5, 10)
    dc.print_progression(5)

    db = DBi(5, 10)
    db.print_progression(5)
