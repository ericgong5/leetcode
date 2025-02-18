public class Solution {
    public int MinEatingSpeed(int[] piles, int h) {
        
        int leftBound = 1;
        int rightBound = piles.Max();
        int minResult = rightBound;
        

        while(leftBound <= rightBound)
        {
            int middle = (rightBound + leftBound)/2;

            long time = 0;

            foreach(int pile in piles)
            {
                time += (int)Math.Ceiling((double)pile/middle);
            }
            if(time <= h)
            {
                minResult = middle;
                rightBound = middle - 1;
            }
            else
            {
                leftBound = middle + 1;
            }
        }
        return minResult;
    }

}
