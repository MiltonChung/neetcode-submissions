class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        sortedPositions = [] # (pos, speed)

        # Sort by descending order and process the higher car positions first
        for i in range(len(position)):
            sortedPositions.append((position[i], speed[i]))
        sortedPositions.sort(key=lambda p:p[0], reverse=True)

        fleet = 1
        prevTime = (target - sortedPositions[0][0]) / sortedPositions[0][1]
        # Calculate time to taget
        for i in range(1, len(sortedPositions)):
            currCar = sortedPositions[i]
            timeToTarget = (target - currCar[0]) / currCar[1]
            if timeToTarget > prevTime:
                fleet += 1
                prevTime = timeToTarget

        return fleet