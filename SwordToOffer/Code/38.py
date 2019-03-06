# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def TreeDepth(self, pRoot):
        # write code here
        if pRoot is None:
            return 0
        return max(1 + self.TreeDepth(pRoot.left), 1 + self.TreeDepth(pRoot.right))


#迭代版本
'''
class Solution {
public:
    int TreeDepth(TreeNode* pRoot) {
        if (!pRoot) return 0;
        queue<TreeNode*> que;
        que.push(pRoot);int depth=0;
        while (!que.empty()) {
            int size=que.size();
            depth++;
            for (int i=0;i<size;i++) {      //一次处理一层的数据
                TreeNode *node=que.front();
                que.pop();
                if (node->left) que.push(node->left);
                if (node->right) que.push(node->right);
            }
        }
        return depth;
    }
};


'''
