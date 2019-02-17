# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        # write code here
        arrList = []
        while (listNode != None):
            arrList.insert(0, listNode.val)
            listNode = listNode.next
        return arrList


solution = Solution()
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node1.next = node2
node2.next = node3
node3.next = node4

print solution.printListFromTailToHead(node1)
