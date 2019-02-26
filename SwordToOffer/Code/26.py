# -*- coding:utf-8 -*-
class Solution:
    def Permutation(self, ss):
        # write code here
        if len(ss)==1:
            return ss

        t = self.Permutation(ss[1:])


s = Solution()
s.Permutation('abcd')
