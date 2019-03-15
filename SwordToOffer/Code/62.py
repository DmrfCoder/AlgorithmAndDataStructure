# -*- coding:utf-8 -*-
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None


class Solution:
    def GetNext(self, pNode):
        # write code here
        if pNode.right is not None:
            rightNode = pNode.right
            while rightNode.left is not None:
                rightNode = rightNode.left
            return rightNode
        else:
            parent = pNode.next
            curNode = pNode
            if parent == None:
                return None
            while parent.right == curNode:
                curNode = parent
                parent = parent.next
                if parent == None:
                    return None

            return parent
