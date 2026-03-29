class Graph:
    
    def __init__(self):
        self.validNodes = {}

    def addEdge(self, src: int, dst: int) -> None:
        if src not in self.validNodes:
            self.validNodes[src] = []
        if dst not in self.validNodes:
            self.validNodes[dst] = []

        self.validNodes[src].append(dst)

    def removeEdge(self, src: int, dst: int) -> bool:
        if src not in self.validNodes or dst not in self.validNodes:
            return False
        
        source = self.validNodes[src]
        indexToRemove = source.index(dst)
        source.pop(indexToRemove)

        return True
    
    def hasPath(self, src: int, dst: int) -> bool:
        visit = set()
        queue = deque()
        # visit.add(src)
        queue.append(src)

        while queue:
            node = queue.popleft()
            if node == dst:
                return True
            visit.add(node)
            for neighbor in self.validNodes[node]:
                if neighbor not in visit:
                    queue.append(neighbor)
                    visit.add(neighbor)
        
        return False

    # def hasPath(self, src: int, dst: int) -> bool:
    #     visitSet = set()

    #     def dfs(node):
    #         if node == dst:
    #             return True

    #         visitSet.add(node)
    #         for neighbor in self.validNodes[node]:
    #             if neighbor not in visitSet:
    #                 if dfs(neighbor):
    #                     return True
            
    #         return False

    #     return dfs(src)

