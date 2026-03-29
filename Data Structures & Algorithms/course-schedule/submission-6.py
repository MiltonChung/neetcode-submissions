class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = {}
        for i in range(numCourses):
          adjList[i] = []
        
        for course, prereq in prerequisites:
            if course == prereq:
                return False
            adjList[course].append(prereq)
        
        visitSet = set()
        def dfs(course):
            if course in visitSet:
                return False
            if adjList[course] == []:
                return True

            visitSet.add(course)
            for prereq in adjList[course]:
                if not dfs(prereq):
                    return False

            visitSet.remove(course)
            adjList[course] = []
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False
        
        return True
    