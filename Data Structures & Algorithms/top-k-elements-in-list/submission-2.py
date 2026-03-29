class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numMap = {} # value -> frequency
        res = []

        for i in range(len(nums)):
            if nums[i] in numMap:
                numMap[nums[i]] += 1
            else:
                numMap[nums[i]] = 1
        
        heap = [] # freq -> key
        for num in numMap.keys():
            heapq.heappush(heap, (numMap[num], num))
            if len(heap) > k:
                heapq.heappop(heap)
        
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        
        return res
            