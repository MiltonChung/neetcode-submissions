import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = {}
        for i in range(1, n + 1):
            adj[i] = []
        for s, d, w in times:
            adj[s].append([d, w])

        shortest = {}
        minHeap = [[0, k]]
        while minHeap:
            sourceWeight, source = heapq.heappop(minHeap)
            if source in shortest:
                continue
            shortest[source] = sourceWeight

            for dst, dstWeight in adj[source]:
                if dst not in shortest:
                    heapq.heappush(minHeap, [dstWeight + sourceWeight, dst])

        maxTime = 0
        if len(shortest) != n:
            return -1
        else:
            for n in shortest:
                maxTime = max(maxTime, shortest[n])
            return maxTime