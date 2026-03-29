class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        adjList = {i: [] for i in range(n)}

        for i in range(len(edges)):
            src, dst = edges[i]
            adjList[src].append([dst, succProb[i]])
            adjList[dst].append([src, succProb[i]])

        visited = {}
        maxHeap = [[-1.0, start_node]]
        while maxHeap:
            prob1, n1 = heapq.heappop(maxHeap)
            prob1 = -prob1
            if n1 in visited:
                continue
            visited[n1] = prob1
            if n1 == end_node:
                break

            for n2, prob2 in adjList[n1]:
                if n2 not in visited:
                    heapq.heappush(maxHeap, [-(prob2 * prob1), n2])

        return visited.get(end_node, 0.0000)