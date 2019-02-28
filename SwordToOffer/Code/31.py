# -*- coding:utf-8 -*-

def cmp(str1, str2):
    s1 = str1 + str2
    s2 = str2 + str1
    if int(s1) < int(s2):
        return -1
    else:
        return 0


class Solution:

    def PrintMinNumber(self, numbers):
        # write code here
        if numbers is None:
            return ""
        if len(numbers) == 0:
            return ""

        strs = []
        for item in numbers:
            strs.append(str(item))

        strs.sort(cmp)
        print strs

        r = ''
        for item in strs:
            r = r + item

        return int(r)


s = Solution()
print s.PrintMinNumber([3, 5, 1, 4, 2])
