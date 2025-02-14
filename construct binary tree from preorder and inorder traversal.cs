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
    public TreeNode BuildTree(int[] preorder, int[] inorder) 
    {
        Dictionary<int, int> inOrderNodeIndexMap = new Dictionary<int, int>();

        for(int i = 0; i<inorder.Length; i++)
        {
            inOrderNodeIndexMap.Add(inorder[i], i);
        }

        int[] currentNodeIndex = {0};
        int[] bounds = {0,inorder.Length-1};

        TreeNode root = buildSubTrees(preorder, inorder, inOrderNodeIndexMap, bounds, currentNodeIndex);

        return root;
    }





    public TreeNode buildSubTrees(int[] preorder, int[] inorder, Dictionary<int, int> indexes, int[] bounds, int[] currentNodeIndex) 
    {
        if(currentNodeIndex[0] > inorder.Length -1)
        {
            return null;
        }
        
        int inOrderNodeIndex = indexes[preorder[currentNodeIndex[0]]];
        
        if(inOrderNodeIndex < bounds[0] || inOrderNodeIndex > bounds[1]){
            return null;
        }
        
        TreeNode root = new TreeNode(preorder[currentNodeIndex[0]]);

        currentNodeIndex[0] = currentNodeIndex[0] + 1;

        int[] leftBounds = {bounds[0],inOrderNodeIndex};
        int[] rightBounds = {inOrderNodeIndex,bounds[1]};

        root.left = buildSubTrees(preorder, inorder, indexes, leftBounds, currentNodeIndex);
        root.right = buildSubTrees(preorder, inorder, indexes, rightBounds, currentNodeIndex);

        return root;

    }


    
















}
