# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
            
        depth = 0
        stack = []
        stack.append((root, 1))

        while stack:
            node, currDepth = stack.pop()
            if node.left:
                stack.append((node.left, currDepth + 1))
            if node.right:
                stack.append((node.right, currDepth + 1))

            depth = max(depth, currDepth)
        
        return depth
            