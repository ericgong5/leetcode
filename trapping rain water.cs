public class Solution {
    public int Trap(int[] height) {

        int[] prefixMax = new int[height.Length];
        int[] suffixMax = new int[height.Length];

        int maxHeight = 0;
        for(int i = 0;i<height.Length; i++)
        {
            if(height[i] > maxHeight)
            {
                maxHeight = height[i];
                
            }
            prefixMax[i] = maxHeight;
        }
        maxHeight = 0;
        for(int i = height.Length-1;i>=0; i--)
        {
            if(height[i] > maxHeight)
            {
                maxHeight = height[i];
                
            }
            suffixMax[i] = maxHeight;
        }

        int totalWater = 0;

        for(int i = 0; i<height.Length; i++)
        {
            totalWater += Math.Min(prefixMax[i],suffixMax[i]) - height[i];
        }
        return totalWater;
        
    }
}
