# -*- coding:utf-8 -*-
'''
和为s的两个数字
输入一个递增排序的数组和一个数字S，在数组中查找两个数，使得他们的和正好是S，如果有多对数字的和等于S，输出两个数的乘积最小的。
输出描述:
对应每个测试案例，输出两个数，小的先输出。
'''
class Solution:
    def FindNumbersWithSum(self, array, tsum):
        # write code here
        lowIndex = 0
        highIndex = len(array)-1
        while highIndex > lowIndex:
            sum = array[highIndex] + array[lowIndex]
            if sum == tsum:
                return [array[lowIndex], array[highIndex]]
            elif sum > tsum:
                highIndex-=1
            else:
                lowIndex += 1
        return []


s=Solution()
print s.FindNumbersWithSum([1,2,4,7,11,15],15)
