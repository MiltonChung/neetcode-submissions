class Solution {
    /**
     * @param {number} n
     * @return {number}
     */
    climbStairs(n) {
        const stairs = (steps) => {
            if (steps >= n) return steps === n
            return stairs(steps + 1) + stairs(steps + 2)
        }

        return stairs(0)
    }
}
