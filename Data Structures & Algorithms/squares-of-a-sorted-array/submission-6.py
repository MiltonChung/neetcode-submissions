class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        L, R, res = 0, len(nums) - 1, []

        while L <= R:
            if abs(nums[L]) > abs(nums[R]):
                res.append(nums[L] * nums[L])
                L += 1
            else:
                res.append(nums[R] * nums[R])
                R -= 1
        
        res.reverse()
        return res
            