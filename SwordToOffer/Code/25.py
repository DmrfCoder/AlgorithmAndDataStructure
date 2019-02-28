# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def Convert(self, pRootOfTree):
        # write code here
        stack = []
        p = pRootOfTree
        a = []
        pre = None
        next = None
        preP = None
        head = None

        while len(stack) != 0 or p is not None:
            if p is not None:
                stack.append(p)
                p = p.left
            else:
                p = stack[-1]
                del stack[-1]
                if head is None:
                    head = p
                # a.append(p.val)
                p.left = preP

                if preP is not None:
                    preP.right = p
                preP = p

                p = p.right

        return head


def MidPrint(root):
    stack = []
    p = root
    a = []
    pre = None
    next = None
    preP = None
    head = None

    while len(stack) != 0 or p is not None:
        if p is not None:
            stack.append(p)
            p = p.left
        else:
            p = stack[-1]
            del stack[-1]
            if head is None:
                head = p
            # a.append(p.val)
            p.left = preP

            if preP is not None:
                preP.right = p
            preP = p

            p = p.right

    return head


pRoot1 = TreeNode(1)
treeNode2 = TreeNode(2)
treeNode3 = TreeNode(3)
treeNode4 = TreeNode(4)
treeNode5 = TreeNode(5)
treeNode6 = TreeNode(6)
treeNode7 = TreeNode(7)

pRoot1.left = treeNode2
pRoot1.right = treeNode3
treeNode2.left = treeNode4
treeNode2.right = treeNode5
treeNode3.left = treeNode6
treeNode3.right = treeNode7
s = Solution()
head = MidPrint(pRoot1)
a = 1
