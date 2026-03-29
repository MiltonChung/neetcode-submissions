class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while (len(stones) > 1):
            minHeap = stones[:]
            heapq.heapify(minHeap)
            while len(minHeap) > 2:
                heapq.heappop(minHeap)

            res = minHeap[0] - minHeap[1]
            i = stones.index(minHeap[0])
            stones.pop(i)
            j = stones.index(minHeap[1])
            stones.pop(j)

            if res > 0:
                stones.append(res)
            elif res < 0:
                stones.append(-res)

        if len(stones) == 1:
            return stones[0]
        else:
            return 0
