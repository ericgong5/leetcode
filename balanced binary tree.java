class Solution {
    public boolean isBalanced(TreeNode root) {
        boolean[] balanced = {true};

        dfs(root,balanced);

        return balanced[0];

        
    }

    public int dfs(TreeNode root, boolean[] balanced ){
        if(root == null){
            return 0;
        }

        int leftHeight = dfs(root.left,balanced);
        int rightHeight = dfs(root.right,balanced);

        if(Math.abs(leftHeight-rightHeight) > 1){
            balanced[0] = false;
        }

        return 1 + Math.max(leftHeight, rightHeight);


    }
}
