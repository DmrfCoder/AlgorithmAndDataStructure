# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        # write code here
        strN = str(n)
        size = len(strN)
        sum = 0

        # 从个位开始
        for i in range(size - 1, -1, -1):
            curBit = int(strN[i])
            multiValue = pow(10, size - 1 - i)
            if i == 0:
                biggerValue = 0
            else:
                biggerValue = strN[0:i]
            if i == size - 1:
                smallerValue = 0
            else:
                smallerValue = strN[i + 1:]

            if curBit == 1:
                count = int(biggerValue) * multiValue + int(smallerValue) + 1
            elif curBit == 0:
                count = int(biggerValue) * multiValue
            else:
                count = (int(biggerValue) + 1) * multiValue

            sum += count

        return sum


s = Solution()
print s.NumberOf1Between1AndN_Solution(13)
