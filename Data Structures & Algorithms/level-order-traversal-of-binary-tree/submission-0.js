/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     constructor(val = 0, left = null, right = null) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

class Solution {
    /**
     * @param {TreeNode} root
     * @return {number[][]}
     */
    levelOrder(root) {
        let queue = []
        let res = []
        if (root !== null) {
            queue.push(root)
        }
        let level = 0
        while (queue.length > 0) {
            const levelLength = queue.length
            res[level] = []

            for (let i = 0; i < levelLength; i++) {
                const curr = queue.shift()
                res[level].push(curr.val)
                if (curr.left !== null) {
                    queue.push(curr.left)
                }
                if (curr.right !== null) {
                    queue.push(curr.right)
                }
            }
            level++
        }

        return res
    }
}
