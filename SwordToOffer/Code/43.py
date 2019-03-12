# -*- coding:utf-8 -*-
'''
左旋字符串
汇编语言中有一种移位指令叫做循环左移（ROL），现在有个简单的任务，就是用字符串模拟这个指令的运算结果。对于一个给定的字符序列S，请你把其循环左移K位后的序列输出。例如，字符序列S=”abcXYZdef”,要求输出循环左移3位后的结果，即“XYZdefabc”。是不是很简单？OK，搞定它！
'''
class Solution:
    def LeftRotateString(self, s, n):
        # write code here
        size=len(s)
        if size==0:
            return s
        n=n%size
        listS=list(s)
        temp=listS[0:n]
        for i in range(n):
            del listS[0]

        listS=listS+temp

        s="".join(listS)

        return s


solution=Solution()
print solution.LeftRotateString('abcde',3)
