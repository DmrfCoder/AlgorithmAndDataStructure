# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def Print(self, pRoot):
        # write code here
        if pRoot is None:
            return []
        a = []
        b = []
        flag = 0
        res = []

        a.append(pRoot)
        res.append([pRoot.val])

        while len(a) != 0 or len(b) != 0:
            if flag == 0:
                curNode = a[0]
                del a[0]

                if curNode.left is not None:
                    b.append(curNode.left)

                if curNode.right is not None:
                    b.append(curNode.right)

                if len(a) == 0:
                    flag = 1
                    temp = []
                    for itemB in b:
                        temp.append(itemB.val)
                    if len(temp) != 0:
                        temp.reverse()
                        res.append(temp)

            else:
                curNode = b[0]
                del b[0]
                if curNode.left is not None:
                    a.append(curNode.left)
                if curNode.right is not None:
                    a.append(curNode.right)
                if len(b) == 0:
                    flag = 0
                    temp = []
                    for itemA in a:
                        temp.append(itemA.val)
                    if len(temp) != 0:
                        res.append(temp)

        return res


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

print s.Print(pRoot)
