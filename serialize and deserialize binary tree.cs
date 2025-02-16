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

public class Codec {

    // Encodes a tree to a single string.
    public string Serialize(TreeNode root) {
        if(root == null)
        {
            return "";
        }

        return bfs(root);


        
    }
    public string bfs(TreeNode root)
    {
        if(root == null)
        {
            return "n";
        }

        return root.val.ToString() + "," + bfs(root.left) + "," + bfs(root.right);
    }

    // Decodes your encoded data to tree.
    public TreeNode Deserialize(string data) {
        if(data == "")
        {
            return null;
        }
        
        int[] index  = {0};
        return deserializeBFS(data, index);
        
    }


    public TreeNode deserializeBFS(string data,int[] index)
    {
        if(index[0] >= data.Length)
        {
            return null;
        }
        if(data[index[0]] == ','){
            index[0] += 1;
        }
        
        if(data[index[0]] == 'n')
        {
            index[0] += 1;
            return null;
        }
        string nodeValue = "";
        while(index[0] < data.Length && data[index[0]] != 'n' && data[index[0]] != ',')
        {
            nodeValue = nodeValue + data[index[0]].ToString();
            index[0] += 1;
        }
        int nodeIntegerValue = Int32.Parse(nodeValue);

        TreeNode root = new TreeNode(nodeIntegerValue);
        root.left = deserializeBFS(data, index);
        root.right = deserializeBFS(data, index);

        return root;
    }

}
