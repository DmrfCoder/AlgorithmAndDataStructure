# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回镜像树的根节点
    def Mirror(self, root):
        # write code here
        if root == None:
            return None
        if root.left == None or root.right == None:
            return self.change(root)

        if root.left.left is None and root.left.right is None and root.right.left is None and root.right.right is None:
            return self.change(root)
        else:
            mirrorRoot = TreeNode(root.val)
            mirrorRoot.left = self.Mirror(root.right)
            mirrorRoot.right = self.Mirror(root.left)
            return mirrorRoot

    def Mirror2(self, root):
        # write code here
        if not root:
            return root
        node = root.left
        root.left = root.right
        root.right = node
        self.Mirror2(root.left)
        self.Mirror2(root.right)
        return root


    def Mirror3(self,root):
        if root:  # 如果存在根节点
            root.left, root.right = root.right, root.left  # 根节点左右交换，俩变量交换也可以这样写
            self.Mirror(root.left)  # 递归调用左节点
            self.Mirror(root.right)  # 递归调用右节点
            return root  # 返回节点
        else:
            return  # else无节点时直接return

    def change(self, Node):
        newNode = TreeNode(Node.val)
        newNode.left = Node.right
        newNode.right = Node.left
        return newNode


def FirstBrowse(pRoot):
    result = []
    if pRoot == None:
        return result
    else:
        result.append(pRoot.val)
        result = result + FirstBrowse(pRoot.left)
        result = result + FirstBrowse(pRoot.right)
    return result


pRoot8 = TreeNode(8)
treeNode6 = TreeNode(6)
treeNode10 = TreeNode(10)
treeNode5 = TreeNode(5)
treeNode7 = TreeNode(7)
treeNode9 = TreeNode(9)
treeNode11 = TreeNode(11)

pRoot8.left = treeNode6
pRoot8.right = treeNode10
treeNode6.left = treeNode5
treeNode6.right = treeNode7
treeNode10.left = treeNode9
treeNode10.right = treeNode11
s = Solution()
t = s.Mirror(pRoot8)
t2 = s.Mirror2(pRoot8)
t3 = s.Mirror2(pRoot8)
print FirstBrowse(pRoot8)
print FirstBrowse(t)
print FirstBrowse(t2)
print FirstBrowse(t3)
