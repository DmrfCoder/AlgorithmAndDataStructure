# -*- coding:utf-8 -*-
def cmp(a, b):
    if a < b:
        return 0
    else:
        return -1


class Solution:

    def InversePairs(self, data):
        # write code here
        size = len(data)
        count = 0
        for i in range(size - 1, -1, -1):
            for j in range(i - 1, -1, -1):
                if data[i] < data[j]:
                    count += 1

        return count % 1000000007


def GuiBingSort(data):
    size = len(data)
    if size == 2:
        if data[0] < data[1]:
            return data
        else:
            return [data[1], data[0]]

    if size==0:
        return data

    index=int(size/2)
    return GuiBingSort(data[0:index])+GuiBingSort(data[index:])


s = Solution()
#print s.InversePairs([1, 2, 3, 4, 5, 6, 7, 0])
print GuiBingSort([1, 2, 3, 4, 5, 6, 7, 0])