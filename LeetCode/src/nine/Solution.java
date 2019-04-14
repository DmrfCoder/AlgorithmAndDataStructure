package nine;

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
    public ListNode detectCycle(ListNode head) {
        if (head == null) {
            return null;
        }
        ListNode fast, slow;
        fast = slow = head;
        while (fast.next != null && fast.next.next != null) {
            fast = fast.next.next;
            slow = slow.next;
            if (fast == slow) {
                break;
            }
        }

        if (fast.next == null || fast.next.next == null) {
            return null;
        }

        fast = head;
        while (fast != null && slow != null) {
            if (fast == slow) {
                return fast;
            }
            fast = fast.next;
            slow = slow.next;

        }
        return null;


    }

    public static void main(String[] args){
        ListNode head=new ListNode(1);
        ListNode node2=new ListNode(2);
        head.next=node2;
        node2.next=head;
        Solution solution=new Solution();
        ListNode res=solution.detectCycle(head);
        System.out.println(res.val);

    }
}