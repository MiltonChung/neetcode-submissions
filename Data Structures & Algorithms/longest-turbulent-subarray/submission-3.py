class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        prev = ''
        maxSize, currSize = 1, 1

        for i in range(1, len(arr)):
            if arr[i - 1] > arr[i]:
                if prev == '<':
                    currSize += 1
                    prev = '>'
                else:
                    currSize = 2
                    prev = '>'
            elif arr[i - 1] < arr[i]:
                if prev == '>':
                    currSize += 1
                    prev = '<'
                else:
                    currSize = 2
                    prev = '<'
            else:
                currSize = 1
                prev = '='

            maxSize = max(currSize, maxSize)

        return maxSize