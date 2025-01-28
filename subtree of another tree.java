class Solution {  
    public boolean isSubtree(TreeNode root, TreeNode subRoot) {
        if(subRoot == null ){
            return true;
        }
        if(root == null){
            return false;
        }

        
        if(isSameTree(root,subRoot)){
            return true;
            
        }

        return isSubtree(root.left,subRoot) || isSubtree(root.right,subRoot);
    }


    public boolean isSameTree(TreeNode p, TreeNode q) {
        if(p == null && q == null){
            return true;
        }

        if (p != null && q != null && p.val == q.val) {
                return isSameTree(p.left, q.left) && 
                    isSameTree(p.right, q.right);
            }
        return false;
    }
}
