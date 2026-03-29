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
     * @param {number[]} preorder
     * @param {number[]} inorder
     * @return {TreeNode}
     */
    buildTree(preorder, inorder) {
        if (preorder.length < 1 || inorder.length < 1) return null

        const root = new TreeNode(preorder[0])
        const midIndex = inorder.indexOf(preorder[0])
        root.left = this.buildTree(
            preorder.slice(1, midIndex + 1), // midIndex here is used to determine how many nodes are in the left subtree
            inorder.slice(0, midIndex)
        )
        root.right = this.buildTree(
            preorder.slice(midIndex + 1),
            inorder.slice(midIndex + 1)
        )
        return root
    }
}
