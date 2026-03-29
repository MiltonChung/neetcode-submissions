"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None
        adjList = {}
        adjList[node] = Node(node.val)
        self.bfs(node, adjList)
        return adjList[node]

    def bfs(self, node, adjList):
        queue = deque()
        queue.append(node)

        while queue:
            for i in range(len(queue)):
                n = queue.popleft()
                
                for neighbor in n.neighbors:
                    if neighbor not in adjList:
                        queue.append(neighbor)
                        adjList[neighbor] = Node(neighbor.val)
                    adjList[n].neighbors.append(adjList[neighbor])

        return


