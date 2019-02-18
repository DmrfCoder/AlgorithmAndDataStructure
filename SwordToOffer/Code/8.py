# -*- coding:utf-8 -*-
class Solution:
    def jumpFloorII(self, number):
        # write code here
        if number == 1:
            return 1
        elif number == 2:
            return 2
        else:
            return 2 * self.jumpFloorII(number - 1)


solution = Solution()
print solution.jumpFloorII(4)
