# -*- coding:utf-8 -*-
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None


class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        # write code here
        currentNode = pHead
        if pHead is None:
            return None

        while currentNode is not None:
            node = RandomListNode(currentNode.label)
            node.next = currentNode.next
            currentNode.next = node
            currentNode = currentNode.next.next

        currentNode = pHead
        while currentNode is not None:
            node = currentNode.next
            if currentNode.random is not None:
                node.random = currentNode.random.next
            currentNode = node.next

        currentNode = pHead
        cloneP = pHead.next

        while currentNode.next is not None:
            temp = currentNode.next
            currentNode.next = temp.next
            currentNode = temp
        return cloneP


head = RandomListNode(1)
node2 = RandomListNode(2)
node3 = RandomListNode(3)
node4 = RandomListNode(4)
node5 = RandomListNode(5)
nodex = RandomListNode('#')

head.next = node2
head.random = node3

node2.next = node3
node2.random = node5

node3.next = node4
node3.random = nodex

node4.next = node5
node4.random = node2

node5.random = nodex

s = Solution()
h = s.Clone(head)
a = 0
