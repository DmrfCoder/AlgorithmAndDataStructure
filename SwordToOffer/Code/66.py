# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def Serialize(self, root):
        # write code here
        if root is None:
            s = 'n'
            return s

        a = []
        a.append(root)

        s = ''
        while len(a) != 0:
            curNode = a[0]
            del a[0]
            if curNode.val != 'n':
                s = s + '/' + str(curNode.val)
                if curNode.left is not None:
                    a.append(curNode.left)
                else:
                    a.append(TreeNode('n'))
                if curNode.right is not None:
                    a.append(curNode.right)
                else:
                    a.append(TreeNode('n'))
            else:
                s = s + '/n'
        return s

    def Deserialize(self, s):
        # write code here
        if s == 'n':
            return None
        array = s.split('/')
        del array[0]

        root = TreeNode(int(array[0]))
        del array[0]
        p = root
        b = [p]
        while len(array) != 0 and len(b) != 0:
            innerP = b[0]
            del b[0]
            temp1 = array[0]
            del array[0]
            if temp1 == 'n':
                innerP.left = None
            else:
                leftn=int(temp1)
                innerP.left = TreeNode(leftn)
                b.append(innerP.left)

            temp2 = array[0]
            del array[0]
            if temp2 == 'n':
                innerP.right = None
            else:
                rightn=int(temp2)
                innerP.right = TreeNode(rightn)
                b.append(innerP.right)

        return root


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

str = s.Serialize(pRoot)
print str
root=s.Deserialize(str)
a=0