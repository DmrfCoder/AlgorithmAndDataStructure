# -*- coding:utf-8 -*-
'''
请实现一个函数，将一个字符串中的每个空格替换成“%20”。例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy。

'''
class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        # write code here
        for index in range(len(s)):
            if s[index]==' ':
                s[index]='%20'

            return s


    def replaceSpace2(self, s):
        # write code here
        targetChar = ' '
        returnS = ''
        for itemChar in s:
            if itemChar == targetChar:
                returnS += '%20'
            else:
                returnS += itemChar
        return returnS


s = 'We Are Happy.'
soulution = Solution()
print soulution.replaceSpace(s)
