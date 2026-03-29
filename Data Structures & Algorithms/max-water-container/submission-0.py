class Solution:
    def maxArea(self, heights: List[int]) -> int:
        L, R = 0, len(heights) - 1
        maxWater = 0

        while L < R:
            area = min(heights[L], heights[R]) * (R - L)
            maxWater = max(maxWater, area)
            
            if heights[L] > heights[R]:
                R -= 1
            else:
                L += 1
        
        return maxWater