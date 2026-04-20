class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums, target) {
        const diffMap = {}

        for (let i=0; i<nums.length; i++) {
            const num = nums[i]
            const difference = target - num

            if (diffMap[difference] === undefined) {
                diffMap[num] = i
            } else {
                return [diffMap[difference], i]
            }
        }
    }
}
