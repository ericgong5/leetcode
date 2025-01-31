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
    public List<Integer> rightSideView(TreeNode root) {
        List<Integer> answer = new ArrayList<>();
        if(root == null ){
            return answer;
        }
        

        List<TreeNode> levels = new ArrayList<TreeNode>();
        levels.add(root);

        while(!levels.isEmpty()){
            answer.add(levels.get(levels.size()-1).val);
            List<TreeNode> temp = new ArrayList<TreeNode>();
            for (TreeNode node : levels){
                if(node.left != null){
                    temp.add(node.left);
                }
                if(node.right != null){
                    temp.add(node.right);
                }
            }
            levels = temp;
        }
        return answer;
    }

}
