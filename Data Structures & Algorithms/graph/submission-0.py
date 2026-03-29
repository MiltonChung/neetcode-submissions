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
        visitSet = set()

        def dfs(node):
            if node in visitSet:
                return 0
            if node == dst:
                return 1

            count = 0
            visitSet.add(node)
            for neighbor in self.validNodes[node]:
                count += dfs(neighbor)
            visitSet.remove(node)
            
            return count

        if dfs(src) > 0:
            return True
        else:
            return False

