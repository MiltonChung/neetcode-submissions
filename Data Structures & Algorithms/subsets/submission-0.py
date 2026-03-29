class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res, curSet = [], []
        
        def dfs(i, nums, res, curSet):
            if i >= len(nums):
                res.append(curSet.copy())
                return
            
            curSet.append(nums[i])
            dfs(i + 1, nums, res, curSet)
            curSet.pop()
            dfs(i + 1, nums, res, curSet)

        dfs(0, nums, res, curSet)
        return res