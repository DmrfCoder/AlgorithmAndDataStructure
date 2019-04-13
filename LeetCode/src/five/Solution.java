package five;

/**
 * @author dmrfcoder
 * @date 2019/4/10
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
    public ListNode insertionSortList(ListNode head) {
        if (head == null || head.next == null) {
            return head;
        }

        ListNode tempHead = new ListNode(0);
        tempHead.next = head;


        ListNode curNode = head;
        ListNode indexNode;

        while (curNode != null) {

            indexNode = curNode.next;
            while (indexNode != null && indexNode.val >= curNode.val) {
                indexNode = indexNode.next;
                curNode = curNode.next;
            }

            if (indexNode == null) {
                return tempHead.next;
            }

            ListNode copyOfTempHead = tempHead;
            ListNode copyOfHead = tempHead.next;

            while (copyOfHead.val < indexNode.val) {
                copyOfTempHead = copyOfTempHead.next;
                copyOfHead = copyOfHead.next;
            }
            copyOfTempHead.next = indexNode;
            curNode.next = indexNode.next;
            indexNode.next = copyOfHead;


        }

        return tempHead.next;
    }

    public static void main(String[] args) {
        ListNode head = new ListNode(3);
        ListNode node2 = new ListNode(2);
        ListNode node1 = new ListNode(1);
        head.next = node2;
        node2.next = node1;

        Solution solution = new Solution();
        solution.insertionSortList(head);
    }
}
