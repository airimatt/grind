/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
#include <vector>

class Solution {
public:
    vector<int> inorderTraversal(TreeNode* root) {

        vector<int> values;
        
        recursiveInOrder(root, values);
        
        return values;
        
    }

private:
    void recursiveInOrder(TreeNode *curr, vector<int> &values) {
        
        if (curr == nullptr) {
            return;
        } 
        
        recursiveInOrder(curr->left, values);
        values.push_back(curr->val);
        recursiveInOrder(curr->right, values);
        
        return;
    }
};