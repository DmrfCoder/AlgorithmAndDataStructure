# -*- coding:utf-8 -*-
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
