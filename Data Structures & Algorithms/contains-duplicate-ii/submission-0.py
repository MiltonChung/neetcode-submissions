class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        res = False
        dups = {}

        for i in range(len(nums)):
            if nums[i] in dups:
                indexOfPrevDup = dups[nums[i]]
                if abs(i - indexOfPrevDup) <= k:
                    return True
            dups[nums[i]] = i
        
        return res