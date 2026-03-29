class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = {}
        for i in range(numCourses):
          adjList[i] = []
        
        for course, prereq in prerequisites:
            if course == prereq:
                return False
            adjList[prereq].append([course, 0])
        print(adjList)
        return self.bfs(adjList)
        
    def bfs(self, adjList):
      lastVisited = None
      course = 0
      queue = deque()
      queue.append(course)

      print('outside', adjList[course], len(adjList[course]))
      while queue:
        for i in range(len(queue)):
          p = queue.popleft()
          if len(adjList[p]) < 1:
            course += 1
            continue

          for nei in adjList[p]:
            print('inside', p, adjList[p], nei)
            if nei[1] == 1:
                return False
            queue.append(nei[0])
            nei[1] = 1
            print('after', nei, queue)
      
      return True
    
    