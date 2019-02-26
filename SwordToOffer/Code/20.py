# -*- coding:utf-8 -*-
class Solution:
    def IsPopOrder(self, pushV, popV):
        # write code here
        size = len(pushV)
        popIndex = 0
        a = []
        for i in range(size):
            if pushV[i] == popV[popIndex]:
                popIndex += 1
            else:
                a.append(pushV[i])

        if len(a)==0:
            return True

        if popIndex >= size:
            return False
        else:
            size2 = len(a)
            if size2 != size - popIndex:
                return False
            else:
                flag = True
                for i in range(size2):
                    if a[i] != popV[- (i+1)]:
                        flag = False
                        break
                    else:
                        popIndex += 1
                return flag


s = Solution()
print s.IsPopOrder([1], [1])
