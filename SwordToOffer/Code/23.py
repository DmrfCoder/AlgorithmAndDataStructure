# -*- coding:utf-8 -*-
import copy


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def cmp(a, b):
    if len(a) > len(b):
        return -1
    else:
        return 0


class Solution:

    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        # write code here
        if root == None:
            return []

        if root.val==expectNumber:
            return [[1]]
        if root.val>expectNumber:
            return []

        result = []
        a = []
        root.val = [root.val]
        a.append(root)




        while a:
            cnode = a[0]
            del a[0]


            if cnode.left != None:
                c = sum(cnode.val) + cnode.left.val
                if c < expectNumber:
                    temp = copy.copy(cnode.left.val)
                    cnode.left.val = copy.copy(cnode.val)
                    cnode.left.val.append(temp)
                    a.append(cnode.left)
                elif c > expectNumber:
                    cnode.left = None
                elif cnode.left.left == None and cnode.left.right == None:
                    t = copy.copy(cnode.val)
                    t.append(cnode.left.val)
                    result.append(t)

            if cnode.right != None:
                c = sum(cnode.val)+ cnode.right.val
                if c < expectNumber:
                    temp = copy.copy(cnode.right.val)
                    cnode.right.val = copy.copy(cnode.val)
                    cnode.right.val.append(temp)

                    a.append(cnode.right)
                elif c > expectNumber:
                    cnode.right = None
                elif cnode.right.left == None and cnode.right.right == None:
                    t = copy.copy(cnode.val)
                    t.append(cnode.right.val)
                    result.append(t)

        result=sorted(result,cmp )
        return result


pRoot8 = TreeNode(10)
treeNode1 = TreeNode(5)
treeNode2 = TreeNode(12)
treeNode3 = TreeNode(4)
treeNode4 = TreeNode(7)
treeNode5 = TreeNode(3)
treeNode6 = TreeNode(10)

# pRoot8.left = treeNode1
# pRoot8.right = treeNode2
# treeNode1.left = treeNode3
# treeNode1.right = treeNode4
s = Solution()
print s.FindPath(pRoot8, 10)
