package four;

/**
 * @author dmrfcoder
 * @date 2019/4/10
 */

/**
 * Definition for singly-linked list.
 */

class ListNode {
    int val;
    ListNode next;

    ListNode(int x) {
        val = x;
        next = null;
    }
}

public class Solution {
    public ListNode sortList(ListNode head) {
        if (head == null || head.next == null) {
            return head;
        }
        ListNode startNode, endNode;
        startNode = head;
        endNode = head.next;

        while (startNode != null && endNode != null && endNode.next != null) {
            startNode = startNode.next;
            endNode = endNode.next.next;
        }


        ListNode right = sortList(startNode.next);
        startNode.next = null;
        ListNode left = sortList(head);


        return mergeList(left, right);
    }

    private ListNode mergeList(ListNode left, ListNode right) {
        ListNode tempListNode = new ListNode(0);
        ListNode p = tempListNode;

        while (left != null && right != null) {
            if (left.val < right.val) {
                p.next = left;
                p = p.next;
                left = left.next;
            } else {
                p.next = right;
                p = p.next;
                right = right.next;
            }
        }
        if (left != null) {
            p.next = left;
        }
        if (right != null) {
            p.next = right;
        }


        return tempListNode.next;
    }

    public static void main(String[] args) {
        ListNode head = new ListNode(1);
        ListNode node2 = new ListNode(2);
        ListNode node3 = new ListNode(3);
        ListNode node4 = new ListNode(4);
        ListNode node5 = new ListNode(5);
        ListNode node6 = new ListNode(6);
        ListNode node7 = new ListNode(7);

        head.next = node7;
        node7.next = node3;
        node3.next = node2;
        node2.next = node4;
        node4.next = node5;

        Solution solution = new Solution();
        head = solution.sortList(head);
        int a = 0;
    }
}
