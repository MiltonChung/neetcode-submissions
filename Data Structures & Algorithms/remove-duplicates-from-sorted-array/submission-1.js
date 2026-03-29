class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    removeDuplicates(nums) {
        let startIndex = 1

        for(let endIndex=1; endIndex < nums.length; endIndex++) {
            if (nums[endIndex] !== nums[endIndex - 1]) {
                nums[startIndex] = nums[endIndex]
                startIndex++
            }
        }

        return startIndex
    }
}
