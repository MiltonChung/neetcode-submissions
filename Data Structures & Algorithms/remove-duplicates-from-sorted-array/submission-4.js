class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    removeDuplicates(nums) {
        let L = 1
        for (let R=1; R<nums.length; R++) {
            if (nums[R] !== nums[R-1]) {
                nums[L] = nums[R]
                L++
            }
        }

        return L
    }
}
