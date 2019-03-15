# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def EntryNodeOfLoop(self, pHead):
        # write code here
        p1 = pHead
        p2 = pHead
        index = 0
        while p1 != p2 or index == 0:
            if p1 == None or p2 == None:
                return None

            index += 1
            p1 = p1.next
            if p1 == None:
                return None
            if p2.next == None:
                return None
            p2 = p2.next.next

        p2 = pHead

        while p1 != p2:
            p1 = p1.next
            p2 = p2.next

        return p1


pHead = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)
node6 = ListNode(6)

pHead.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = pHead
node6.next = node4

s = Solution()
circleNode = s.EntryNodeOfLoop(pHead)
a = 0
