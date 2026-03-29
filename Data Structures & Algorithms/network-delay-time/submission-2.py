class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adjList = {}
        for i in range(1, n + 1):
            adjList[i] = []
        for src, dst, weight in times:
            adjList[src].append([dst, weight])
        
        visited = set()
        minHeap = [[0, k]]
        t = 0
        while minHeap:
            weight1, dst1 = heapq.heappop(minHeap)
            if dst1 in visited:
                continue
            visited.add(dst1)
            t = max(weight1, t)

            for dst2, weight2 in adjList[dst1]:
                if dst2 not in visited:
                    heapq.heappush(minHeap, [weight1 + weight2, dst2])

        if len(visited) == n:
            return t
        else:
            return -1