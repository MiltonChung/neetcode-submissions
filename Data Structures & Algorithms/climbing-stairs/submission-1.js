class Solution {
    /**
     * @param {number} n
     * @return {number}
     */
    climbStairs(n) {
        const stairs = (steps) => {
            if (steps > n) return 0
            if (steps === n) return 1
            return stairs(steps + 1) + stairs(steps + 2)
        }

        return stairs(0)
    }
}
