class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        bestProfit = 0
        curMin = 101
        curMax = 0
        
        for i in range(len(prices)):
            if prices[i] < curMin:
                curMin = prices[i]
                curMax = prices[i]
            elif prices[i] > curMax:
                curMax = prices[i]
                if prices[i] - curMin > bestProfit:
                    bestProfit = prices[i] - curMin

        return bestProfit
