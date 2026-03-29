class Solution {
    /**
     * @param {number[]} nums
     * @return {void} Do not return anything, modify nums in-place instead.
     */
    sortColors(nums) {
        let counter = [0, 0, 0]
        for (let i = 0; i < nums.length; i++) {
            counter[nums[i]]++
        }

        let i = 0;
        for (let n = 0; n < nums.length; n++) {
            for (let j = 0; j < counter[n]; j++) {
                nums[i] = n
                i++
            }
        }
    }
}
