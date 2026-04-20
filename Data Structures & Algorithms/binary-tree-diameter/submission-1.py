class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxDiameter = 0

        def dfs(node):
            nonlocal maxDiameter

            if node is None:
                return 0
                
            left = dfs(node.left)
            right = dfs(node.right)
            maxDiameter = max(maxDiameter, left + right)
            
            return 1 + max(dfs(node.left), dfs(node.right))
        
        dfs(root)
        return maxDiameter