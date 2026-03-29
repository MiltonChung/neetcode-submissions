class Solution:
    def findMin(self, nums: List[int]) -> int:
        L, R = 0, len(nums) - 1

        while L < R:
            M = (R + L) // 2
            if M == L or M == R: break
            if nums[L] < nums[M] and nums[M] < nums[R]:
                return nums[L]
            if nums[L] < nums[M]:
                L = M
            else:
                R = M
                
        return min(nums[L], nums[R])