# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回二维列表[[1,2],[4,5]]
    def Print(self, pRoot):
        # write code here
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
