class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleetStack = []
        sortedPositions = [] # (pos, speed)

        # Sort by descending order and process the higher car positions first
        for i in range(len(position)):
            sortedPositions.append((position[i], speed[i]))
        sortedPositions.sort(key=lambda p:p[0], reverse=True)

        # Calculate time to taget
        for pos, spe in sortedPositions:
            timeToTarget = (target - pos) / spe
            if not fleetStack or fleetStack[-1] < timeToTarget:
                fleetStack.append(timeToTarget)

        return len(fleetStack)