# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.a = []
        self.b = []
        self.count = 0

    def push(self, node):
        # write code here
        if self.count == 0:
            self.b.append(node)
            self.count += 1

        elif node < self.b[-1]:
            self.b.append(node)
            self.count += 1
        else:
            self.b.append(self.b[-1])
            self.count += 1
        self.a.append(node)

    def pop(self):
        # write code here
        r = self.a[-1]
        self.a.pop()
        self.b.pop()
        self.count -= 1
        return r

    def top(self):
        # write code here
        return self.a[-1]

    def min(self):
        # write code here
        return self.b[-1]


a = ["PSH3", "MIN", "PSH4", "MIN", "PSH2", "MIN", "PSH3", "MIN", "POP", "MIN", "POP", "MIN", "POP", "MIN", "PSH0",
     "MIN"]

s = Solution()
for item_a in a:
    s.push(item_a)

for i in range(len(a)):
    print s.min()
    s.pop()
