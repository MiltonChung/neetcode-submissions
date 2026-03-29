class Solution:
    def threeSum(self, nums: List[int]) -> List[int]:
        res = set()
        diffMap = {} # index -> remainder

        nums.sort()
        for i in range(len(nums)):
            diffMap[i] = 0 - nums[i]

        for key in diffMap:
            L = 0
            R = len(nums) - 1
            while L < R:
                if L == key:
                    L += 1
                    continue
                if R == key:
                    R -= 1
                    continue
                
                current_sum = nums[L] + nums[R]
                if current_sum == diffMap[key]:
                    res.add(tuple(sorted((nums[L], nums[key], nums[R]))))
                    L += 1
                    R -= 1
                elif current_sum < diffMap[key]:
                    L += 1
                else:
                    R -= 1

        return [list(t) for t in res]