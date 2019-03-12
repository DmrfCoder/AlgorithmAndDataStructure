# coding:utf-8
'''
最大陆地问题：
给定一个二维数组，数组的值非0即1，0代表海洋，1代表陆地，求该数组代表的区域陆地的最大面积。

'''

'''
深度优先搜索
'''


def maxArea(array):
    sizeX = len(array)
    sizeY = len(array[0])
    sum = 0
    for x in range(sizeX):
        for y in range(sizeY):
            if array[x][y] == 1:
                tempSum = dfs(array, x, y)
                if tempSum > sum:
                    sum = tempSum
    return sum


def dfs(array, x, y):
    sizeX = len(array)
    sizeY = len(array[0])

    if x < 0 or x >= sizeX or y < 0 or y >= sizeY or array[x][y] != 1:
        return 0

    sum = 1
    array[x][y] = 0
    sum += dfs(array, x + 1, y)
    sum += dfs(array, x - 1, y)
    sum += dfs(array, x, y - 1)
    sum += dfs(array, x, y + 1)
    return sum


'''
广度优先搜索：
如果发现陆地，就将其标记，然后广度搜索标记并计数与其相邻的点
'''


def bfs(array, x, y, tempSum, sizeX, sizeY):
    if x < 0 or y < 0 or x >= sizeX or y >= sizeY:
        return 0
    array[x][y] = 0
    tempSum += 1
    queue = []
    queue.append([x, y])

    while len(queue) != 0:
        tempX, tempY = queue[0][0], queue[0][1]
        del queue[0]
        if tempX + 1 < sizeX and array[tempX + 1][tempY] == 1:
            array[tempX + 1][tempY] = 0
            tempSum += 1
            queue.append([tempX + 1, tempY])

        if tempX - 1 >= 0 and array[tempX - 1][tempY] == 1:
            array[tempX - 1][tempY] = 0
            tempSum += 1
            queue.append([tempX - 1, tempY])

        if tempY - 1 >= 0 and array[tempX][tempY - 1] == 1:
            array[tempX][tempY - 1] = 0
            tempSum += 1
            queue.append([tempX, tempY - 1])

        if tempY + 1 < sizeY and array[tempX][tempY + 1] == 1:
            array[tempX][tempY + 1] = 0
            tempSum += 1
            queue.append([tempX, tempY + 1])

    return tempSum


def maxAreaBfs(array):
    sizeX = len(array)
    sizeY = len(array[0])
    sum = 0
    for x in range(sizeX):
        for y in range(sizeY):
            if array[x][y] == 1:
                tempSum = bfs(array, x, y, 0, sizeX, sizeY)
                if tempSum > sum:
                    sum = tempSum
    return sum


a = [[1, 1, 1, 0, 0, 0],
     [0, 1, 1, 0, 0, 0],
     [1, 0, 0, 0, 1, 1],
     [0, 0, 0, 0, 0, 1],
     [1, 1, 1, 1, 0, 0],
     [1, 0, 1, 0, 0, 0]]
print maxArea(a)
