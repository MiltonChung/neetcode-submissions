class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleetStack = []
        sortedPositions = [] # (pos, speed)

        for i in range(len(position)):
            sortedPositions.append((position[i], speed[i]))
        sortedPositions.sort(key=lambda p:p[0], reverse=True)

        for i in range(len(sortedPositions)):
            turns = (target - sortedPositions[i][0]) / sortedPositions[i][1]
            if not fleetStack or fleetStack[-1] < turns:
                fleetStack.append(turns)

        return len(fleetStack)