class Solution {
    public List<List<Integer>> levelOrder(TreeNode root) {
        List<List<Integer>> answer = new ArrayList<>();
        if(root == null ){
            return answer;
        }
        
        List<TreeNode> levels = new ArrayList<TreeNode>();
        levels.add(root);
        while(!levels.isEmpty()){
            List<TreeNode> temp = new ArrayList<TreeNode>();
            List<Integer> integers = new ArrayList<Integer>();
            for (TreeNode node : levels){
                integers.add(node.val);
                if(node.left != null){
                    temp.add(node.left);
                }
                if(node.right != null){
                    temp.add(node.right);
                }
            }
            answer.add(integers);
            levels = temp;
        }
        return answer;
        
    }
}
