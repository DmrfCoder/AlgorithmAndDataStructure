# -*- coding:utf-8 -*-
class Solution:
    def FindGreatestSumOfSubArray(self, array):
        # write code here
        res = array[0]
        f = array[0]

        size = len(array)

        for i in range(1, size):
            f = max(array[i], array[i] + f)
            res = max(res, f)

        return res


s = Solution()
print s.FindGreatestSumOfSubArray([1, -2, 3, 10, -4, 7, 2, -5])
