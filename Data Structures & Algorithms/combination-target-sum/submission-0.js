class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @returns {number[][]}
     */
    combinationSum(nums, target) {
        let res = []
        let curr = []

        const dfs = (i, total) => {
            if (total > target || i >= nums.length) {
                return
            }
            if (total === target) {
                res.push([...curr])
                return
            }

            curr.push(nums[i])
            dfs(i, total + nums[i])

            curr.pop()
            dfs(i + 1, total)
        }

        dfs(0, 0)

        return res
    }
}
