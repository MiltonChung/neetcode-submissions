class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res, subsets = [], []
        nums.sort()

        def dfs(i):
            if i >= len(nums):
                res.append(subsets.copy())
                return
            
            # Choice to include current number
            subsets.append(nums[i])
            dfs(i + 1)

            # Before continuing with the choice to not include current number,
            # skip all duplicates
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1

            subsets.pop()
            dfs(i + 1)

        dfs(0)
        return res