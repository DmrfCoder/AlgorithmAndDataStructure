# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

import copy
class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        # write code here
        size=0

        head1copy=copy.copy(pHead1)
        head2copy=copy.copy(pHead2)


        while head1copy is not None and head2copy is not None:
            head1copy=head1copy.next
            head2copy=head2copy.next

        flag=-1
        while head1copy is not None:
            head1copy = head1copy.next
            flag=1
            size+=1

        while head2copy is not None:
            head2copy = head2copy.next
            flag=2
            size+=1


        if flag==2:
            for i in range(size):
                pHead2=pHead2.next
        else:
            for i in range(size):
                pHead1=pHead1.next

        while pHead1 is not None:
            if pHead1.val==pHead2.val:
                return pHead1
            else:
                pHead1=pHead1.next
                pHead2=pHead2.next
        return None





s = Solution()
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)
node6 = ListNode(6)

node1.next = node2
node2.next = node3
node3.next = node4

node5.next = node6
node6.next = node3

node = s.FindFirstCommonNode(node1, node5)
a = 0
