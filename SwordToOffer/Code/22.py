# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.stk = []

    def VerifySquenceOfBST(self, sequence):
        # write code here

        size = len(sequence)
        if sequence is None:
            return True
        if size==0:
            return False
        rootNode = sequence[-1]
        smallS = []
        bigS = []
        flag = True
        for i in range(size - 1):
            if sequence[i] < rootNode:
                if flag:
                    smallS.append(sequence[i])
                else:
                    return False
            elif sequence[i] > rootNode:
                if flag:
                    flag = False
                bigS.append(sequence[i])
            else:
                return False
        flagS=True
        if len(smallS)>0:
            flagS=self.VerifySquenceOfBST(smallS)
        flagB=True
        if len(bigS)>0:
            flagB=self.VerifySquenceOfBST(bigS)


        return flagS and flagB

s=Solution()
print s.VerifySquenceOfBST([1,2,3,4,5])