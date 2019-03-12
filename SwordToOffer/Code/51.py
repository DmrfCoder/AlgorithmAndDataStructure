# -*- coding:utf-8 -*-
'''
给定一个数组A[0,1,...,n-1],请构建一个数组B[0,1,...,n-1],其中B中的元素B[i]=A[0]*A[1]*...*A[i-1]*A[i+1]*...*A[n-1]。不能使用除法。
'''
class Solution:
    def multiply(self, A):
        # write code here
        size=len(A)
        array=[]

        itemArray=[]
        for j in range(size):
            if j==0:
                itemArray.append(1)
            else:
                value=itemArray[-1]*A[j-1]
                itemArray.append(value)

        itemArray2 = [1]*size
        for j in range(size-1,-1,-1):
            if j == size-1:
                itemArray2[j]=1
            else:
                value = itemArray2[j+1] * A[j+1]
                itemArray2[j]=value


        b=[]
        for j in range(size):
            b.append(itemArray[j]*itemArray2[j])
        return b

s=Solution()
print s.multiply([1,2,3,4])





