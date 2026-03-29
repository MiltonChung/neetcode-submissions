class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {} # {diff: index}
        res = []

        for i, n in enumerate(nums):
            if n in hashmap:
                return [hashmap[n], i]
            diff = target - n
            hashmap[diff] = i