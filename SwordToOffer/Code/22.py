# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.stk=[]

    def VerifySquenceOfBST(self, sequence):
        # write code here
        a=[]
        flag=0
        for i in range(len(sequence)):
            if sequence[i]<sequence[i+1] :
                if flag==0:
                    flag=1
                else:



