/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     public int val;
 *     public TreeNode left;
 *     public TreeNode right;
 *     public TreeNode(int val=0, TreeNode left=null, TreeNode right=null) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

public class Solution {
    public bool IsValidBST(TreeNode root) {
        return bst(root, -1001, 1001);
        
        
    }

    public bool bst(TreeNode root,  int minValue, int maxValue) {
        if(root == null)
        {
            return true;
        }

        if(root.val <= minValue  || root.val >= maxValue)
        {
            return false;

        }

        return bst(root.left, minValue, root.val) && bst(root.right, root.val, maxValue);
        
        
    }
}
