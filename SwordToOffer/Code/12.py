# -*- coding:utf-8 -*-
class Solution:
    def reOrderArray(self, array):
        # write code here

        jiCount = 0
        ouCount = 0

        for itemArray in array:
            if itemArray % 2 == 0:
                ouCount += 1
            else:
                jiCount += 1

        jiIndex = 0
        ouIndex = jiCount

        arraySize = len(array)
        newArray = [0] * arraySize

        for i in range(arraySize):
            if array[i] % 2 == 1:
                newArray[jiIndex] = array[i]
                jiIndex += 1

            else:
                newArray[ouIndex] = array[i]
                ouIndex += 1

        return newArray


solution = Solution()
print solution.reOrderArray([1, 2, 3, 4, 5])
