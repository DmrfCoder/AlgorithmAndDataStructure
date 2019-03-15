# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回对应节点TreeNode
    def KthNode(self, pRoot, k):
        # write code here
        if k == 0:
            return None

        a = []
        index = 0
        topNode = pRoot

        while len(a) != 0 or topNode is not None:
            if topNode is not None:
                a.append(topNode)
                topNode = topNode.left
            else:
                topNode = a[-1]
                del a[-1]
                index += 1
                if index == k:
                    return topNode
                topNode = topNode.right


s = Solution()
pRoot = TreeNode(8)
node1 = TreeNode(6)
node2 = TreeNode(10)
node3 = TreeNode(5)
node4 = TreeNode(7)
node5 = TreeNode(9)
node6 = TreeNode(11)

pRoot.left = node1
pRoot.right = node2
node1.left = node3
node1.right = node4
node2.left = node5
node2.right = node6

print s.KthNode(pRoot, 2).val
