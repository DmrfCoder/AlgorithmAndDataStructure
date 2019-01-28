# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        # write code here
        headNode = TreeNode(pre[0])

        centureIndex = tin.index(pre[0])
        left = tin[0:centureIndex]
        right = tin[centureIndex + 1:]

        if len(left) == 0:
            leftNode = None
        elif len(left) == 1:
            leftNode = TreeNode(left[0])
        else:
            leftNode = self.reConstructBinaryTree(pre[1:1 + len(left)], left)

        if len(right) == 0:
            rightNode = None
        elif len(right) == 1:
            rightNode = TreeNode(right[0])

        else:
            rightNode = self.reConstructBinaryTree(pre[1 + len(left):], right)

        headNode.left = leftNode
        headNode.right = rightNode

        return headNode


solution = Solution()

pre = [1, 2, 4, 3, 5, 6]
tin = [4, 2, 1, 5, 3, 6]

headNode = solution.reConstructBinaryTree(pre, tin)
print headNode
