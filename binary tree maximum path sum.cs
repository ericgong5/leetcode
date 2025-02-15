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
    public int MaxPathSum(TreeNode root) 
    {
        if(root == null)
        {
            return 0;
        }
        int[] maxPathSum = {root.val};

        getPathSumAndMax(root, maxPathSum);

        return  maxPathSum[0];

    }


    public int getPathSumAndMax(TreeNode root, int[] maxPathSum)
    {
        if (root == null)
        {
            return 0;
        }

        int leftChildPathVal =  getPathSumAndMax(root.left, maxPathSum);
        int rightChildPathVal =  getPathSumAndMax(root.right, maxPathSum);

        if(leftChildPathVal < 0)
        {
            leftChildPathVal = 0;
        }

        if(rightChildPathVal < 0)
        {
            rightChildPathVal = 0;
        }

        int currentPathSum = leftChildPathVal + rightChildPathVal + root.val;

        maxPathSum[0] = Math.Max(currentPathSum, maxPathSum[0]);
 


        return Math.Max(leftChildPathVal, rightChildPathVal) + root.val;


    }
}
