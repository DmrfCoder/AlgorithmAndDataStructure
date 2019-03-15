# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetrical(self, pRoot):
        if pRoot is None:
            return True
        return self.cmpRoot(pRoot.left, pRoot.right)

    def cmpRoot(self, root1, root2):
        if root1 == None and root2 == None:
            return True
        elif root1 == None or root2 == None:
            return False
        if root1.val != root2.val:
            return False

        return self.cmpRoot(root1.left, root2.right) and self.cmpRoot(root1.right, root2.left)


s = Solution()
pRoot = TreeNode(8)
node1 = TreeNode(6)
node2 = TreeNode(6)
node3 = TreeNode(5)
node4 = TreeNode(7)
node5 = TreeNode(7)
node6 = TreeNode(5)

pRoot.left = node1
pRoot.right = node2
node1.left = node3
node1.right = node4
node2.left = node5
node2.right = node6

print s.isSymmetrical(pRoot)
