# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1(self, n):
        # write code here
        count = 0
        c = 1

        for i in range(32):
            p = c & n
            if p != 0:
                count += 1
            c = c << 1

        return count

    def NumberOf1_2(self, n):
        count=0
        while n:
            count += 1
            n = (n - 1) & n
        return count



solution = Solution()
print solution.NumberOf1_2(-2)

