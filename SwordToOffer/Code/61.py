# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplication(self, pHead):
        # write code here

        if pHead is None:
            return pHead

        p1 = pHead
        if p1 is None:
            return pHead

        p2 = pHead.next
        if p2 is None:
            return pHead

        newHead = ListNode(0)
        newHead.next = pHead

        preP = newHead
        curP = newHead.next

        while curP is not None:
            if curP.next is not None and curP.next.val == curP.val:
                while curP.next is not None and curP.val == curP.next.val:
                    curP = curP.next

                preP.next = curP.next
                curP = curP.next

            else:
                preP = curP
                curP = curP.next

        return newHead.next


s = Solution()
pHead = ListNode(1)
node2 = ListNode(1)
node3 = ListNode(1)
node4 = ListNode(1)
node5 = ListNode(1)
node6 = ListNode(1)
node7 = ListNode(1)

pHead.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = node7

newHead = s.deleteDuplication(pHead)
a = 0
