class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmapCount = {}
        res = []

        for n in nums:
            if n not in hashmapCount:
                hashmapCount[n] = 0
            hashmapCount[n] += 1
        
        sortedCount = []
        for key, v in hashmapCount.items():
            sortedCount.append((v, key))
        sortedCount.sort(key=lambda v: v[0], reverse=True)

        for i in range(k):
            res.append(sortedCount[i][1])
        
        return res