class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    removeDuplicates(nums) {
        const uniq = new Map();

        for (const n of nums) {
            if (!uniq.has(n)) {
                uniq.set(n, n)
            }
        }

        let i = 0;
        for (const n of uniq.keys()) {
            nums[i] = n;
            i++;
        }

        return uniq.size;
    }
}
