class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def dfs(node):
            isRoot = False
            isLeft = False
            isRight = False

            if not node:
                return False
            if node.val == p.val or node.val == q.val:
                isRoot = True

            isLeft = dfs(node.left)
            isRight = dfs(node.right)

            if isinstance(isLeft, TreeNode): return isLeft
            if isinstance(isRight, TreeNode): return isRight

            trues = 0
            arr = [isRoot, isLeft, isRight]
            for b in arr:
                if b: trues += 1
            if trues >= 2: return node
            return isRoot or isLeft or isRight
        
        return dfs(root)