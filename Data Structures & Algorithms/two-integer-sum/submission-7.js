class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums, target) {
        const diffMap = new Map()

        for (let i=0; i<nums.length; i++) {
            const num = nums[i]
            const difference = target - num

            if (!diffMap.has(difference)) {
                diffMap.set(num, i)
            } else {
                return [diffMap.get(difference), i]
            }
        }
    }
}
