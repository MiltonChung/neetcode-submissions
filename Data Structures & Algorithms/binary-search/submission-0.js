class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number}
     */
    search(nums, target) {
        let leftIndex = 0
        let rightIndex = nums.length - 1

        while (leftIndex <= rightIndex) {
            const midIndex = Math.floor((leftIndex + rightIndex) / 2)

            if (nums[midIndex] < target) {
                leftIndex = midIndex + 1
            } else if (nums[midIndex] > target) {
                rightIndex = midIndex - 1
            } else {
                return midIndex
            }
        }

        return -1
    }
}
