
public class Solution {
    public int kthSmallest(TreeNode root, int k) {
        if(root == null )
        {
            return -1;
        }
        boolean[] reachedSmallestNode = {false};
        int[] kCounter = {k};

        return bst(root, kCounter, reachedSmallestNode);

        
    }

    public int bst(TreeNode root, int[] kCounter, boolean[] reachedSmallestNode) {
        if(root == null )
        {
            return 0;
        }
        
        int leftChildResult = bst(root.left, kCounter, reachedSmallestNode);
        if(!reachedSmallestNode[0] && leftChildResult == 0){
            reachedSmallestNode[0] = true;

        }
        if(kCounter[0] == 1 && reachedSmallestNode[0])
        {   
            kCounter[0] -= 1;
            return root.val;
        }

        kCounter[0] -= 1;

        

        return leftChildResult + bst(root.right, kCounter, reachedSmallestNode);
        

        
    }
}
