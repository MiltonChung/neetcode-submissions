class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums, target) {
        const diff = {}

        for (let i=0; i<nums.length; i++) {
            const d = target - nums[i]
            
            if (diff[d] !== undefined) {
                return [diff[d], i]
            } else {
                diff[nums[i]] = i
            }
        }
    }
}
