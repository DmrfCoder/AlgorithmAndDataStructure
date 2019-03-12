# -*- coding:utf-8 -*-
'''
请实现一个函数用来匹配包括'.'和'*'的正则表达式。模式中的字符'.'表示任意一个字符，而'*'表示它前面的字符可以出现任意次（包含0次）。 在本题中，匹配是指字符串的所有字符匹配整个模式。例如，字符串"aaa"与模式"a.a"和"ab*ac*a"匹配，但是与"aa.a"和"ab*a"均不匹配
'''


class Solution:
    # s, pattern都是字符串
    def match(self, s, pattern):
        # write code here
        sizeS = len(s)

        pre = ''
        preChar = ''
        patternIndex = len(pattern) - 1
        j = sizeS - 1
        while j >= 0:
            curPatternChar = pattern[patternIndex]
            curSChar = s[j]
            if patternIndex == -1:
                return False
            if pattern[patternIndex] == curSChar:
                patternIndex -= 1
                j -= 1
            elif curPatternChar != '*' and curPatternChar != '.':
                if pre == '*':
                    if preChar == '':
                        preChar = curPatternChar
                    if curSChar == preChar or preChar=='.':
                        j -= 1
                    else:
                        patternIndex -= 1
                        preChar = ''
                        pre = ''

                else:
                    return False
            elif curPatternChar == '.':
                patternIndex -= 1
                j -= 1
            else:
                pre = '*'
                patternIndex -= 1

        if patternIndex == -1:
            return True
        else:
            return False


s = Solution()
print s.match('', '.*')

'''
aaa
ab*ac*a
'''
