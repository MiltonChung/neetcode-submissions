class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {
        const hashset = new Set()

        for (const num of nums) {
            if (hashset.has(num)) return true
            else hashset.add(num)
        }

        return false
    }
}
