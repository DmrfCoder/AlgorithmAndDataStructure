# -*- coding:utf-8 -*-
'''
机器人的运动范围
地上有一个m行和n列的方格。一个机器人从坐标0,0的格子开始移动，每一次只能向左，右，上，下四个方向移动一格，但是不能进入行坐标和列坐标的数位之和大于k的格子。 例如，当k为18时，机器人能够进入方格（35,37），因为3+5+3+7 = 18。但是，它不能进入方格（35,38），因为3+5+3+8 = 19。请问该机器人能够达到多少个格子？
'''


class Solution:
    def movingCount(self, threshold, rows, cols):
        # write code here
        array = [[0 for col in range(cols)] for row in range(rows)]
        tempSum = self.dfs(array, 0, 0, threshold)
        return tempSum

    def dfs(self, array, x, y, threshold):

        if x < 0 or y < 0 or x >= len(array) or y >= len(array[0]) or array[x][y] == 1 or self.getSum(x) + self.getSum(
                y) > threshold:
            return 0
        sum = 1

        array[x][y] = 1
        sum += self.dfs(array, x + 1, y, threshold)
        sum += self.dfs(array, x - 1, y, threshold)
        sum += self.dfs(array, x, y + 1, threshold)
        sum += self.dfs(array, x, y - 1, threshold)
        return sum

    def getSum(self, x):
        sum = 0
        t = 10
        while x != 0:
            tempX = x % t
            sum += tempX
            x = x / t
        return sum


class Solution2:
    def __init__(self):
        self.count = 0

    def movingCount(self, threshold, rows, cols):
        # write code here
        arr = [[1 for i in range(cols)] for j in range(rows)]
        self.findway(arr, 0, 0, threshold)
        return self.count

    def findway(self, arr, i, j, k):
        if i < 0 or j < 0 or i >= len(arr) or j >= len(arr[0]):
            return
        tmpi = list(map(int, list(str(i))))
        tmpj = list(map(int, list(str(j))))
        if sum(tmpi) + sum(tmpj) > k or arr[i][j] != 1:
            return
        print i, j, arr[i][j]
        arr[i][j] = 0
        self.count += 1
        self.findway(arr, i + 1, j, k)
        self.findway(arr, i - 1, j, k)
        self.findway(arr, i, j + 1, k)
        self.findway(arr, i, j - 1, k)


s = Solution()
print s.movingCount(10, 1, 100)
