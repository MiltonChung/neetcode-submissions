class Solution:
    def trap(self, height: List[int]) -> int:
        maxArea = 0

        L, R = 0, len(height) - 1
        while L + 1 < len(height) and height[L] <= height[L + 1]:
            L += 1
        while R - 1 > 0 and height[R - 1] >= height[R]:
            R -= 1
        
        newHeights = height[L:R + 1]

        L = 0
        for R in range(1, len(newHeights)):
            if newHeights[L] <= newHeights[R]:
                area = (R - L - 1) * min(newHeights[L], newHeights[R])
                L += 1
                while L != R:
                    area -= newHeights[L]
                    L += 1
                maxArea += area
        
        L = len(newHeights) - 1
        for R in range(len(newHeights) - 2, -1, -1):
            if newHeights[L] < newHeights[R]:
                area = (L - R - 1) * min(newHeights[L], newHeights[R])
                L -= 1
                while L != R:
                    area -= newHeights[L]
                    L -= 1
                maxArea += area
        
        return maxArea
