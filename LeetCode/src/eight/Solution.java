package eight;

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
    public void reorderList(ListNode head) {
        if (head != null && head.next != null) {
            ListNode fast, slow;
            fast = slow = head;
            //快慢指针找出链表的中间节点
            while (fast.next != null && fast.next.next != null) {
                fast = fast.next.next;
                slow = slow.next;
            }

            //拆分链表
            ListNode preNode = slow.next;
            slow.next = null;
            ListNode afterNode = preNode.next;
            preNode.next=null;
            //翻转后一半链表
            while (afterNode != null) {
                ListNode tempNode = afterNode.next;
                afterNode.next = preNode;
                preNode = afterNode;
                afterNode = tempNode;
            }

            //合并链表
            while (preNode != null && head != null) {
                ListNode tempNode1 = head.next;
                ListNode tempNode2 = preNode.next;
                head.next = preNode;
                preNode.next = tempNode1;
                preNode = tempNode2;
                head = tempNode1;

            }


        }

    }


    public static void main(String[] args) {
        ListNode head = new ListNode(1);
        ListNode node2 = new ListNode(2);
        ListNode node3 = new ListNode(3);
        ListNode node4 = new ListNode(4);
        ListNode node5 = new ListNode(5);

        head.next = node2;
        node2.next = node3;
        node3.next = node4;
        node4.next = node5;
        Solution solution = new Solution();
        solution.reorderList(head);
    }
}