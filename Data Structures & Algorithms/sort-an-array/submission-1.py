class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(arr, L, R, M):
            left, right, i = 0, 0, L
            leftArr = arr[L:M+1]
            rightArr = arr[M+1:R+1]

            while left < len(leftArr) and right < len(rightArr):
                if leftArr[left] <= rightArr[right]:
                    arr[i] = leftArr[left]
                    i += 1
                    left += 1
                else:
                    arr[i] = rightArr[right]
                    i += 1
                    right += 1
            
            while left < len(leftArr):
                arr[i] = leftArr[left]
                i += 1
                left += 1
            
            while right < len(rightArr):
                arr[i] = rightArr[right]
                i += 1
                right += 1


        def mergeSort(arr, L, R):
            if L >= R:
                return arr

            mid = (R + L) // 2
            mergeSort(arr, L, mid)
            mergeSort(arr, mid + 1, R)
            merge(arr, L, R, mid)
            return arr

        return mergeSort(nums, 0, len(nums) - 1)