# -*- coding:utf-8 -*-
class Solution:
    def GetNumberOfK(self, data, k):
        # write code here
        size = len(data)
        if size == 0:
            return 0
        if k > data[-1] or k < data[0]:
            return 0

        count = 0

        startIndex = 0
        endIndex = size - 1

        index = size - 1

        while True:
            if index < 0 or index > size:
                break
            if data[index] > k:
                endIndex = index
                index = int((startIndex + endIndex) / 2)
            elif data[index] > k:
                startIndex = index
                index = int((startIndex + endIndex) / 2)

            else:
                for i in range(index, -1, -1):
                    if data[i] == k:
                        count += 1

                    else:
                        break

                for i in range(index + 1, size):
                    if data[i] == k:
                        count += 1
                    else:
                        break
                break

        return count


a = [1, 2, 3, 4, 5, 5]
s = Solution()
count = s.GetNumberOfK(a, 5)
print count
