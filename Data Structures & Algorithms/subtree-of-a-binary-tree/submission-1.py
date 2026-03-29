class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def mainDfs(node):
            if not subRoot:
                return True
            if not node:
                return False
            
            if node.val == subRoot.val:
                if matchDfs(node, subRoot):
                    return True
            
            return mainDfs(node.left) or mainDfs(node.right)

        def matchDfs(n1, n2):
            if not n1 and not n2:
                return True
            if not n1 or not n2 or n1.val != n2.val:
                return False

            return matchDfs(n1.left, n2.left) and matchDfs(n1.right, n2.right)

        return mainDfs(root)