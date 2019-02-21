# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def FirstBrowse(self, pRoot):
        result = []
        if pRoot == None:
            return result
        else:
            result.append(pRoot.val)
            result = result + self.FirstBrowse(pRoot.left)
            result = result + self.FirstBrowse(pRoot.right)
        return result

class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        # write code here
        if pRoot1 == None or pRoot2 == None:
            return False
        flag = False
        if pRoot1.val == pRoot2.val:
            flag = self.doseNode1HasNode2(pRoot1, pRoot2)

        if not flag:
            flag = self.HasSubtree(pRoot1.left, pRoot2)

        if not flag:
            flag = self.HasSubtree(pRoot1.right, pRoot2)

        return flag

    def doseNode1HasNode2(self, Node1, Node2):
        if Node2 == None:
            return True
        if Node1 == None:
            return False
        if Node1.val != Node2.val:
            return False

        return self.doseNode1HasNode2(Node1.left, Node2.left) and self.doseNode1HasNode2(Node1.right, Node2.right)


pRoot1 = TreeNode(1)
treeNode1 = TreeNode(2)
treeNode2 = TreeNode(3)
treeNode3 = TreeNode(4)
treeNode4 = TreeNode(5)
treeNode5 = TreeNode(6)
treeNode6 = TreeNode(7)
pRoot1.left = treeNode1
pRoot1.right = treeNode2
treeNode1.left = treeNode3
treeNode1.right = treeNode4
treeNode2.left = treeNode5
treeNode2.right = treeNode6

pRoot2 = TreeNode(1)
treeNode1b = TreeNode(2)
treeNode2b = TreeNode(3)
treeNode3b = TreeNode(4)
treeNode4b = TreeNode(6)
treeNode5b = TreeNode(7)
pRoot2.left = treeNode1b
pRoot2.right = treeNode2b
treeNode2b.left = treeNode3b
treeNode2b.right = treeNode4b
treeNode3b.left = treeNode5b

solution = Solution()
print solution.HasSubtree(pRoot1, pRoot2)
