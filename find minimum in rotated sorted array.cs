public class Solution {
    public int FindMin(int[] nums) {
        int leftBound = 0;
        int rightBound = nums.Length - 1;

        while(rightBound - leftBound > 1)
        {
            int middle = (rightBound + leftBound)/2;
            if(nums[middle] >= nums[leftBound])
            {
                leftBound = middle;
            }
            else
            {
                rightBound = middle;
            }
        }

        if(nums[rightBound] < nums[leftBound])
        {
            return nums[rightBound];
        }
        else
        {
            return nums[0];
        }

    }

}
