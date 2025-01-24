class Solution {
    public int diameterOfBinaryTree(TreeNode root) {
        if(root == null){
            return 0;
        }
        int[] maxDiameter =  {0};

        getHeightAndDiameter(root, maxDiameter);

        return  maxDiameter[0];
        
    }

    public int getHeightAndDiameter(TreeNode root, int[] maxDiameter){
        if (root == null){
            return 0;
        }

        int leftChild =  getHeightAndDiameter(root.left, maxDiameter);
        int rightChild =  getHeightAndDiameter(root.right, maxDiameter);

        int diameter = leftChild + rightChild;

        maxDiameter[0] = Math.max(diameter, maxDiameter[0]);
 


        return 1  +  Math.max(leftChild, rightChild);
    }
}
