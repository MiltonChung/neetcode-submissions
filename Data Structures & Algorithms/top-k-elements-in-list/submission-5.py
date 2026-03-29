class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmapCount = {}
        freqArr = [[] for _ in range(len(nums) + 1)]
        res = []

        for n in nums:
            if n not in hashmapCount:
                hashmapCount[n] = 0
            hashmapCount[n] += 1
        
        for key, c in hashmapCount.items():
            freqArr[c].append(key)
        
        for i in range(len(freqArr) - 1, 0, -1):
            for n in freqArr[i]:
                res.append(n)
                if len(res) == k:
                    return res
