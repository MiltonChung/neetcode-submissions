class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqArr = [[] for _ in range(len(nums) + 1)]
        numMap = {} # value -> frequency
        res = []

        for i in range(len(nums)):
            if nums[i] in numMap:
                numMap[nums[i]] += 1
            else:
                numMap[nums[i]] = 1
        
        for n in numMap:
            freqArr[numMap[n]].append(n)

        for i in range(len(nums), -1, -1):
            for n in freqArr[i]:
                res.append(n)
                if len(res) == k: return res            
        