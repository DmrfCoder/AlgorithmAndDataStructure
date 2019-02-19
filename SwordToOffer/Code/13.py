# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        if head == None or k <= 0:
            return None
        node = head
        node2 = head
        while node.next != None:
            if k == 1:
                node2 = node2.next
            else:
                k -= 1
            node = node.next

        if k != 1:
            return None

        return node2


solution = Solution()
head = ListNode(1)
node1 = ListNode(2)
node2 = ListNode(3)
node3 = ListNode(4)
node4 = ListNode(5)

head.next = node1
node1.next = node2
node2.next = node3
# node3.next = node4

print solution.FindKthToTail(head, 20)
