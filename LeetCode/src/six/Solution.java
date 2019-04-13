package six;

import java.util.ArrayList;
import java.util.Stack;

/**
 * @author dmrfcoder
 * @date 2019/4/10
 */


class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;

    TreeNode(int x) {
        val = x;
    }
}

public class Solution {
    public ArrayList<Integer> postorderTraversal(TreeNode root) {
        Stack<TreeNode> treeNodeStack = new Stack<>();
        ArrayList<Integer> arrayList = new ArrayList<>();
        if (root == null) {
            return arrayList;
        }

        TreeNode preNode = null;
        TreeNode curNode = null;

        treeNodeStack.push(root);

        while (!treeNodeStack.isEmpty()) {
            if (curNode == null) {
                curNode = treeNodeStack.peek();

            }

            if (curNode.left == null && curNode.right == null) {
                preNode = curNode;
                arrayList.add(curNode.val);
                treeNodeStack.pop();
                curNode = null;
            } else if ((preNode == curNode.left && curNode.left != null) || (preNode == curNode.right && curNode.right != null)) {
                preNode = curNode;
                arrayList.add(curNode.val);
                treeNodeStack.pop();
                curNode = null;
            } else {
                if (curNode.right != null) {
                    treeNodeStack.push(curNode.right);
                }

                if (curNode.left != null) {
                    treeNodeStack.push(curNode.left);
                }
                curNode = curNode.left;
            }


        }
        return arrayList;
    }

    public static void main(String args[]) {
        TreeNode root = new TreeNode(1);
        TreeNode node2 = new TreeNode(2);
        TreeNode node3 = new TreeNode(3);
        TreeNode node4 = new TreeNode(4);
        TreeNode node5 = new TreeNode(5);
        TreeNode node6 = new TreeNode(6);
        TreeNode node7 = new TreeNode(7);

        root.left = node2;
//        root.right = node3;
//        node2.left = node4;
//        node2.right = node5;
//        node3.left = node6;
//        node3.right = node7;

        Solution solution = new Solution();
        ArrayList<Integer> arrayList = solution.postorderTraversal(root);
        System.out.println(arrayList.toArray().toString());

    }
}