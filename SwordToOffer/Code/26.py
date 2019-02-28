# -*- coding:utf-8 -*-
class Solution:

    def swap(self, arr, one, two):
        arr = list(arr)
        t = arr[one]
        arr[one] = arr[two]
        arr[two] = t
        return ''.join(arr)

    def Permutation(self, ss):
        # write code here
        if ss is None:
            return []
        if len(ss)==0:
            return []
        if len(ss) == 1:
            return [ss]
        size = len(ss)
        t = self.Permutation(ss[1:])
        arr = []
        for i in range(len(t)):
            t[i] = ss[0] + t[i]
            arr.append(t[i])
            for j in range(1, size):
                if t[i][0]==t[i][j]:
                    continue
                arr.append(self.swap(t[i], 0, j))
        return arr

    def Permutation2(self,ss):
        intSs=[]



s = Solution()
print s.Permutation('aab')
