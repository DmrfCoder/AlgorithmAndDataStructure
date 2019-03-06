# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def TreeDepth(self, pRoot):
        # write code here
        if pRoot is None:
            return 0

        deepth1 = self.TreeDepth(pRoot.left)
        if deepth1==-1:
            return -1
        deepth2 = self.TreeDepth(pRoot.right)
        if deepth2==-1:
            return -1
        if abs(deepth1 - deepth2) > 1:
            return -1
        return max(1 + deepth1, 1 + deepth2)

    def IsBalanced_Solution(self, pRoot):
        # write code here
        if pRoot is None:
            return True
        deepth1 = self.TreeDepth(pRoot)

        if deepth1 == -1:
            return False
        return True
