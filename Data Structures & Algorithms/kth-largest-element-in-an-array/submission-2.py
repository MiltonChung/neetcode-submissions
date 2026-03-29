class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        negativeHeap = [-n for n in nums]

        heapq.heapify(negativeHeap)

        res = None
        while (k > 0):
            res = -1 * heapq.heappop(negativeHeap)
            k = k - 1
        
        return res