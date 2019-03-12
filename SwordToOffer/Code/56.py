# -*- coding:utf-8 -*-
'''
矩阵中的路径
请设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串所有字符的路径。路径可以从矩阵中的任意一个格子开始，每一步可以在矩阵中向左，向右，向上，向下移动一个格子。如果一条路径经过了矩阵中的某一个格子，则之后不能再次进入这个格子。 例如 a b c e s f c s a d e e 这样的3 X 4 矩阵中包含一条字符串"bcced"的路径，但是矩阵中不包含"abcb"路径，因为字符串的第一个字符b占据了矩阵中的第一行第二个格子之后，路径不能再次进入该格子。
'''

'''
a b c e 
s f c s 
a d e e 

ok:bcced
not ok:abcb

ABCE
SFCS
ADEE

ABCCED
'''

import copy


class Solution:
    def hasPath(self, matrix, rows, cols, path):
        # write code here
        matrix = list(matrix)

        for row in range(rows):
            for col in range(cols):
                flag = self.dfs(copy.copy(matrix), row, col, rows, cols, path)
                if flag:
                    return True

        return False

    def dfs(self, matrix, x, y, rows, cols, path):
        index = x * cols + y

        if len(path) == 0:
            return True
        if index >= len(matrix) or index < 0 or matrix[index] != path[0] or matrix[index] == None:
            return False

        matrix[index] = None
        flag1 = self.dfs(copy.copy(matrix), x + 1, y, rows, cols, path[1:])
        flag2 = self.dfs(copy.copy(matrix), x - 1, y, rows, cols, path[1:])
        flag3 = self.dfs(copy.copy(matrix), x, y + 1, rows, cols, path[1:])
        flag4 = self.dfs(copy.copy(matrix), x, y - 1, rows, cols, path[1:])

        return flag1 or flag2 or flag3 or flag4


'''
ABCEHJIG
SFCSLOPQ
ADEEMNOE
ADIDEJFM
VCEIFGGS

SLHECCEIDEJFGGFIE
'''
s = Solution()
print s.hasPath('ABCEHJIGSFCSLOPQADEEMNOEADIDEJFMVCEIFGGS', 5, 8, 'SLHECCEIDEJFGGFIE')
