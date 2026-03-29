class Solution {
    /**
     * @param {number[]} nums
     * @return {number[]}
     */
    getConcatenation(nums) {
        const length = nums.length;
        const ansArr = new Array(length * 2)

        for (let i = 0; i < length; i++) {
            ansArr[i] = nums[i]
            ansArr[i + length] = nums[i]
        }

        return ansArr
    }
}
