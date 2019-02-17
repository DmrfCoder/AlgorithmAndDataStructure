# -*- coding:utf-8 -*-
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here

        length = len(rotateArray)

        if length == 0:
            return 0

        for i in range(length-1, 0, -1):
            if rotateArray[i - 1] > rotateArray[i]:
                return rotateArray[i]


solution=Solution()
print solution.minNumberInRotateArray([3,4,5,1,2])
