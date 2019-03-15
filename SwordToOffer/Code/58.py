# -*- coding:utf-8 -*-
'''
数据流的中位数
如何得到一个数据流中的中位数？如果从数据流中读出奇数个数值，那么中位数就是所有数值排序之后位于中间的数值。如果从数据流中读出偶数个数值，那么中位数就是所有数值排序之后中间两个数的平均值。我们使用Insert()方法读取数据流，使用GetMedian()方法获取当前读取数据的中位数。
'''


# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.maxHeap = []
        self.minHeap = []

    def Insert(self, num):
        # write code here
        if len(self.minHeap) != 0:
            if num < self.minHeap[0]:
                self.maxHeapInsert(num)
            else:
                self.minHeapInsert(num)
        else:
            self.minHeapInsert(num)

        if len(self.minHeap) - len(self.maxHeap) == 2:
            self.maxHeapInsert(self.minHeap[0])
            self.minHeapDeleteTop()

        if len(self.minHeap) + 1 == len(self.maxHeap):
            self.minHeapInsert(self.maxHeap[0])
            self.maxHeapDeleteTop()

    def maxHeapInsert(self, num):
        self.maxHeap.append(num)
        size = len(self.maxHeap)
        index = size - 1
        while index >= 0:
            if self.maxHeap[index] > self.maxHeap[int(index / 2)]:
                temp = self.maxHeap[index]
                self.maxHeap[index] = self.maxHeap[int(index / 2)]
                self.maxHeap[int(index / 2)] = temp
                index = int(index / 2)

            else:
                break

    def maxHeapDeleteTop(self):
        t = self.maxHeap[0]
        self.maxHeap[0] = self.maxHeap[-1]
        del self.maxHeap[-1]
        size = len(self.maxHeap)
        index = 0
        while index * 2 + 1 < size:
            nextIndex = index * 2 + 1
            if nextIndex + 1 < size and self.maxHeap[nextIndex+ 1] > self.maxHeap[nextIndex]:
                nextIndex += 1
            if self.maxHeap[nextIndex] > self.maxHeap[index]:
                temp = self.maxHeap[nextIndex]
                self.maxHeap[nextIndex] = self.maxHeap[index]
                self.maxHeap[index] = temp
                index = nextIndex
            else:
                break
        return t

    def minHeapDeleteTop(self):
        t = self.minHeap[0]
        self.minHeap[0] = self.minHeap[-1]
        del self.minHeap[-1]
        index = 0
        size = len(self.minHeap)
        while index * 2 + 1 < size:
            nextIndex = index * 2 + 1
            if nextIndex + 1 < size and self.minHeap[nextIndex + 1] < self.minHeap[nextIndex]:
                nextIndex += 1
            if self.minHeap[nextIndex] < self.minHeap[index]:
                temp = self.minHeap[index]
                self.minHeap[index] = self.minHeap[nextIndex]
                self.minHeap[nextIndex] = temp
                index = nextIndex

            else:
                break
        return t

    def minHeapInsert(self, num):
        self.minHeap.append(num)
        size = len(self.minHeap)
        index = size - 1
        while index >= 0:
            if self.minHeap[index] < self.minHeap[int(index / 2)]:
                temp = self.minHeap[index]
                self.minHeap[index] = self.minHeap[int(index / 2)]
                self.minHeap[int(index / 2)] = temp
                index = int(index / 2)
            else:
                break

    def GetMedian(self,n=None):
        # write code here
        if len(self.minHeap) == len(self.maxHeap):
            return (self.minHeap[0] + self.maxHeap[0]) / 2.0
        else:
            return self.minHeap[0]

s=Solution()
#5,2,3,4,1,6,7,0,8
s.Insert(5)
print s.GetMedian()
s.Insert(2)
print s.GetMedian()
s.Insert(3)
print s.GetMedian()
s.Insert(4)
print s.GetMedian()
s.Insert(1)
print s.GetMedian()
s.Insert(6)
print s.GetMedian()
s.Insert(7)
print s.GetMedian()
s.Insert(0)
print s.GetMedian()
s.Insert(8)
print s.GetMedian()