# -*- coding:utf-8 -*-
'''
不用加减乘除做加法
写一个函数，求两个整数之和，要求在函数体内不得使用+、-、*、/四则运算符号。
'''
class Solution:
    def Add(self, num1, num2):
        # write code here
        a = (num1 & num2) << 1
        b = num1 ^ num2
        sum=a|b
        while a != 0:
            c = a
            d = b

            a = (c & d) << 1
            b = c ^ d
            sum=c|d

        return sum


s = Solution()
print s.Add(111, 899)
