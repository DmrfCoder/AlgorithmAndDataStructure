# -*- coding:utf-8 -*-
'''
数据流的中位数
如何得到一个数据流中的中位数？如果从数据流中读出奇数个数值，那么中位数就是所有数值排序之后位于中间的数值。如果从数据流中读出偶数个数值，那么中位数就是所有数值排序之后中间两个数的平均值。我们使用Insert()方法读取数据流，使用GetMedian()方法获取当前读取数据的中位数。
'''


class Node:
    def __init__(self):
        self.left = None
        self.right = None
        self.val = None
        self.hight = 0




class Solution:
    def __init__(self):
        self.array = []

    def Insert(self, num):
        # write code here
        # [1,2,3,4]
        self.count += 1
        self.array.append(num)
        if self.count % 2 == 1:
            pass
        else:

            pass

    def GetMedian(self):
        pass

# write code here
