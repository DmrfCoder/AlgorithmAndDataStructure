# -*- coding:utf-8 -*-
import numpy as np


class Solution:


    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        # write code here
        size = len(matrix)

        newArray = []
        if size==1:
            newArray.append(matrix[0][0])
            return newArray

        for index1 in range(0, size):
            for index2 in range(index1, size - index1 - 1):
                newArray.append(matrix[index1][ index2])
            for index3 in range(index1, size - index1 - 1):
                newArray.append(matrix[index3][ size - index1 - 1])
            for index4 in range(size - index1 - 1, index1, -1):
                newArray.append(matrix[size - index1 - 1][ index4])
            for index5 in range(size - index1 - 1, index1, -1):
                newArray.append(matrix[index5][ index1])

        return newArray

    def reversematrix(self,matrix):
        s=matrix.shape
        newmatrix=[]
        for i in range(s[1]-1,-1,-1):
            a=[]
            for j in range(s[0]):
                a.append(matrix[j][i])
            newmatrix.append(a)
        newmatrix=np.array(newmatrix)
        return newmatrix

    def printMatrix2(self, matrix):
        newArray=[]
        matrix=np.array(matrix)
        while len(matrix)!=0:
            newArray.extend(matrix[0])
            matrix=matrix[1:]
            matrix=self.reversematrix(matrix)
        return newArray


s = Solution()
#print s.printMatrix([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
print s.printMatrix([[1]])
