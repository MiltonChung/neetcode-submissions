class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        maxSize, curSize = 1, 1
        prev = 0
        
        for k in range(len(arr) - 1):
            if arr[k] < arr[k + 1]:
                if prev == -1:
                    curSize += 1
                else:
                    curSize = 2
                
                prev = 1
            elif arr[k] > arr[k + 1]:
                if prev == 1:
                    curSize += 1
                else:
                    curSize = 2
                
                prev = -1
            else:
                prev = 0
                curSize = 1
            
            maxSize = max(curSize, maxSize)
            
        return maxSize