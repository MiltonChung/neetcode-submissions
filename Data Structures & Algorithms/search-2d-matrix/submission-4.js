class Solution {
    /**
     * @param {number[][]} matrix
     * @param {number} target
     * @return {boolean}
     */
    searchMatrix(matrix, target) {
        const ROW = matrix.length
        const COL = matrix[0].length

        let start = 0
        let end = ROW - 1
        while (start <= end) {
            const midRow = Math.floor((end + start) / 2)

            if (target > matrix[midRow][COL - 1]) {
                start = midRow + 1
            } else if (target < matrix[midRow][0]) {
                end = midRow - 1
            } else {
                // The target might be in this midRow
                break
            }
        }

        if (start > end) return false

        const midRow = Math.floor((end + start) / 2)
        let left = 0
        let right = COL - 1
        while (left <= right) {
            const mid = Math.floor((right + left) / 2)

            if (target > matrix[midRow][mid]) {
                left = mid + 1
            } else if (target < matrix[midRow][mid]) {
                right = mid - 1
            } else {
                return true
            }
        }

        return false
    }
}








