# -*- coding:utf-8 -*-
class Solution:
    def GetUglyNumber_Solution(self, index):
        # write code here
        if index==0:
            return 0

        t2Index = 0
        t3Index = 0
        t5Index = 0

        res = [1]

        for i in range(0, index - 1):
            minValue = min(res[t2Index] * 2, min(res[t3Index] * 3, res[t5Index] * 5))
            res.append(minValue)
            if minValue == res[t2Index] * 2:
                t2Index += 1
            if minValue == res[t3Index] * 3:
                t3Index += 1
            if minValue == res[t5Index] * 5:
                t5Index += 1

        return res[-1]


s = Solution()
print s.GetUglyNumber_Solution(7)
