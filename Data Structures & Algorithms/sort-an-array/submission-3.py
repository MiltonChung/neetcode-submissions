class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(L, R, M):
            left, right, i = 0, 0, L
            leftArr = nums[L:M+1]
            rightArr = nums[M+1:R+1]

            while left < len(leftArr) and right < len(rightArr):
                if leftArr[left] <= rightArr[right]:
                    nums[i] = leftArr[left]
                    i += 1
                    left += 1
                else:
                    nums[i] = rightArr[right]
                    i += 1
                    right += 1
            
            while left < len(leftArr):
                nums[i] = leftArr[left]
                i += 1
                left += 1
            
            while right < len(rightArr):
                nums[i] = rightArr[right]
                i += 1
                right += 1

        def mergeSort(L, R):
            if L >= R:
                return

            mid = (R + L) // 2
            mergeSort(L, mid)
            mergeSort(mid + 1, R)
            merge(L, R, mid)

        mergeSort(0, len(nums) - 1)
        return nums