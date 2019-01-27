# -*- coding:utf-8 -*-
'''
在一个二维数组中（每个一维数组的长度相同），每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。
请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。

'''
class Solution:
    # array 二维列表
    def Find(self, target, array):
        for row in array:
            for column in row:
                if column == target:
                    return True
        return False

    def Find2(self, target, array):
        arrayRowLength = len(array)
        arrayColumnLength = len(array[0])
        rowIndex = arrayRowLength - 1
        columnIndex = 0

        while (arrayRowLength > rowIndex >= 0 and 0 <= columnIndex < arrayColumnLength):
            if target < array[rowIndex][columnIndex]:
                rowIndex -= 1
            elif target > array[rowIndex][columnIndex]:
                columnIndex += 1
            elif target == array[rowIndex][columnIndex]:
                return True
        return False


# array = [[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6], [4, 5, 10, 7]]
array = [[]]
target = 10
solution = Solution()
print solution.Find2(target, array)
