# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.s=[]

    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        # write code here
        a = []
        if root is None:
            return a

        self.s.append(root)
        a.append(root.val)
        while self.s:
            t=self.s[0]
            del self.s[0]
            if t.left is not None:
                self.s.append(t.left)
                a.append(t.left.val)
            if t.right is not None:
                self.s.append(t.right)
                a.append(t.right.val)

        return a



pRoot8 = TreeNode(8)
treeNode6 = TreeNode(6)
treeNode10 = TreeNode(10)
treeNode5 = TreeNode(5)
treeNode7 = TreeNode(7)
treeNode9 = TreeNode(9)
treeNode11 = TreeNode(11)

pRoot8.left = treeNode6
pRoot8.right = treeNode10
treeNode6.left = treeNode5
treeNode6.right = treeNode7
treeNode10.left = treeNode9
treeNode10.right = treeNode11

s=Solution()
print s.PrintFromTopToBottom(pRoot8)