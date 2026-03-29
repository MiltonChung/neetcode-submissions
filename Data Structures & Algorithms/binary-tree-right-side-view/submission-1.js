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
     * @return {number[]}
     */
    rightSideView(root) {
        let queue = []
        let res = []
        if (root !== null) {
            queue.push(root)
        }

        while (queue.length > 0) {
            const queueLength = queue.length
            let rightSide = null

            for (let i = 0; i < queueLength; i++) {
                const curr = queue.shift()
                if (curr) {

                    rightSide = curr
                    if (curr.left !== null) {
                        queue.push(curr.left)
                    }
                    if (curr.right !== null) {
                        queue.push(curr.right)
                    }
                }
            }

            if (rightSide) res.push(rightSide.val)
        }

        return res
    }
}
