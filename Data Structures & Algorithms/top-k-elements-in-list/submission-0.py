class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numMap = {} # value -> frequency
        res = []

        for i in range(len(nums)):
            if nums[i] in numMap:
                numMap[nums[i]] += 1
            else:
                numMap[nums[i]] = 1

        for _ in range(k):
            if len(res) == k: break
            maxKey = max(numMap, key=numMap.get)
            res.append(maxKey)
            numMap[maxKey] = -1
        
        return res