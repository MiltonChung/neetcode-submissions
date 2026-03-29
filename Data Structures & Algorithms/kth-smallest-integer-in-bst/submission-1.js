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
     * @param {number} k
     * @return {number}
     */
    kthSmallest(root, k) {
        let res = []

        const inorder = (root) => {
            if (root === null) return root

            inorder(root.left)
            res.push(root.val)
            inorder(root.right)
        }

        inorder(root)
        return res[k - 1]

        // Iterative:
        // let stack = []
        // let curr = root
        // let count = 0

        // while (curr || stack.length > 0) {
        //     while (curr) {
        //     stack.push(curr)
        //     curr = curr.left
        //     }

        //     curr = stack.pop()
        //     count++
        //     if (count === k) {
        //     return curr.val
        //     }
        //     curr = curr.right
        // }
    }
}
