# -*- coding:utf-8 -*-
class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        # write code here
        if array is None:
            return []
        xorResult = array[0]
        for i in range(1, len(array)):
            xorResult = xorResult ^ array[i]
        if xorResult == 0:
            return []

        index = 0
        while (xorResult & 1) == 0:
            xorResult=xorResult >> 1
            index += 1

        a = b = 0

        for itemArray in array:
            if self.isBit(itemArray, index):
                a = a ^ itemArray
            else:
                b = b ^ itemArray

        return [a, b]

    def isBit(self, data, index):
        data=data >> index
        return data & 1

a=[1,1,2,2,3,4,4,5]
s=Solution()
b=s.FindNumsAppearOnce(a)
print b