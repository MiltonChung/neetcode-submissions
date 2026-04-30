class Solution {
    /**
     * @param {number[]} nums1
     * @param {number} m
     * @param {number[]} nums2
     * @param {number} n
     * @return {void} Do not return anything, modify nums1 in-place instead.
     */
    merge(nums1, m, nums2, n) {
        let main = m + n - 1
        let i = m - 1 // nums1
        let j = n - 1 // nums2

        while (i >= 0 && j >= 0) {
            if (nums1[i] >= nums2[j]) {
                nums1[main] = nums1[i]
                i--
            } else {
                nums1[main] = nums2[j]
                j--
            }
            main--
        }

        while (j >= 0) {
            nums1[main] = nums2[j]
            j--
            main--
        }
    }
}
