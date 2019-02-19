# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


import copy


class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        # write code here

        if pHead1 != None and pHead2 != None:
            if pHead1.val <= pHead2.val:
                newHead = pHead1
                pHead1 = pHead1.next
            else:
                newHead = pHead2
                pHead2 = pHead2.next
        elif pHead1!=None:
            return pHead1
        else:
            return pHead2


        curHead = newHead

        while pHead1 != None and pHead2 != None:
            if pHead1.val <= pHead2.val:
                curHead.next = pHead1

                pHead1 = pHead1.next
            else:
                curHead.next = pHead2
                pHead2 = pHead2.next

            curHead = curHead.next

        if pHead1 != None:
            curHead.next = pHead1
        if pHead2 != None:
            curHead.next = pHead2

        return newHead


solution = Solution()
head = ListNode(1)
node1 = ListNode(3)
node2 = ListNode(5)
node3 = ListNode(7)
node4 = ListNode(9)

head.next = node1
node1.next = node2
node2.next = node3
node3.next = node4

headb = ListNode(2)
node1b = ListNode(4)
node2b = ListNode(6)
node3b = ListNode(8)
node4b = ListNode(10)

headb.next = node1b
node1b.next = node2b
node2b.next = node3b
node3b.next = node4b

newHead = solution.Merge(head, headb)
a = 0
