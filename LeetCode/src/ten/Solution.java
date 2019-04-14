package ten;


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

    public boolean hasCycle(ListNode head) {

        if (head == null) {
            return false;
        }
        ListNode fast, slow;
        fast = slow = head;

        while (fast.next != null && fast.next.next != null) {
            fast = fast.next.next;
            slow = slow.next;
            if (fast == slow) {
                return true;
            }
        }
        return false;


    }
}
