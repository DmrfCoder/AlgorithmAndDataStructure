package thirteen;

/**
 * @author dmrfcoder
 * @date 2019-04-19
 */

/**
 * Definition for singly-linked list with a random pointer.
 */
class RandomListNode {
    int label;
    RandomListNode next, random;

    RandomListNode(int x) {
        this.label = x;
    }
};

public class Solution {
    public RandomListNode copyRandomList(RandomListNode head) {

        if (head == null) {
            return null;
        }
        RandomListNode curNode = head;
        RandomListNode curNodeNext;
        while (curNode != null) {
            RandomListNode copyOfCurNode = new RandomListNode(curNode.label);
            curNodeNext = curNode.next;
            curNode.next = copyOfCurNode;
            copyOfCurNode.next = curNodeNext;
            curNode = curNode.next.next;
        }

        curNode = head;

        while (curNode != null) {
            curNode.next.random = curNode.random;
            curNode = curNode.next.next;
        }

        RandomListNode copyListHead = head.next;
        RandomListNode curNewNode = head.next;
        RandomListNode tempNode;

        curNode = head;

        while (curNode != null) {
            tempNode = curNewNode.next;
            curNode.next = tempNode;
            if (tempNode != null) {
                curNewNode.next = tempNode.next;
            } else {
                curNewNode.next = null;
            }

            curNode = tempNode;
            if (curNode!=null){
                curNewNode = curNode.next;
            }


        }

        return copyListHead;
    }

    public static void main(String[] args) {
        RandomListNode head = new RandomListNode(-1);
        RandomListNode node2 = new RandomListNode(1);
        RandomListNode node3 = new RandomListNode(3);
        RandomListNode node4 = new RandomListNode(4);
        RandomListNode node5 = new RandomListNode(5);
        head.next = node2;
        //node2.next = node3;
//        node3.next = node4;
//        node4.next = node5;
//
//        head.random = node5;
//        node2.random = head;
//        node3.random = null;
//        node4.random = node3;
//        node5.random = node2;

        Solution s = new Solution();
        RandomListNode randomListNode = s.copyRandomList(head);

        int a = 0;
    }
}
