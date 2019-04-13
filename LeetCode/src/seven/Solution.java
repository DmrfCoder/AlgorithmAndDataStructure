package seven;

/**
 * @author dmrfcoder
 * @date 2019-04-13
 */

import java.util.ArrayList;
import java.util.Stack;

/**
 * Definition for binary tree
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
    public ArrayList<Integer> preorderTraversal(TreeNode root) {
        Stack<TreeNode> stack = new Stack<>();
        ArrayList<Integer> arrayList = new ArrayList<>();
        if (root == null) {
            return arrayList;
        }


        TreeNode curNode = root;
        arrayList.add(root.val);
        stack.push(root);

        while (!stack.empty()) {
            if (curNode == null) {
                curNode = stack.pop();
                if (curNode.right != null) {
                    arrayList.add(curNode.right.val);
                    stack.push(curNode.right);
                    curNode = curNode.right;
                } else {
                    curNode = null;
                }
                continue;
            } else if (curNode.left != null) {
                arrayList.add(curNode.left.val);
                stack.push(curNode.left);


            }
            curNode = curNode.left;
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
        ArrayList<Integer> arrayList = solution.preorderTraversal(root);
        System.out.println(arrayList.toArray().toString());

    }
}