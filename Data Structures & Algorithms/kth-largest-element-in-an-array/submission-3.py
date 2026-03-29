class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)

        while (k < len(nums)):
            heapq.heappop(nums)

        return heapq.heappop(nums)


        # negativeHeap = [-n for n in nums]

        # heapq.heapify(negativeHeap)

        # res = None
        # while (k > 0):
        #     res = -1 * heapq.heappop(negativeHeap)
        #     k = k - 1
        
        # return res