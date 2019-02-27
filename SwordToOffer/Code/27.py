# -*- coding:utf-8 -*-
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        if numbers is None:
            return 0

        size = len(numbers)

        if size == 0:
            return 0
        if size == 1:
            return numbers

        soldier = numbers[0]
        soldierCount = 1
        soldierIndex = 0
        flag = False
        for i in range(1, size):
            if numbers[i] != soldier:
                soldierCount -= 1
                if soldierCount == 0:
                    soldierIndex += 1
                    soldier = numbers[soldierIndex]
                    soldierCount = 1
                    flag = False
            else:
                flag = True
                soldierCount += 1

        if soldierCount > 1:
            return soldier
        elif soldierCount == 1 and flag:
            return soldier
        else:
            return 0


s = Solution()
print s.MoreThanHalfNum_Solution([1])
