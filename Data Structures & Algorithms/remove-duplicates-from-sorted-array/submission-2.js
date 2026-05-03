class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    removeDuplicates(nums) {
        const uniq = [];

        for (const n of nums) {
            if (!uniq.includes(n)) {
                uniq.push(n);
            }
        }

        for (let i = 0; i < uniq.length; i++) {
            nums[i] = uniq[i];
        }

        return uniq.length;
    }
}
