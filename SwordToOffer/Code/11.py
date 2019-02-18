# -*- coding:utf-8 -*-
class Solution:
    def Power(self, base, exponent):
        # write code here
        if base == 0:
            return 0
        if exponent == 0:
            return 1
        flag = 1
        if exponent < 0:
            flag = 0
            exponent = -exponent

        sum = 1.0
        tmp = base
        while (exponent > 0):
            if exponent & 1 == 1:
                sum *= tmp
            tmp *= tmp
            exponent = exponent >> 1

        if flag == 0:
            sum = 1 / sum

        return sum


solution = Solution()
# 00..11
print solution.Power(3, 2)
