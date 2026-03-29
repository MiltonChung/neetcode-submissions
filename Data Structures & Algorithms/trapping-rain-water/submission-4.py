class Solution:
    def trap(self, height: List[int]) -> int:
        maxArea = 0

        leftBound, rightBound  = 0, len(height) - 1
        while leftBound + 1 < len(height) and height[leftBound] <= height[leftBound + 1]:
            leftBound += 1
        while rightBound - 1 > 0 and height[rightBound - 1] >= height[rightBound]:
            rightBound -= 1
        
        newHeights = height[leftBound : rightBound + 1]
				
        leftWall = 0
        for rightCandidate in range(1, len(newHeights)):
            if newHeights[rightCandidate] >= newHeights[leftWall]:
                waterLevel = newHeights[leftWall]
                width = rightCandidate - leftWall - 1
                area = width * waterLevel

                leftWall += 1
                while leftWall  != rightCandidate:
                    area -= newHeights[leftWall]
                    leftWall += 1

                maxArea += area
        
        rightWall = len(newHeights) - 1
        for leftCandidate in range(len(newHeights) - 2, -1, -1):
            if newHeights[leftCandidate] > newHeights[rightWall]:
                waterLevel = newHeights[rightWall]
                width = rightWall - leftCandidate - 1
                area = width * waterLevel

                rightWall -= 1
                while rightWall > leftCandidate:
                    area -= newHeights[rightWall]
                    rightWall -= 1

                maxArea += area
        return maxArea