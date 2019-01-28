# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, node):
        # write code here
        self.stack1.append(node)

    def pop(self):
        # return xx
        self.stack2 = []

        while len(self.stack1) != 1:
            self.stack2.append(self.stack1.pop())

        node = self.stack1.pop()

        while self.stack2:
            self.stack1.append(self.stack2.pop())

        return node


solution = Solution()
solution.push(1)
solution.push(2)
solution.push(3)
solution.push(4)

print solution.pop()
print solution.pop()
print solution.pop()
print solution.pop()
