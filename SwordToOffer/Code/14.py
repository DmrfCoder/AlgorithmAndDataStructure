# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        if pHead == None:
            return None

        newHead=ListNode(pHead.val)
        newHead.next=None

        pHead=pHead.next

        while pHead!=None:
            cHead=ListNode(pHead.val)
            cHead.next=newHead
            newHead=cHead

            pHead=pHead.next

        return newHead


head = ListNode(1)
node1 = ListNode(2)
node2 = ListNode(3)
node3 = ListNode(4)
node4 = ListNode(5)

head.next = node1
node1.next = node2
node2.next = node3
node3.next = node4
solution = Solution()
newHead=solution.ReverseList(head)
a=1
