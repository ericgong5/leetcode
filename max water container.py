class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1
        biggestContainerSize = 0 

        while left < right:
            tallestEdge = min(heights[left], heights[right])
            biggestContainerSize = max(biggestContainerSize, (right-left)*tallestEdge)
            if heights[left] > heights[right]:
                right -= 1
            else:
                left += 1

        return biggestContainerSize
