# -*- coding:utf-8 -*-
class Solution:
    def FindContinuousSequence(self, tsum):
        # write code here
        arrayList = []
        for i in range(1, tsum):
            startIndex, array = self.findArray(tsum, i, [], 0)
            if startIndex == -1:
                continue
            else:
                i = i + startIndex
                arrayList.append(array)
        return arrayList

    def findArray(self, tsum, startIndex, array, sum):
        if startIndex == tsum - 1:
            return -1, []
        for i in range(startIndex, tsum):
            sum += i
            array.append(i)

            if sum == tsum:
                return startIndex, array
            elif sum < tsum:
                array.append(i)
            else:
                startIndex += 1
                sum -= array[0]
                del array[0]
        return -1, []


s = Solution()
t = s.FindContinuousSequence(10)
print t
