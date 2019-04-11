package one;

import java.util.LinkedList;
import java.util.Queue;

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
    public int run(TreeNode root) {
        if (root == null) {
            return 0;
        }

        Queue<TreeNode> treeNodeQueue = new LinkedList<TreeNode>();
        treeNodeQueue.offer(root);
        treeNodeQueue.offer(null);


        int minDepth = 1;

        while (!treeNodeQueue.isEmpty()) {
            TreeNode curNode = treeNodeQueue.poll();
            if (curNode == null) {

                if (treeNodeQueue.isEmpty()) {
                    return minDepth;
                } else {
                    minDepth += 1;
                    treeNodeQueue.offer(null);
                }
            } else {
                if (curNode.left == null && curNode.right == null) {
                    return minDepth;
                }
                if (curNode.left != null) {
                    treeNodeQueue.offer(curNode.left);
                }
                if (curNode.right != null) {
                    treeNodeQueue.offer(curNode.right);
                }
            }


        }
        return minDepth;
    }




    public static void main(String[] args) {
        Solution solution = new Solution();
        TreeNode root = new TreeNode(1);
        TreeNode node2 = new TreeNode(2);
        TreeNode node3 = new TreeNode(2);
        TreeNode node4 = new TreeNode(2);
        TreeNode node5 = new TreeNode(2);
        root.left = node2;
        root.right = node3;
        node2.left = node4;
        node2.right = node5;

        System.out.println(solution.run(root));

    }
}