# -*- coding:utf-8 -*-
class Solution:
    def jumpFloor(self, number):
        a=1
        b=2

        # write code here
        if number == 1:
            return 1
        elif number == 2:
            return 2
        else:
            number=number-2
            while number != 0:
                c=a+b
                a=b
                b=c
                number -= 1

            return b


solution = Solution()
print solution.jumpFloor(4)
