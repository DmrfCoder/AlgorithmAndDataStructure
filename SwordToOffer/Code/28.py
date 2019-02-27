# -*- coding:utf-8 -*-
class Solution:

    def siftUp(self, a, index):

        while (True):
            if index == 1:
                return a
            parentIndex = int(index / 2)
            if a[parentIndex] < a[index]:
                t = a[parentIndex]
                a[parentIndex] = a[index]
                a[index] = t
                index = parentIndex
            else:
                return a

    def siftDown(self, a, index):
        size = len(a) - 1
        while (True):
            index = 2 * index
            if index > size:
                return a

            if index + 1 <= size:
                if a[index + 1] > a[index]:
                    index += 1

            if a[index] > a[int(index / 2)]:
                t = a[index]
                a[index] = a[int(index / 2)]
                a[int(index / 2)] = t

    def makeHeap(self, a, k):
        for i in range(int(k / 2), 0, -1):
            a = self.siftDown(a, i)
        return a

    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        if tinput is None:
            return []

        size = len(tinput)
        if size < k or k==0:
            return []

        a = [0]
        a = a + tinput[0:k]
        a = self.makeHeap(a, k)
        for i in range(k, len(tinput)):
            if tinput[i] < a[1]:
                a[1] = tinput[i]
                a = self.siftDown(a, 1)

        a = sorted(a[1:])

        return a


s = Solution()
s.GetLeastNumbers_Solution([4, 5, 1, 6, 2, 7, 3, 8], 4)
