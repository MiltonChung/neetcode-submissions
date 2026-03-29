class Solution:
    def trap(self, height: List[int]) -> int:
        maxL, maxR = 0, 0
        L, R = 0, len(height) - 1
        res = 0

        while L < R:
            if height[L] < height[R]:
                maxL = max(maxL, height[L])
                res = res + (maxL - height[L])
                L += 1
            else:
                maxR = max(maxR, height[R])
                res = res + (maxR - height[R])
                R -= 1

        return res