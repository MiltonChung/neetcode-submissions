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
     * @param {number} key
     * @return {TreeNode}
     */
    deleteNode(root, key) {
        function deleteNodeHelper(root, key) {
            if (root === null) return root

            if (key < root.val) {
                root.left = deleteNodeHelper(root.left, key)
            } else if (key > root.val) {
                root.right = deleteNodeHelper(root.right, key)
            } else {
                if (root.left === null) {
                    return root.right
                } else if (root.right === null) {
                    return root.left
                } else {
                    const minNode = findAndReturnMinFromBST(root.right)
                    root.val = minNode.val
                    root.right = deleteNodeHelper(root.right, minNode.val)
                }
            }

            return root
        }

        return deleteNodeHelper(root, key)
    }
}


function findAndReturnMinFromBST(root) {
    let curr = root

    while (curr && curr.left) {
        curr = curr.left
    }

    return curr
}
