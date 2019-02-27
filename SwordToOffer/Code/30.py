# -*- coding:utf-8 -*-
class Solution:

    def PrintMinNumber(self, numbers):
        # write code here
        if numbers is None:
            return ""
        if len(numbers)==0:
            return ""
        strs = []
        for item in numbers:
            strs.append(str(item))

        z = sorted(strs, cmp)

        r=''

        for item in z:
            r=r+item


        return int(r)


def cmp(str1, str2):
    s1 = str1 + str2
    s2 = str2 + str1

    if int(s1) < int(s2):
        return -1
    else:
        return 0


s = Solution()
print s.PrintMinNumber([3,32,321])
