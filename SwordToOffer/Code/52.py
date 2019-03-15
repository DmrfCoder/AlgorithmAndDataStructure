# -*- coding:utf-8 -*-
'''
请实现一个函数用来匹配包括'.'和'*'的正则表达式。模式中的字符'.'表示任意一个字符，而'*'表示它前面的字符可以出现任意次（包含0次）。 在本题中，匹配是指字符串的所有字符匹配整个模式。例如，字符串"aaa"与模式"a.a"和"ab*ac*a"匹配，但是与"aa.a"和"ab*a"均不匹配
'''


class Solution:
    # s, pattern都是字符串
    def match(self, s, pattern):
        # write code here

        sizeS = len(s)
        sizeP = len(pattern)

        if s == '' and pattern == '':
            return True

        if s != '' and pattern == '':
            return False

        indexS = 0
        indexP = 0
        if indexS + 1 >= sizeS:
            temps = ''
        else:
            temps = s[indexS + 1:]

        if indexP + 1 >= sizeP:
            tempp = ''
            arrayp = ''
        else:
            tempp = pattern[indexP + 1]
            arrayp = pattern[indexP + 1:]

        if indexP + 2 >= sizeP:
            arrayp2 = ''
        else:
            arrayp2 = pattern[indexP + 2:]

        if s == '':
            curS = ''
        else:
            curS = s[indexS]

        if tempp != '*':
            if curS == pattern[indexP]:
                return self.match(temps, arrayp)
            elif pattern[indexP] == '.' and s != '':
                return self.match(temps, arrayp)
            else:
                return False
        else:
            if pattern[indexP] == curS:
                return self.match(temps, pattern) or self.match(s, arrayp2)
            elif pattern[indexP] == '.' and s != '':
                return self.match(temps, pattern) or self.match(s, arrayp2)
            else:
                return self.match(s, arrayp2)


s = Solution()
print s.match("bbbba", ".*a*a")
'''
aaa
ab*ac*a
'''
