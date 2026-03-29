class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dupsPosition = {}

        for i in range(len(nums)):
            if nums[i] in dupsPosition:
                indexOfPrevDup = dupsPosition[nums[i]]
                if abs(i - indexOfPrevDup) <= k:
                    return True
            dupsPosition[nums[i]] = i
        
        return False