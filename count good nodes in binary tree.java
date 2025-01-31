/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

class Solution {
    public int goodNodes(TreeNode root) {
        if(root == null){
            return 0;
        }

        return dfs(root, root.val);


        
    }

    public int dfs(TreeNode root, int maxNumber){
        if(root == null){
            return 0;
        }
        if(root.val < maxNumber){
            return dfs(root.left,maxNumber) + dfs(root.right,maxNumber);
        }else{
            return 1 + dfs(root.left,root.val) + dfs(root.right,root.val);
        }
    }
}
